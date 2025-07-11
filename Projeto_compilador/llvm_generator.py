# llvm_generator.py (VERSÃO FINAL E ROBUSTA)
import ast
from llvmlite import ir, binding
from tac_generator import Var, Temp, Constant, Label

class LLVMGenerator:
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()

        self.module = ir.Module(name="meu_programa")
        self.module.triple = self.binding.get_default_triple()

        self.symbol_table = {}
        self.blocks = {} # Dicionário para guardar os blocos já criados
        self.func = None # Para guardar a referência da função main
        self.builder = None

        self.int_type = ir.IntType(32)
        self.float_type = ir.DoubleType()
        self.void_ptr_type = ir.IntType(8).as_pointer()

    def _declare_runtime_functions(self):
        printf_type = ir.FunctionType(self.int_type, [self.void_ptr_type], var_arg=True)
        ir.Function(self.module, printf_type, name="printf")
        read_double_type = ir.FunctionType(self.float_type, [])
        ir.Function(self.module, read_double_type, name="read_double")

    def _get_llvm_operand(self, tac_operand):
        if isinstance(tac_operand, (Var, Temp)):
            llvm_val = self.symbol_table.get(tac_operand.name)
            if llvm_val is None:
                raise NameError(f"Operando desconhecido: {tac_operand.name}")
            if isinstance(llvm_val, ir.AllocaInstr):
                return self.builder.load(llvm_val, name=tac_operand.name + "_val")
            else:
                return llvm_val
        elif isinstance(tac_operand, Constant):
            if isinstance(tac_operand.name, float):
                return ir.Constant(self.float_type, tac_operand.name)
            else:
                return ir.Constant(self.int_type, tac_operand.name)
        return None

    def _get_or_create_block(self, label_name):
        """Cria um bloco LLVM se ele não existir, ou retorna o existente."""
        if label_name not in self.blocks:
            self.blocks[label_name] = self.func.append_basic_block(name=label_name)
        return self.blocks[label_name]

    def generate(self, tac_code):
        self._declare_runtime_functions()

        main_func_type = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, main_func_type, name="main")
        
        entry_block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        # Pré-passo para alocar variáveis
        for instr in tac_code:
            if isinstance(instr.result, Var) and instr.result.name not in self.symbol_table:
                ptr = self.builder.alloca(self.float_type, name=instr.result.name)
                self.symbol_table[instr.result.name] = ptr
        
        # NÃO vamos mais pré-criar os blocos. Eles serão criados sob demanda.

        for i, instr in enumerate(tac_code):
            if instr.opcode == 'LABEL':
                # Pega ou cria o bloco para este rótulo
                block = self._get_or_create_block(instr.result.name)
                # Se o bloco anterior não terminou com um salto, cria um salto para este novo bloco
                if not self.builder.block.is_terminated:
                    self.builder.branch(block)
                # Move o builder para o novo bloco
                self.builder.position_at_end(block)

            elif instr.opcode == 'GOTO':
                target_block = self._get_or_create_block(instr.result.name)
                # Garante que o bloco atual termine com este salto incondicional
                if not self.builder.block.is_terminated:
                    self.builder.branch(target_block)

            elif instr.opcode == 'IF_FALSE':
                condition = self._get_llvm_operand(instr.arg1)
                false_block = self._get_or_create_block(instr.result.name)
                
                # O bloco "true" é sempre o próximo, então criamos um novo para ele
                true_block = self.func.append_basic_block(name=f"if_true_{i}")
                
                # Gera o salto condicional
                self.builder.cbranch(condition, true_block, false_block)
                # Move o builder para o bloco "true" para continuar a geração
                self.builder.position_at_end(true_block)

            # --- O restante da lógica de tradução de instruções permanece o mesmo ---
            elif instr.opcode in ['+', '-', '*', '/', '==', '!=', '<', '>', '<=', '>=', '&&', '||']:
                lhs = self._get_llvm_operand(instr.arg1)
                rhs = self._get_llvm_operand(instr.arg2)
                op_map = {
                    '+': self.builder.fadd, '-': self.builder.fsub, '*': self.builder.fmul, '/': self.builder.fdiv,
                    '&&': self.builder.and_, '||': self.builder.or_
                }
                if instr.opcode in op_map:
                    result = op_map[instr.opcode](lhs, rhs, name=instr.result.name)
                else: # Operadores de comparação
                    result = self.builder.fcmp_ordered(instr.opcode, lhs, rhs, name=instr.result.name)
                self.symbol_table[instr.result.name] = result

            elif instr.opcode == 'ASSIGN':
                source_val = self._get_llvm_operand(instr.arg1)
                target_ptr = self.symbol_table[instr.result.name]
                self.builder.store(source_val, target_ptr)

            elif instr.opcode == 'READ':
                target_ptr = self.symbol_table[instr.result.name]
                read_func = self.module.get_global("read_double")
                read_value = self.builder.call(read_func, [], name="input_val")
                self.builder.store(read_value, target_ptr)


            elif instr.opcode == 'WRITE':
                operand_to_print = instr.result

                # Determina o formato e o valor a ser passado para o printf
                if isinstance(operand_to_print, Constant) and isinstance(operand_to_print.name, str) and operand_to_print.name.startswith('"'):
                    # Cenário 1: É uma string literal
                    format_str = "%s"  # O formato é para string

                    # Usa ast.literal_eval para interpretar corretamente escapes como \n
                    try:
                        py_str = ast.literal_eval(operand_to_print.name)
                    except (ValueError, SyntaxError):
                        py_str = operand_to_print.name.strip('"') # Fallback

                    # Cria a string global C, null-terminated
                    c_str_val = bytearray((py_str + '\0').encode('utf-8'))
                    c_str = ir.Constant(ir.ArrayType(ir.IntType(8), len(c_str_val)), c_str_val)
                    str_ptr = ir.GlobalVariable(self.module, c_str.type, name=f"str_const_{i}")
                    str_ptr.initializer = c_str
                    str_ptr.linkage = 'internal'

                    value_to_pass = self.builder.bitcast(str_ptr, self.void_ptr_type)
                else:
                    # Cenário 2: É um número
                    format_str = "%f"  # O formato é para float, SEM \n
                    value_to_pass = self._get_llvm_operand(operand_to_print)

                # Agora, cria a string de formato global, também null-terminated
                fmt_bytes = bytearray((format_str + '\0').encode('utf-8'))
                global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_bytes)), name=f"fmt_str_{i}")
                global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_bytes)), fmt_bytes)
                global_fmt.linkage = 'internal'

                # Pega um ponteiro para a string de formato
                fmt_ptr = self.builder.bitcast(global_fmt, self.void_ptr_type)

                # Chama a função printf
                printf_func = self.module.get_global("printf")
                self.builder.call(printf_func, [fmt_ptr, value_to_pass])

        # Finalizar a função main com um retorno, caso o último bloco não tenha sido terminado
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))

        return str(self.module)
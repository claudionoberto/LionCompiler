# tac_generator.py (VERSÃO CORRIGIDA)

from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

# As classes TACOperand e TACInstruction não mudam.
class TACOperand:
    def __init__(self, name): self.name = name
    def __str__(self): return str(self.name)
class Var(TACOperand): pass
class Temp(TACOperand): pass
class Label(TACOperand): pass
class Constant(TACOperand):
    def __init__(self, name):
        if isinstance(name, str) and name.startswith('"'): self.name = name
        else: self.name = name

class TACInstruction:
    def __init__(self, opcode, result, arg1=None, arg2=None):
        self.opcode, self.result, self.arg1, self.arg2 = opcode, result, arg1, arg2
    def __str__(self):
        op = self.opcode
        if op in ['+', '-', '*', '/', '==', '!=', '<', '>', '<=', '>=', '&&', '||']:
            return f"{self.result} := {self.arg1} {op} {self.arg2}"
        elif op == 'ASSIGN': return f"{self.result} := {self.arg1}"
        elif op == 'NOT': return f"{self.result} := {op} {self.arg1}"
        elif op == 'GOTO': return f"GOTO {self.result}"
        elif op == 'IF_FALSE': return f"IF_FALSE {self.arg1} GOTO {self.result}"
        elif op == 'LABEL': return f"{self.result}:"
        elif op == 'READ': return f"READ {self.result}"
        elif op == 'WRITE': return f"WRITE {self.result}"
        else: return f"Unknown Opcode: {op}"

# -----------------------------------------------------------------------------
# O GERADOR DE TAC (Visitor) - CORRIGIDO
# -----------------------------------------------------------------------------

class TACGenerator(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.tac_code = []
        self._temp_count = 0
        self._label_count = 0

    def _new_temp(self):
        temp = Temp(f"_t{self._temp_count}")
        self._temp_count += 1
        return temp

    def _new_label(self):
        label = Label(f"L{self._label_count}")
        self._label_count += 1
        return label

    def add_instruction(self, opcode, result, arg1=None, arg2=None):
        self.tac_code.append(TACInstruction(opcode, result, arg1, arg2))

    # --- Métodos do Visitor para as regras da sua gramática ---

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        self.visit(ctx.declarations())
        return self.tac_code

    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        var_name = Var(ctx.ID().getText())
        expr_result = self.visit(ctx.expression())
        self.add_instruction('ASSIGN', var_name, expr_result)

    def visitOutputCommand(self, ctx:ExprParser.OutputCommandContext):
        expr_result = self.visit(ctx.expression())
        self.add_instruction('WRITE', expr_result)

    def visitInputCommand(self, ctx:ExprParser.InputCommandContext):
        var_name = Var(ctx.ID().getText())
        self.add_instruction('READ', var_name)


    def visitIfCommand(self, ctx:ExprParser.IfCommandContext):
        label_false = self._new_label()
        
        if ctx.ELSE():
            # Se temos um bloco ELSE, precisamos de um rótulo para o final de tudo
            label_end = self._new_label()
            
            # Gera o código da condição
            condition_result = self.visit(ctx.expression())
            self.add_instruction('IF_FALSE', label_false, condition_result)
            
            # Gera o código do bloco THEN
            self.visit(ctx.block(0))
            # Após o THEN, pula para o final
            self.add_instruction('GOTO', label_end)
            
            # Gera o código do bloco ELSE
            self.add_instruction('LABEL', label_false)
            self.visit(ctx.block(1))
            
            # Marca o final de toda a estrutura
            self.add_instruction('LABEL', label_end)
        else:
            # Se NÃO temos um bloco ELSE (if simples)
            condition_result = self.visit(ctx.expression())
            self.add_instruction('IF_FALSE', label_false, condition_result)
            
            # Gera o código do bloco THEN
            self.visit(ctx.block(0))
            
            # Marca o final da estrutura
            self.add_instruction('LABEL', label_false)

    def visitWhileCommand(self, ctx:ExprParser.WhileCommandContext):
        label_start, label_end = self._new_label(), self._new_label()
        self.add_instruction('LABEL', label_start)
        condition_result = self.visit(ctx.expression())
        self.add_instruction('IF_FALSE', label_end, condition_result)
        self.visit(ctx.block())
        self.add_instruction('GOTO', label_start)
        self.add_instruction('LABEL', label_end)

    # --- Expressões (visitando os filhos e retornando o resultado) ---

    def visitParenExpr(self, ctx:ExprParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitStringExpr(self, ctx:ExprParser.StringExprContext):
        return Constant(ctx.STRING().getText())
        
    def visitIdExpr(self, ctx:ExprParser.IdExprContext):
        return Var(ctx.ID().getText())

    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return Constant(float(ctx.NUMBER().getText()))

    def visitArithExpr(self, ctx:ExprParser.ArithExprContext):
        return self.visit(ctx.arithmeticExpression())

    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        return self.visit(ctx.logicalExpression())
    
    def visitConcatExpr(self, ctx:ExprParser.ConcatExprContext):
        left, right = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        result = self._new_temp()
        self.add_instruction('+', result, left, right)
        return result

    def visitArithmeticExpression(self, ctx:ExprParser.ArithmeticExpressionContext):
        left = self.visit(ctx.term(0))
        for i in range(len(ctx.term()))[1:]:
            op, right = ctx.arithmeticOperator(i-1).getText(), self.visit(ctx.term(i))
            result = self._new_temp()
            self.add_instruction(op, result, left, right)
            left = result
        return left

    def visitTerm(self, ctx:ExprParser.TermContext):
        left = self.visit(ctx.factor(0))
        for i in range(len(ctx.factor()))[1:]:
            op, right = ctx.termOperator(i-1).getText(), self.visit(ctx.factor(i))
            result = self._new_temp()
            self.add_instruction(op, result, left, right)
            left = result
        return left

    # CORREÇÃO CRÍTICA 1: Implementação do visitFactor
    def visitFactor(self, ctx:ExprParser.FactorContext):
        if ctx.NUMBER():
            return Constant(float(ctx.NUMBER().getText()))
        if ctx.ID():
            return Var(ctx.ID().getText())
        if ctx.arithmeticExpression():
            return self.visit(ctx.arithmeticExpression())
        return None

    def visitComparison(self, ctx:ExprParser.ComparisonContext):
        left, right = self.visit(ctx.arithmeticExpression(0)), self.visit(ctx.arithmeticExpression(1))
        op = ctx.comparisonOperator().getText()
        result = self._new_temp()
        self.add_instruction(op, result, left, right)
        return result

    def visitLogicalExpression(self, ctx:ExprParser.LogicalExpressionContext):
        left = self.visit(ctx.logicalTerm(0))
        for i in range(len(ctx.logicalTerm()))[1:]:
            op, right = ctx.OR(i-1).getText(), self.visit(ctx.logicalTerm(i))
            result = self._new_temp()
            self.add_instruction(op, result, left, right)
            left = result
        return left

    def visitLogicalTerm(self, ctx:ExprParser.LogicalTermContext):
        left = self.visit(ctx.logicalFactor(0))
        for i in range(len(ctx.logicalFactor()))[1:]:
            op, right = ctx.AND(i-1).getText(), self.visit(ctx.logicalFactor(i))
            result = self._new_temp()
            self.add_instruction(op, result, left, right)
            left = result
        return left
    
    # CORREÇÃO CRÍTICA 2: Tornar visitLogicalFactor explícito
    def visitLogicalFactor(self, ctx:ExprParser.LogicalFactorContext):
        if ctx.NOT():
            operand, result = self.visit(ctx.logicalFactor()), self._new_temp()
            self.add_instruction('NOT', result, operand)
            return result
        if ctx.logicalExpression():
            return self.visit(ctx.logicalExpression())
        if ctx.comparison():
            return self.visit(ctx.comparison())
        return None
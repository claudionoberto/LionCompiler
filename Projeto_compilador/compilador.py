# compilador.py (VERSÃO FINAL COMPLETA)

import sys
import argparse
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Importa todas as classes necessárias das outras fases
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from AnalisadorSemantico import SemanticAnalyzer
from tac_generator import TACGenerator
from llvm_generator import LLVMGenerator

class CustomSyntaxErrorListener(ErrorListener):
    """
    Listener customizado que armazena erros sintáticos em uma lista
    em vez de apenas imprimi-los no console.
    """
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = offendingSymbol.text if offendingSymbol else "EOF"
        # Mensagem mais amigável
        if "expecting" in msg:
            expected = msg.split("expecting ")[1].replace('<EOF>', 'fim do arquivo')
            error_msg = f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: Encontrado '{token_text}', mas era esperado {expected}"
        else:
            error_msg = f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: Entrada inválida perto de '{token_text}'"
        
        self.errors.append(error_msg)

def main():
    """
    Função principal que orquestra todo o pipeline do compilador.
    """
    # --- Configuração dos Argumentos ---
    arg_parser = argparse.ArgumentParser(description='Compilador para a linguagem LION.')
    arg_parser.add_argument('input_file', type=str, help='Arquivo de código-fonte a ser compilado.')
    arg_parser.add_argument('--gerar-tac', action='store_true', help='Salva o arquivo de Código de Três Endereços (TAC).')
    arg_parser.add_argument('--gerar-llvm', action='store_true', help='Gera o código final em LLVM IR.')
    
    args = arg_parser.parse_args()
    input_path = args.input_file

    # --- Definição dos Nomes de Arquivos de Saída ---
    base_name = input_path.rsplit('.', 1)[0]
    log_file = base_name + '.log'
    tac_file = base_name + '.tac'
    llvm_file = base_name + '.ll'

    print(f"Compilando o arquivo: {input_path}")

    try:
        # --- FASE 1: ANÁLISE LÉXICA ---
        input_stream = FileStream(input_path, encoding='utf-8')
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        # --- FASE 2: ANÁLISE SINTÁTICA ---
        parser = ExprParser(token_stream)
        
        # Configurando nosso listener de erro customizado
        parser.removeErrorListeners()
        error_listener = CustomSyntaxErrorListener()
        parser.addErrorListener(error_listener)
        
        # Executando o parser
        tree = parser.program()
        
        # Verificando se ocorreram erros sintáticos
        syntax_errors = error_listener.errors
        if syntax_errors:
            print(f"\nERRO: {len(syntax_errors)} erro(s) sintático(s) encontrado(s). Compilação interrompida.")
            for error in syntax_errors:
                print(f"  - {error}")
            sys.exit(1)
            
        print("Análise sintática concluída sem erros.")

        # --- FASE 3: ANÁLISE SEMÂNTICA ---
        open(log_file, 'w').close() # Limpa o log anterior
        semantic_analyzer = SemanticAnalyzer(log_file)
        semantic_errors = semantic_analyzer.analyze(tree)

        if semantic_errors:
            print(f"\nERRO: {len(semantic_errors)} erro(s) semântico(s) encontrado(s). Compilação interrompida.")
            for error in semantic_errors:
                print(f"  - {error}")
            sys.exit(1)
        
        print(f"Análise semântica concluída sem erros. Log disponível em '{log_file}'.")

        # --- FASE 4: GERAÇÃO DE CÓDIGO INTERMEDIÁRIO (TAC) ---
        # Esta etapa agora é executada internamente para que a FASE 5 tenha o que processar.
        tac_gen = TACGenerator()
        tac_code = tac_gen.visit(tree)
        
        # O flag --gerar-tac agora apenas controla se o arquivo .tac é salvo no disco
        if args.gerar_tac:
            print("\nSalvando Código de Três Endereços (TAC)...")
            with open(tac_file, 'w', encoding='utf-8') as f:
                f.write("--- CÓDIGO DE TRÊS ENDEREÇOS (TAC) ---\n\n")
                for instruction in tac_code:
                    f.write(str(instruction) + '\n')
            print(f"Arquivo TAC salvo em: {tac_file}")

        # --- FASE 5: GERAÇÃO DE CÓDIGO FINAL (LLVM IR) ---
        # Esta seção só é executada se o flag --gerar-llvm for fornecido.
        if args.gerar_llvm:
            print("\nIniciando geração de Código Final (LLVM IR)...")
            llvm_gen = LLVMGenerator()
            llvm_ir_code = llvm_gen.generate(tac_code) # Passa a lista de TAC

            with open(llvm_file, 'w', encoding='utf-8') as f:
                f.write(llvm_ir_code)
            print(f"Geração de LLVM IR concluída. Código salvo em: {llvm_file}")
            print("\nPara compilar e executar o código gerado, você precisará do LLVM instalado.")
            print("Use os seguintes comandos:")
            print(f"  1. llc -filetype=obj {llvm_file} -o {base_name}.o")
            print(f"  2. clang {base_name}.o -o {base_name}")
            print(f"  3. ./{base_name}")

    except FileNotFoundError:
        print(f"ERRO: O arquivo de entrada '{input_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a compilação: {e}")

if __name__ == '__main__':
    main()
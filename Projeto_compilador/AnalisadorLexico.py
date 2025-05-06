import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from ExprLexer import ExprLexer
from ExprParser import ExprParser

class LexicoErrorListener(ErrorListener):
    """Listener personalizado para capturar erros léxicos do ANTLR"""
    
    def __init__(self, output_file=None):
        super().__init__()
        self.errors = []
        self.output_file = output_file
        self.log_buffer = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Chamado quando ocorre um erro de sintaxe"""
        if offendingSymbol is None and hasattr(recognizer, 'getInputStream'):
            char = recognizer.getInputStream().getText(recognizer._tokenStartCharIndex, recognizer._tokenStartCharIndex)
            error_msg = f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo '{char}' inválido"
        else:
            char = offendingSymbol.text if offendingSymbol else "?"
            error_msg = f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo '{char}' inválido"
        
        self.errors.append(error_msg)
        self.log(error_msg)
    
    def log(self, message):
        print(message)
        self.log_buffer.append(message)
        
        if self.output_file:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
    
    def get_errors(self):
        return self.errors

class Scanner:
    def __init__(self, lexer_class, input_file, log_file=None, output_file=None):
        self.lexer_class = lexer_class
        self.input_file = input_file
        self.log_file = log_file
        self.output_file = output_file
        self.tokens = []
        self.errors = []
        self.log_buffer = []
        self.lexer = None
        self.error_listener = LexicoErrorListener(log_file)
    
    def log(self, message):
        print(message)
        self.log_buffer.append(message)
        
        if self.log_file:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
    
    def save_tokens(self):
        if self.output_file:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for token in self.tokens:
                    f.write(f"{self.format_token(token)}\n")
            self.log(f"Tokens salvos em {self.output_file}")
    
    def format_token(self, token):
        token_name = self.lexer.symbolicNames[token.type]
        if not token_name:
            token_name = str(token.type)
        return f"<{token_name},{token.text}> [L{token.line},C{token.column}]"
    
    def analyze(self):
        try:
            if self.log_file:
                open(self.log_file, 'w').close()
            
            self.log(f"Iniciando análise léxica do arquivo: {self.input_file}")
            
            input_stream = FileStream(self.input_file, encoding='utf-8')
            self.lexer = self.lexer_class(input_stream)
            
            self.lexer.removeErrorListeners()
            self.lexer.addErrorListener(self.error_listener)
            
            token_stream = CommonTokenStream(self.lexer)
            token_stream.fill()
            
            self.tokens = [t for t in token_stream.tokens if t.type != Token.EOF]
            
            for token in self.tokens:
                token_name = self.lexer.symbolicNames[token.type]
                
                if token_name == "ErrorChar":
                    char = token.text
                    error_msg = f"ERRO LÉXICO [Linha {token.line}, Coluna {token.column}]: Símbolo '{char}' inválido"
                    self.errors.append(error_msg)
                    self.log(error_msg)
                else:
                    self.log(f"Token encontrado: {self.format_token(token)}")
            
            self.errors.extend(self.error_listener.get_errors())
            
            self.log(f"Análise léxica concluída. {len(self.tokens)} tokens encontrados, {len(self.errors)} erros.")
            
            self.save_tokens()
            
            return self.tokens, self.errors
        
        except Exception as e:
            error_msg = f"Erro ao analisar o arquivo: {str(e)}"
            self.log(error_msg)
            return [], [error_msg]


def main():
    if len(sys.argv) < 3:
        print("Uso: python scanner.py <arquivo_entrada> <arquivo_saida> [arquivo_log]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        scanner = Scanner(ExprLexer, input_file, log_file, output_file)
        tokens, errors = scanner.analyze()
        
        if errors:
            print(f"\nAnálise concluída com {len(errors)} erros:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("\nAnálise concluída sem erros.")
            
    except Exception as e:
        print(f"Erro ao executar o scanner: {str(e)}")

if __name__ == "__main__":
    main()

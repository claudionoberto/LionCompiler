from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.error.ErrorListener import ErrorListener
import graphviz
import sys

class ASTNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def to_dot(self, dot=None, parent=None):
        if dot is None:
            dot = graphviz.Digraph()
        dot.node(str(id(self)), self.name)
        if parent:
            dot.edge(str(id(parent)), str(id(self)))
        for child in self.children:
            child.to_dot(dot, self)
        return dot

class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = offendingSymbol.text if offendingSymbol else "EOF"
        error_msg = f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg.replace('<EOF>', 'EOF')} (encontrado '{token_text}')"
        self.errors.append(error_msg)

    def get_errors(self):
        return self.errors

def build_ast(ctx):
    node = ASTNode(type(ctx).__name__)
    for child in ctx.getChildren():
        if isinstance(child, ParserRuleContext):
            node.add_child(build_ast(child))
        else:
            node.add_child(ASTNode(child.getText()))
    return node

def generate_ast(input_path, output_dot_path):
    input_stream = FileStream(input_path, encoding='utf-8')
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)

    # Captura erros sintáticos
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    # Checa erros
    errors = error_listener.get_errors()
    if errors:
        print("\n".join(errors))
        return

    # Gera AST
    ast_root = build_ast(tree)
    dot = ast_root.to_dot()
    dot.render(output_dot_path, format='dot', cleanup=True)
    print(f"AST gerada com sucesso em: {output_dot_path}.dot")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python AnalisadorSintatico.py <arquivo_entrada> <arquivo_saida_sem_extensao>")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2]
    generate_ast(entrada, saida)

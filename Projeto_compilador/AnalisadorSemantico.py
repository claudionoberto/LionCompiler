from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

class SemanticAnalyzer:
    def __init__(self, log_file):
        self.symbol_table = {}
        self.errors = []
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(message + '\n')

    def analyze(self, ctx):
        self.visit(ctx)
        return self.errors

    def visit(self, ctx):
        node_name = type(ctx).__name__
        self.log(f"[LOG] Visitando nó: {node_name}")

        if node_name == "VariableDeclarationContext":
            var_name = ctx.ID().getText()
            var_type = ctx.type_().getText()
            if var_name in self.symbol_table:
                erro = f"Erro: variável '{var_name}' já declarada."
                self.errors.append(erro)
                self.log(f"[ERRO] {erro}")
            else:
                self.symbol_table[var_name] = var_type
                self.log(f"[LOG] Declarando variável '{var_name}' do tipo '{var_type}'")
            for child in ctx.getChildren():
                if isinstance(child, ParserRuleContext):
                    self.visit(child)

        elif node_name == "AssignmentContext":
            var_name = ctx.ID().getText()
            expr_ctx = ctx.expression()
            self.log(f"[LOG] Atribuindo valor à variável '{var_name}'")

            if var_name not in self.symbol_table:
                erro = f"Erro: variável '{var_name}' não declarada."
                self.errors.append(erro)
                self.log(f"[ERRO] {erro}")
                self.visit(expr_ctx)
            else:
                expected_type = self.symbol_table[var_name]
                expr_type = self.eval_expression(expr_ctx)
                if expr_type is None:
                    pass
                elif expr_type != expected_type:
                    erro = (f"Erro: tipo incompatível na atribuição à variável '{var_name}'. "
                            f"Esperado '{expected_type}', encontrado '{expr_type}'.")
                    self.errors.append(erro)
                    self.log(f"[ERRO] {erro}")

        elif node_name in ("IfCommandContext", "WhileCommandContext"):
            expr_ctx = None
            for child in ctx.getChildren():
                if type(child).__name__.startswith("ExpressionContext"):
                    expr_ctx = child
                    break
            if expr_ctx:
                expr_type = self.eval_expression(expr_ctx)
                if expr_type != "bool":
                    erro = (f"Erro: expressão condicional deve ser do tipo bool, encontrado '{expr_type}'.")
                    self.errors.append(erro)
                    self.log(f"[ERRO] {erro}")
            for child in ctx.getChildren():
                if isinstance(child, ParserRuleContext):
                    self.visit(child)
        else:
            for child in ctx.getChildren():
                if isinstance(child, ParserRuleContext):
                    self.visit(child)

    def eval_expression(self, ctx):
        node_name = type(ctx).__name__
        self.log(f"[LOG] Avaliando expressão: {node_name}")

        if hasattr(ctx, "STRING") and ctx.STRING():
            return "text"
        if hasattr(ctx, "NUMBER") and ctx.NUMBER():
            return "int"
        if hasattr(ctx, "ID") and ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.symbol_table:
                erro = f"Erro: variável '{var_name}' não declarada."
                self.errors.append(erro)
                self.log(f"[ERRO] {erro}")
                return None
            return self.symbol_table[var_name]
        if node_name == "ParenExprContext":
            return self.eval_expression(ctx.expression())
        if node_name == "ConcatExprContext":
            left_type = self.eval_expression(ctx.expression(0))
            right_type = self.eval_expression(ctx.expression(1))
            if left_type == "text" and right_type == "text":
                return "text"
            else:
                erro = "Erro: operador '+' para concatenação requer dois textos."
                self.errors.append(erro)
                self.log(f"[ERRO] {erro}")
                return None
        if node_name == "LogicExprContext":
            return self.eval_logical_expression(ctx.logicalExpression())
        if node_name == "ArithExprContext":
            return self.eval_arithmetic_expression(ctx.arithmeticExpression())

        return None

    def eval_logical_expression(self, ctx):
        self.log(f"[LOG] Avaliando expressão lógica")
        return "bool"

    def eval_arithmetic_expression(self, ctx):
        self.log(f"[LOG] Avaliando expressão aritmética")
        tokens = ctx.getChildren()
        for child in tokens:
            if hasattr(child, "getText") and child.getText() is not None:
                text = child.getText()
                if text == '/':
                    right = list(tokens)[-1].getText()
                    if right == '0':
                        erro = "Erro: divisão por zero detectada."
                        self.errors.append(erro)
                        self.log(f"[ERRO] {erro}")
                elif text.isidentifier() and text not in self.symbol_table:
                    erro = f"Erro: variável '{text}' não declarada em expressão aritmética."
                    self.errors.append(erro)
                    self.log(f"[ERRO] {erro}")
        return "int"

def main(file_path, log_path):
    input_stream = FileStream(file_path, encoding="utf-8")
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.program()

    # Limpa o arquivo de log antes de iniciar
    open(log_path, 'w').close()

    semantic = SemanticAnalyzer(log_path)
    errors = semantic.analyze(tree)

    # Apenas imprime o resultado no terminal
    print("\n=== Resultado da Análise Semântica ===")
    if errors:
        print("Erros semânticos encontrados:")
        for e in errors:
            print(e)
    else:
        print("Análise semântica finalizada sem erros.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python AnalisadorSemantico.py programa.lion arquivolog.txt")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declarations.
    def visitDeclarations(self, ctx:ExprParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ExprParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type.
    def visitType(self, ctx:ExprParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#command.
    def visitCommand(self, ctx:ExprParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#inputCommand.
    def visitInputCommand(self, ctx:ExprParser.InputCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#outputCommand.
    def visitOutputCommand(self, ctx:ExprParser.OutputCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifCommand.
    def visitIfCommand(self, ctx:ExprParser.IfCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileCommand.
    def visitWhileCommand(self, ctx:ExprParser.WhileCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stringExpr.
    def visitStringExpr(self, ctx:ExprParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicExpr.
    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithExpr.
    def visitArithExpr(self, ctx:ExprParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenExpr.
    def visitParenExpr(self, ctx:ExprParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#idExpr.
    def visitIdExpr(self, ctx:ExprParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#concatExpr.
    def visitConcatExpr(self, ctx:ExprParser.ConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:ExprParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx:ExprParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:ExprParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#termOperator.
    def visitTermOperator(self, ctx:ExprParser.TermOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor.
    def visitFactor(self, ctx:ExprParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalExpression.
    def visitLogicalExpression(self, ctx:ExprParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalTerm.
    def visitLogicalTerm(self, ctx:ExprParser.LogicalTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalFactor.
    def visitLogicalFactor(self, ctx:ExprParser.LogicalFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparison.
    def visitComparison(self, ctx:ExprParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:ExprParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)



del ExprParser
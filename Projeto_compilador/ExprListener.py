# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#declarations.
    def enterDeclarations(self, ctx:ExprParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by ExprParser#declarations.
    def exitDeclarations(self, ctx:ExprParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:ExprParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:ExprParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#command.
    def enterCommand(self, ctx:ExprParser.CommandContext):
        pass

    # Exit a parse tree produced by ExprParser#command.
    def exitCommand(self, ctx:ExprParser.CommandContext):
        pass


    # Enter a parse tree produced by ExprParser#inputCommand.
    def enterInputCommand(self, ctx:ExprParser.InputCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#inputCommand.
    def exitInputCommand(self, ctx:ExprParser.InputCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#outputCommand.
    def enterOutputCommand(self, ctx:ExprParser.OutputCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#outputCommand.
    def exitOutputCommand(self, ctx:ExprParser.OutputCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#ifCommand.
    def enterIfCommand(self, ctx:ExprParser.IfCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#ifCommand.
    def exitIfCommand(self, ctx:ExprParser.IfCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#whileCommand.
    def enterWhileCommand(self, ctx:ExprParser.WhileCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#whileCommand.
    def exitWhileCommand(self, ctx:ExprParser.WhileCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#stringExpr.
    def enterStringExpr(self, ctx:ExprParser.StringExprContext):
        pass

    # Exit a parse tree produced by ExprParser#stringExpr.
    def exitStringExpr(self, ctx:ExprParser.StringExprContext):
        pass


    # Enter a parse tree produced by ExprParser#logicExpr.
    def enterLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass

    # Exit a parse tree produced by ExprParser#logicExpr.
    def exitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass


    # Enter a parse tree produced by ExprParser#numberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#numberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExprParser#arithExpr.
    def enterArithExpr(self, ctx:ExprParser.ArithExprContext):
        pass

    # Exit a parse tree produced by ExprParser#arithExpr.
    def exitArithExpr(self, ctx:ExprParser.ArithExprContext):
        pass


    # Enter a parse tree produced by ExprParser#parenExpr.
    def enterParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parenExpr.
    def exitParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ExprParser#idExpr.
    def enterIdExpr(self, ctx:ExprParser.IdExprContext):
        pass

    # Exit a parse tree produced by ExprParser#idExpr.
    def exitIdExpr(self, ctx:ExprParser.IdExprContext):
        pass


    # Enter a parse tree produced by ExprParser#concatExpr.
    def enterConcatExpr(self, ctx:ExprParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by ExprParser#concatExpr.
    def exitConcatExpr(self, ctx:ExprParser.ConcatExprContext):
        pass


    # Enter a parse tree produced by ExprParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:ExprParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:ExprParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:ExprParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:ExprParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#termOperator.
    def enterTermOperator(self, ctx:ExprParser.TermOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#termOperator.
    def exitTermOperator(self, ctx:ExprParser.TermOperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalExpression.
    def enterLogicalExpression(self, ctx:ExprParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalExpression.
    def exitLogicalExpression(self, ctx:ExprParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalTerm.
    def enterLogicalTerm(self, ctx:ExprParser.LogicalTermContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalTerm.
    def exitLogicalTerm(self, ctx:ExprParser.LogicalTermContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalFactor.
    def enterLogicalFactor(self, ctx:ExprParser.LogicalFactorContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalFactor.
    def exitLogicalFactor(self, ctx:ExprParser.LogicalFactorContext):
        pass


    # Enter a parse tree produced by ExprParser#comparison.
    def enterComparison(self, ctx:ExprParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ExprParser#comparison.
    def exitComparison(self, ctx:ExprParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ExprParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:ExprParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:ExprParser.ComparisonOperatorContext):
        pass



del ExprParser
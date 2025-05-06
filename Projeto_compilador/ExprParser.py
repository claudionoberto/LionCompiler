# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,1,5,1,53,8,1,10,1,
        12,1,56,9,1,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,3,5,75,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,100,
        8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,121,8,12,1,12,1,12,1,12,
        5,12,126,8,12,10,12,12,12,129,9,12,1,13,1,13,1,13,1,13,5,13,135,
        8,13,10,13,12,13,138,9,13,1,14,1,14,1,14,1,14,5,14,144,8,14,10,14,
        12,14,147,9,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,159,8,17,1,18,1,18,1,18,5,18,164,8,18,10,18,12,18,167,9,18,
        1,19,1,19,1,19,5,19,172,8,19,10,19,12,19,175,9,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,184,8,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,0,1,24,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,0,4,1,0,5,6,1,0,20,21,1,0,22,23,1,0,14,19,189,0,46,
        1,0,0,0,2,54,1,0,0,0,4,59,1,0,0,0,6,61,1,0,0,0,8,67,1,0,0,0,10,74,
        1,0,0,0,12,76,1,0,0,0,14,82,1,0,0,0,16,88,1,0,0,0,18,93,1,0,0,0,
        20,101,1,0,0,0,22,106,1,0,0,0,24,120,1,0,0,0,26,130,1,0,0,0,28,139,
        1,0,0,0,30,148,1,0,0,0,32,150,1,0,0,0,34,158,1,0,0,0,36,160,1,0,
        0,0,38,168,1,0,0,0,40,183,1,0,0,0,42,185,1,0,0,0,44,189,1,0,0,0,
        46,47,5,1,0,0,47,48,3,2,1,0,48,49,5,2,0,0,49,50,5,0,0,1,50,1,1,0,
        0,0,51,53,3,4,2,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,3,1,0,0,0,56,54,1,0,0,0,57,60,3,6,3,0,58,60,3,10,5,0,
        59,57,1,0,0,0,59,58,1,0,0,0,60,5,1,0,0,0,61,62,5,3,0,0,62,63,5,33,
        0,0,63,64,5,4,0,0,64,65,3,8,4,0,65,66,5,32,0,0,66,7,1,0,0,0,67,68,
        7,0,0,0,68,9,1,0,0,0,69,75,3,12,6,0,70,75,3,14,7,0,71,75,3,18,9,
        0,72,75,3,20,10,0,73,75,3,16,8,0,74,69,1,0,0,0,74,70,1,0,0,0,74,
        71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,11,1,0,0,0,76,77,5,7,0,
        0,77,78,5,28,0,0,78,79,5,33,0,0,79,80,5,29,0,0,80,81,5,32,0,0,81,
        13,1,0,0,0,82,83,5,8,0,0,83,84,5,28,0,0,84,85,3,24,12,0,85,86,5,
        29,0,0,86,87,5,32,0,0,87,15,1,0,0,0,88,89,5,33,0,0,89,90,5,27,0,
        0,90,91,3,24,12,0,91,92,5,32,0,0,92,17,1,0,0,0,93,94,5,9,0,0,94,
        95,3,24,12,0,95,96,5,10,0,0,96,99,3,22,11,0,97,98,5,11,0,0,98,100,
        3,22,11,0,99,97,1,0,0,0,99,100,1,0,0,0,100,19,1,0,0,0,101,102,5,
        12,0,0,102,103,3,24,12,0,103,104,5,13,0,0,104,105,3,22,11,0,105,
        21,1,0,0,0,106,107,5,30,0,0,107,108,3,2,1,0,108,109,5,31,0,0,109,
        23,1,0,0,0,110,111,6,12,-1,0,111,121,3,36,18,0,112,121,3,26,13,0,
        113,121,5,35,0,0,114,121,5,33,0,0,115,121,5,34,0,0,116,117,5,28,
        0,0,117,118,3,24,12,0,118,119,5,29,0,0,119,121,1,0,0,0,120,110,1,
        0,0,0,120,112,1,0,0,0,120,113,1,0,0,0,120,114,1,0,0,0,120,115,1,
        0,0,0,120,116,1,0,0,0,121,127,1,0,0,0,122,123,10,7,0,0,123,124,5,
        20,0,0,124,126,3,24,12,8,125,122,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,25,1,0,0,0,129,127,1,0,0,0,130,136,3,
        28,14,0,131,132,3,30,15,0,132,133,3,28,14,0,133,135,1,0,0,0,134,
        131,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,
        27,1,0,0,0,138,136,1,0,0,0,139,145,3,34,17,0,140,141,3,32,16,0,141,
        142,3,34,17,0,142,144,1,0,0,0,143,140,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,29,1,0,0,0,147,145,1,0,0,0,148,149,
        7,1,0,0,149,31,1,0,0,0,150,151,7,2,0,0,151,33,1,0,0,0,152,153,5,
        28,0,0,153,154,3,26,13,0,154,155,5,29,0,0,155,159,1,0,0,0,156,159,
        5,34,0,0,157,159,5,33,0,0,158,152,1,0,0,0,158,156,1,0,0,0,158,157,
        1,0,0,0,159,35,1,0,0,0,160,165,3,38,19,0,161,162,5,25,0,0,162,164,
        3,38,19,0,163,161,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,37,1,0,0,0,167,165,1,0,0,0,168,173,3,40,20,0,169,170,
        5,24,0,0,170,172,3,40,20,0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,39,1,0,0,0,175,173,1,0,0,0,176,177,5,
        26,0,0,177,184,3,40,20,0,178,179,5,28,0,0,179,180,3,36,18,0,180,
        181,5,29,0,0,181,184,1,0,0,0,182,184,3,42,21,0,183,176,1,0,0,0,183,
        178,1,0,0,0,183,182,1,0,0,0,184,41,1,0,0,0,185,186,3,26,13,0,186,
        187,3,44,22,0,187,188,3,26,13,0,188,43,1,0,0,0,189,190,7,3,0,0,190,
        45,1,0,0,0,12,54,59,74,99,120,127,136,145,158,165,173,183
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@start'", "'@end'", "'roar'", "'as'", 
                     "'int'", "'text'", "'hunt'", "'roarout'", "'if'", "'then'", 
                     "'else'", "'while'", "'strike'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", 
                     "'&&'", "'||'", "'!'", "'='", "'('", "')'", "'{'", 
                     "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "START", "END", "ROAR", "AS", "INT", 
                      "TEXT", "HUNT", "ROAROUT", "IF", "THEN", "ELSE", "WHILE", 
                      "STRIKE", "EQUALS", "NOT_EQUALS", "LESS", "GREATER", 
                      "LESS_EQUALS", "GREATER_EQUALS", "PLUS", "MINUS", 
                      "MULT", "DIV", "AND", "OR", "NOT", "ASSIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", "ID", "NUMBER", 
                      "STRING", "WS", "COMMENT", "ErrorChar" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_declaration = 2
    RULE_variableDeclaration = 3
    RULE_type = 4
    RULE_command = 5
    RULE_inputCommand = 6
    RULE_outputCommand = 7
    RULE_assignment = 8
    RULE_ifCommand = 9
    RULE_whileCommand = 10
    RULE_block = 11
    RULE_expression = 12
    RULE_arithmeticExpression = 13
    RULE_term = 14
    RULE_arithmeticOperator = 15
    RULE_termOperator = 16
    RULE_factor = 17
    RULE_logicalExpression = 18
    RULE_logicalTerm = 19
    RULE_logicalFactor = 20
    RULE_comparison = 21
    RULE_comparisonOperator = 22

    ruleNames =  [ "program", "declarations", "declaration", "variableDeclaration", 
                   "type", "command", "inputCommand", "outputCommand", "assignment", 
                   "ifCommand", "whileCommand", "block", "expression", "arithmeticExpression", 
                   "term", "arithmeticOperator", "termOperator", "factor", 
                   "logicalExpression", "logicalTerm", "logicalFactor", 
                   "comparison", "comparisonOperator" ]

    EOF = Token.EOF
    START=1
    END=2
    ROAR=3
    AS=4
    INT=5
    TEXT=6
    HUNT=7
    ROAROUT=8
    IF=9
    THEN=10
    ELSE=11
    WHILE=12
    STRIKE=13
    EQUALS=14
    NOT_EQUALS=15
    LESS=16
    GREATER=17
    LESS_EQUALS=18
    GREATER_EQUALS=19
    PLUS=20
    MINUS=21
    MULT=22
    DIV=23
    AND=24
    OR=25
    NOT=26
    ASSIGN=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    SEMICOLON=32
    ID=33
    NUMBER=34
    STRING=35
    WS=36
    COMMENT=37
    ErrorChar=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        def notifyErrorListeners(self, offendingToken, msg, e):
            line = offendingToken.line
            column = offendingToken.column
            tokenText = offendingToken.text
            expected = msg.split("expecting")[-1] if "expecting" in msg else "outro token"
            raise Exception(f"ERRO SINTÁTICO na linha {line}, coluna {column}: encontrado '{tokenText}', esperado {expected}")



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(ExprParser.START, 0)

        def declarations(self):
            return self.getTypedRuleContext(ExprParser.DeclarationsContext,0)


        def END(self):
            return self.getToken(ExprParser.END, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExprParser.START)
            self.state = 47
            self.declarations()
            self.state = 48
            self.match(ExprParser.END)
            self.state = 49
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = ExprParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589939592) != 0):
                self.state = 51
                self.declaration()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(ExprParser.VariableDeclarationContext,0)


        def command(self):
            return self.getTypedRuleContext(ExprParser.CommandContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.variableDeclaration()
                pass
            elif token in [7, 8, 9, 12, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROAR(self):
            return self.getToken(ExprParser.ROAR, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def AS(self):
            return self.getToken(ExprParser.AS, 0)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = ExprParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ExprParser.ROAR)
            self.state = 62
            self.match(ExprParser.ID)
            self.state = 63
            self.match(ExprParser.AS)
            self.state = 64
            self.type_()
            self.state = 65
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def TEXT(self):
            return self.getToken(ExprParser.TEXT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputCommand(self):
            return self.getTypedRuleContext(ExprParser.InputCommandContext,0)


        def outputCommand(self):
            return self.getTypedRuleContext(ExprParser.OutputCommandContext,0)


        def ifCommand(self):
            return self.getTypedRuleContext(ExprParser.IfCommandContext,0)


        def whileCommand(self):
            return self.getTypedRuleContext(ExprParser.WhileCommandContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_command)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.inputCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.outputCommand()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.ifCommand()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.whileCommand()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HUNT(self):
            return self.getToken(ExprParser.HUNT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_inputCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputCommand" ):
                listener.enterInputCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputCommand" ):
                listener.exitInputCommand(self)




    def inputCommand(self):

        localctx = ExprParser.InputCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inputCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExprParser.HUNT)
            self.state = 77
            self.match(ExprParser.LPAREN)
            self.state = 78
            self.match(ExprParser.ID)
            self.state = 79
            self.match(ExprParser.RPAREN)
            self.state = 80
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROAROUT(self):
            return self.getToken(ExprParser.ROAROUT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_outputCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputCommand" ):
                listener.enterOutputCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputCommand" ):
                listener.exitOutputCommand(self)




    def outputCommand(self):

        localctx = ExprParser.OutputCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_outputCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ExprParser.ROAROUT)
            self.state = 83
            self.match(ExprParser.LPAREN)
            self.state = 84
            self.expression(0)
            self.state = 85
            self.match(ExprParser.RPAREN)
            self.state = 86
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ExprParser.ID)
            self.state = 89
            self.match(ExprParser.ASSIGN)
            self.state = 90
            self.expression(0)
            self.state = 91
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_ifCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCommand" ):
                listener.enterIfCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCommand" ):
                listener.exitIfCommand(self)




    def ifCommand(self):

        localctx = ExprParser.IfCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ExprParser.IF)
            self.state = 94
            self.expression(0)
            self.state = 95
            self.match(ExprParser.THEN)
            self.state = 96
            self.block()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 97
                self.match(ExprParser.ELSE)
                self.state = 98
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def STRIKE(self):
            return self.getToken(ExprParser.STRIKE, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_whileCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCommand" ):
                listener.enterWhileCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCommand" ):
                listener.exitWhileCommand(self)




    def whileCommand(self):

        localctx = ExprParser.WhileCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ExprParser.WHILE)
            self.state = 102
            self.expression(0)
            self.state = 103
            self.match(ExprParser.STRIKE)
            self.state = 104
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExprParser.LBRACE, 0)

        def declarations(self):
            return self.getTypedRuleContext(ExprParser.DeclarationsContext,0)


        def RBRACE(self):
            return self.getToken(ExprParser.RBRACE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ExprParser.LBRACE)
            self.state = 107
            self.declarations()
            self.state = 108
            self.match(ExprParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)


    class LogicExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalExpression(self):
            return self.getTypedRuleContext(ExprParser.LogicalExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class ArithExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmeticExpression(self):
            return self.getTypedRuleContext(ExprParser.ArithmeticExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpr" ):
                listener.enterArithExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpr" ):
                listener.exitArithExpr(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class ConcatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.LogicExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 111
                self.logicalExpression()
                pass

            elif la_ == 2:
                localctx = ExprParser.ArithExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.arithmeticExpression()
                pass

            elif la_ == 3:
                localctx = ExprParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(ExprParser.STRING)
                pass

            elif la_ == 4:
                localctx = ExprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(ExprParser.ID)
                pass

            elif la_ == 5:
                localctx = ExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(ExprParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = ExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(ExprParser.LPAREN)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.match(ExprParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ConcatExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 122
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 123
                    self.match(ExprParser.PLUS)
                    self.state = 124
                    self.expression(8) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TermContext)
            else:
                return self.getTypedRuleContext(ExprParser.TermContext,i)


        def arithmeticOperator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArithmeticOperatorContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArithmeticOperatorContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_arithmeticExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpression" ):
                listener.enterArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpression" ):
                listener.exitArithmeticExpression(self)




    def arithmeticExpression(self):

        localctx = ExprParser.ArithmeticExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arithmeticExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.term()
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.arithmeticOperator()
                    self.state = 132
                    self.term() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FactorContext)
            else:
                return self.getTypedRuleContext(ExprParser.FactorContext,i)


        def termOperator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TermOperatorContext)
            else:
                return self.getTypedRuleContext(ExprParser.TermOperatorContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.factor()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.termOperator()
                    self.state = 141
                    self.factor() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_arithmeticOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticOperator" ):
                listener.enterArithmeticOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticOperator" ):
                listener.exitArithmeticOperator(self)




    def arithmeticOperator(self):

        localctx = ExprParser.ArithmeticOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arithmeticOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_termOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermOperator" ):
                listener.enterTermOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermOperator" ):
                listener.exitTermOperator(self)




    def termOperator(self):

        localctx = ExprParser.TermOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_termOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def arithmeticExpression(self):
            return self.getTypedRuleContext(ExprParser.ArithmeticExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(ExprParser.LPAREN)
                self.state = 153
                self.arithmeticExpression()
                self.state = 154
                self.match(ExprParser.RPAREN)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(ExprParser.NUMBER)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LogicalTermContext)
            else:
                return self.getTypedRuleContext(ExprParser.LogicalTermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.OR)
            else:
                return self.getToken(ExprParser.OR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)




    def logicalExpression(self):

        localctx = ExprParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.logicalTerm()
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.match(ExprParser.OR)
                    self.state = 162
                    self.logicalTerm() 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LogicalFactorContext)
            else:
                return self.getTypedRuleContext(ExprParser.LogicalFactorContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.AND)
            else:
                return self.getToken(ExprParser.AND, i)

        def getRuleIndex(self):
            return ExprParser.RULE_logicalTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalTerm" ):
                listener.enterLogicalTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalTerm" ):
                listener.exitLogicalTerm(self)




    def logicalTerm(self):

        localctx = ExprParser.LogicalTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicalTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.logicalFactor()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 169
                    self.match(ExprParser.AND)
                    self.state = 170
                    self.logicalFactor() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def logicalFactor(self):
            return self.getTypedRuleContext(ExprParser.LogicalFactorContext,0)


        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(ExprParser.LogicalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def comparison(self):
            return self.getTypedRuleContext(ExprParser.ComparisonContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_logicalFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalFactor" ):
                listener.enterLogicalFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalFactor" ):
                listener.exitLogicalFactor(self)




    def logicalFactor(self):

        localctx = ExprParser.LogicalFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicalFactor)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ExprParser.NOT)
                self.state = 177
                self.logicalFactor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(ExprParser.LPAREN)
                self.state = 179
                self.logicalExpression()
                self.state = 180
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArithmeticExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArithmeticExpressionContext,i)


        def comparisonOperator(self):
            return self.getTypedRuleContext(ExprParser.ComparisonOperatorContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = ExprParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.arithmeticExpression()
            self.state = 186
            self.comparisonOperator()
            self.state = 187
            self.arithmeticExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ExprParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(ExprParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(ExprParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ExprParser.GREATER, 0)

        def LESS_EQUALS(self):
            return self.getToken(ExprParser.LESS_EQUALS, 0)

        def GREATER_EQUALS(self):
            return self.getToken(ExprParser.GREATER_EQUALS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = ExprParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         





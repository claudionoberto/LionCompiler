grammar Expr;

@parser::members {
    def notifyErrorListeners(self, offendingToken, msg, e):
        line = offendingToken.line
        column = offendingToken.column
        tokenText = offendingToken.text
        expected = msg.split("expecting")[-1] if "expecting" in msg else "outro token"
        raise Exception(f"ERRO SINTÁTICO na linha {line}, coluna {column}: encontrado '{tokenText}', esperado {expected}")
}

// Estrutura principal do programa
program: START declarations END EOF;

// Declarações múltiplas
declarations: declaration*;

declaration
    : variableDeclaration
    | command
    ;

// Declaração de variável
variableDeclaration: ROAR ID AS type SEMICOLON;

// Tipos suportados
type: INT | TEXT;

// Comandos
command
    : inputCommand
    | outputCommand
    | ifCommand
    | whileCommand
    | assignment
    ;

// Entrada de dados
inputCommand: HUNT LPAREN ID RPAREN SEMICOLON;

// Saída de dados
outputCommand: ROAROUT LPAREN expression RPAREN SEMICOLON;

// Atribuição
assignment: ID ASSIGN expression SEMICOLON;

// Estrutura condicional
ifCommand: IF expression THEN block (ELSE block)?;

// Estrutura de repetição
whileCommand: WHILE expression STRIKE block;

// Bloco de código
block: LBRACE declarations RBRACE;

// Expressões
expression
    : expression PLUS expression               #concatExpr
    | logicalExpression                        #logicExpr
    | arithmeticExpression                     #arithExpr
    | STRING                                   #stringExpr
    | ID                                       #idExpr
    | NUMBER                                   #numberExpr
    | LPAREN expression RPAREN                 #parenExpr
    ;

// Expressões aritméticas
arithmeticExpression
    : term (arithmeticOperator term)*
    ;

term
    : factor (termOperator factor)*
    ;

arithmeticOperator: PLUS | MINUS;
termOperator: MULT | DIV;

factor
    : LPAREN arithmeticExpression RPAREN
    | NUMBER
    | ID
    ;

// Expressões lógicas
logicalExpression
    : logicalTerm (OR logicalTerm)*
    ;

logicalTerm
    : logicalFactor (AND logicalFactor)*
    ;

logicalFactor
    : NOT logicalFactor
    | LPAREN logicalExpression RPAREN
    | comparison
    ;

comparison
    : arithmeticExpression comparisonOperator arithmeticExpression
    ;

comparisonOperator
    : EQUALS
    | NOT_EQUALS
    | LESS
    | GREATER
    | LESS_EQUALS
    | GREATER_EQUALS
    ;

// Palavras-chave
START: '@start';
END: '@end';
ROAR: 'roar';
AS: 'as';
INT: 'int';
TEXT: 'text';
HUNT: 'hunt';
ROAROUT: 'roarout';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
STRIKE: 'strike';

// Operadores
EQUALS: '==';
NOT_EQUALS: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUALS: '<=';
GREATER_EQUALS: '>=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';

// Delimitadores
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';

// Literais
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"';

// Espaços e comentários
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;

// Erro léxico genérico
ErrorChar: . ;
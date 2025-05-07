# Lion

Lion é uma linguagem de programação educacional desenvolvida para a disciplina de Compiladores. O projeto implementa o analisador léxico e sintático utilizando ANTLR4 com suporte à execução em Python.

## Características da Linguagem

### Tipos de Dados
- `int` : Números inteiros
- `text` : Cadeias de caracteres entre aspas duplas

### Palavras-chave
- `@start` e `@end` : Delimitam o início e fim do programa
- `roar` : Declaração de variável
- `as` : Usado na declaração de tipo
- `hunt` : Entrada de dados
- `roarout` : Saída de dados
- `if`, `then`, `else` : Estrutura condicional
- `while`, `strike` : Estrutura de repetição

### Operadores
#### Aritméticos
- `+`, `-`, `*`, `/`

#### Relacionais
- `==`, `!=`, `<`, `>`, `<=`, `>=`

#### Lógicos
- `&&`, `||`, `!`

### Estrutura de Controle

#### Condicional
```text
if <expressao> then {
    // bloco verdadeiro
} else {
    // bloco falso
}
```

#### Repetição
```text
while <expressao> strike {
    // bloco de repetição
}
```

### Entrada e Saída
```text
hunt(variavel);       // Entrada
roarout(expressao);   // Saída
```

### Declaração de Variáveis
```text
roar idade as int;
roar nome as text;
```

## Exemplo de Programa

```text
@start
roar idade as int;
roar nome as text;

roarout("Digite seu nome:");
hunt(nome);
roarout("Digite sua idade:");
hunt(idade);

if idade >= 18 then {
    roarout("Maior de idade.");
} else {
    roarout("Menor de idade.");
}
@end
```

## Como Usar

### Requisitos
- Python 3.x
- ANTLR 4.13.2
- Java (para gerar analisadores)
- `antlr4-python3-runtime` (instalável via pip)

### Gerar Analisadores com ANTLR
```bash
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 Expr.g4
```

### Executar Analisadores
Para executar o Analisador Léxico:
```bash
python AnalisadorLexico.py <arquivo_entrada> <arquivo_saida> [arquivo_log]
```

Para executar o Analisador Sintático:
```bash
python AnalisadorSintatico.py <arquivo_entrada> <arquivo_saida_sem_extensao>
```
Gerar o arquivo .png através do .dot:
```bash
dot -Tpng <arquivo_entrada>.dot -o <arquivo_saida>.png  
```

### Tratamento de Erros

#### Erros Léxicos
```text
ERRO LÉXICO [Linha 5, Coluna 12]: Símbolo '#' inválido .
```

#### Erros Sintáticos
```text
ERRO SINTÁTICO [Linha 8, Coluna 3]: Esperado ';', encontrado '}' .
```

## Estrutura de Pastas
```
Lion/
├── Expr.interp              # Arquivos gerados pelo ANTLR
├── Expr.tokens             # Arquivos gerados pelo ANTLR
├── ExprLexer.interp              # Arquivos gerados pelo ANTLR
├── ExprLexer.interp              # Arquivos gerados pelo ANTLR
├── ExprLexer.py             # Arquivos gerados pelo ANTLR
├── ExprLexer.tokens              # Arquivos gerados pelo ANTLR
├── ExprListener.py              # Arquivos gerados pelo ANTLR
├── ExprParser.py              # Arquivos gerados pelo ANTLR
├── TrianguloPascal.lion           # Exemplos de programas em Lion (.lion)
├── ClassTriangulos.lion           # Exemplos de programas em Lion (.lion)
├── Expr.g4              # Arquivo de gramática
├── AnalisadorLexico.py              # Código principal de execução
├── AnalisadorSintatico.py              # Código principal de execução
└── README.md            # Este documento
```

## Autores

- Claudio Noberto França Junior
- Khawan Fellipe Magalhaes da Silva

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
- ANTLR 4.13.1
- Java (para gerar analisadores)
- `antlr4-python3-runtime` (instalável via pip)

### Gerar Analisadores com ANTLR
```bash
antlr4 -Dlanguage=Python3 -visitor -o parser Expr.g4
```

### Executar Analisador
Implemente um script Python como `main.py` para executar o parser com a gramática gerada.

### Tratamento de Erros

#### Erros Léxicos
```text
line X:Y token recognition error at: 'Z'
```

#### Erros Sintáticos
```text
ERRO SINTÁTICO na linha X, coluna Y: encontrado 'Z', esperado '...'
```

## Estrutura de Pastas
```
Lion/
├── parser/              # Arquivos gerados pelo ANTLR
├── examples/            # Exemplos de programas em Lion (.lion)
├── Expr.g4              # Arquivo de gramática
├── main.py              # Código principal de execução
└── README.md            # Este documento
```

## Autores

- Claudio Noberto França Junior
- Khawan Fellipe Magalhaes da Silva

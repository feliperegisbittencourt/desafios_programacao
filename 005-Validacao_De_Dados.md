# Validação de Dados

## Descrição
Escreva um programa que verifique em um arquivo de dados se todos os parâmetros requeridos têm valor definido.

## Formato de entrada

Na primeira linha haverá uma lista separada por vírgula com os parâmetros obrigatórios.

Nas linhas seguintes haverá os valores dos parâmetros sendo um por linha no formato `chave = valor`. Espaços em branco devem ser ignorados.

Exemplo 1:

```
peso,altura
altura = 1,71
peso = 80
idade = 35
```

Exemplo 2:
```
ip,dominio,porta,habilitado
ip = 192.168.1.100
dominio = meusite.intranet
```

## Formato de saída
Na saída deve ser exibido `ok` se todos os parâmetros obrigatórios forem encontrados ou `x <lista dos parametros faltantes>` se algum não for encontrado.

As saídas para os exemplos 1 e 2 seriam as seguintes:
- Ex 1: `ok`
- Ex 2: `x [porta,habilitado]`

#Em Python, não é necessário declarar o tipo de variável (linguagem dinamicamente tipada). O interpretador detecta automaticamente com base no valor atribuído. Exemplo:

x = 10 #inteiro
nome = 'mariana' #string

# Tipos de variáveis em Python:
# Inteiros (int)
idade = 21
ano = 2025
saldo = 0

#Usado para contagens, índices, quantidades.
#É ilimitado em tamanho (não existe “int32” ou “int64”)

# Flutuantes (float)
preco = 19.90
temperatura = -5.75
pi = 3.14
#Usado para números com casas decimais, medições, cálculos financeiros.

# Strings (str)
nome = "Mariana"
mensagem = 'dale boy'
#Usado para textos, nomes, frases. Pode ser definido com aspas simples ou duplas.
#pode conter letras, números e símbolos.
#strings são imutáveis (não podem ser alteradas após criadas).

# Booleanos (bool)
ativo = True
logado = False
#Usado para valores lógicos, verdadeiro (True) ou falso (False).
#utilizado em condições, verificações, controle de fluxo.
#são resultados de comparações, expressões lógicas:

10 > 5 # True
nome == "Mariana" # False

# Listas (list)
frutas = ["maçã", "banana", "pera"]
numeros = [1, 2, 3, 4, 5]
mistura = [1, "texto", True, 3.14]
#Usado para armazenar coleções de itens ordenados e mutáveis.
#Podem conter diferentes tipos de dados.
#permitem acesso por índice, fatiamento e iteração.

# Tuplas (tuple)
coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta")
#Usado para armazenar coleções de itens ordenados e imutáveis.
#mais leve e rápido que listas.
#Podem conter diferentes tipos de dados.

# Dicionários (dict)
pessoa = {
    "nome": "Renan",
    "idade": 21,
    "cidade": "Olinda"
}
#Usado para armazenar pares chave-valor.
#muito útil para representar dados estruturados.

# Conjuntos (set)
numeros = {1, 2, 3, 4, 5}
print(numeros)
#Usado para armazenar coleções de itens únicos e não ordenados.
#suportam operações matemáticas como união, interseção e diferença.

#(nulo) NoneType
resposta = None
#Usado para representar a ausência de valor ou um valor nulo.
#muito usado como valor padrão ou inicial

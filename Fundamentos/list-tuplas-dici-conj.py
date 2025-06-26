#Listas (list)
#são coleções mútaveis e ordenadas

frutas = ["maçã", "banana", "laranja"]

#características
#permitem altear os dados
#mantêm a ordem de inserção
#aceitam tipos variados (string, números, litas...)

#principais operações:
frutas.append("uva")                                    #adiciona ao final da lista
frutas.insert(1, "abacaxi")                             #insere na posição especificada
frutas.remove("banana")                                 #remove por valor
del frutas[0]                                           #remove por índice
print(frutas[1])                                        #acessa por índice
print(len(frutas))                                      #tamanho da lista

#Tuplas (tuple)
#são como listas, mas imutáveis (não podem ser alteradas após a criação)
cores = ("preto", "branco", "vermelho")
#mais eficientes em memória
#ideais para dados fixos
#suportam desempacotamento

b, w, r = cores  
#tentativas de alterar a tupla vão causar erro

#dicionários (dict)
aluno = {
    "nome": "Renan",
    "idade": 21,
    "cidade": "Recife",
    "stack de estudo": "Python"
}
#acessa elementos pela chave
#mutável
#ideal para dados estruturados
#principais operações:
print(aluno["nome"])                                        #acessa por chave
aluno["idade"] = 22                                         #altera valor
aluno["curso"] = "análise e desenvolvimento de sistemas"    #adiciona nova chave
del aluno["cidade"]                                         #remove chave
print(aluno.keys())                                         #exibe chaves
print(aluno.values())                                       #exibe valores

#conjuntos (set)
#armazenam valores únicos e não ordenados
numeros = {1, 2, 3, 4, 4, 2}
print(numeros)  
#elimina duplicatas 
#suporta operações de conjuntos matemmáticos
#principais operações:
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))  #união
print(a.intersection(b))  #interseção
print(a.difference(b))  #diferença

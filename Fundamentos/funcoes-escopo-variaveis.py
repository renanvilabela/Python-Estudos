#funções são blocos de código nomeados que executam uma tarefa específica. Elas evitam repetição de código e tornam o programa modular

#como declarar uma função
def saudacao():
    print("Dale boy")

#chamar a função
saudacao()

#Funções com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Renan")

#funções com retorno
def soma(a, b):
    return a + b
resultado = soma(19, 2)
print(resultado)

#Parâmetros com valor padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()
saudacao("Renan")

#Funções com número variável de argumentos
#args: empacota múltiplos argumentos posicionais em uma tupla
#kwargs: empacota múltiplos argumentos nomeados em um dicionário

def somar_tudo(*args):
    return sum(args)
print(somar_tudo(1, 3, 5, 7, 9))

def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
exibir_dados(nome="Renan", idade=21, cidade="Recife")

#Escopo de variáveis
#Variáveis locais: definidas dentro de uma função, só são acessíveis dentro dela

#escopo Local
#variavel definida dentro de uma função -- só existe dentro dela
def exemplo():
    x = 10
    print(x)
exemplo()

#escopo Global
#variável definida fora de qualquer função -- acessível por todo o script
x = 1914
def mostrar():
    print(x)
mostrar()

#modificando uma variável global (não recomendado)
x = 8
def alterar():
    global x  # Declara que x é a variável global
    x = 20
    print(f"Valor alterado dentro da função: {x}")
alterar()
print(x)
#em geral, evita usar global. prefira retornar valores e trabalhar com argumentos

#Funções aninhadas e escopo
def externa():
    mensagem = "Olá"

    def interna():
        nonlocal mensagem
        mensagem = "Oi"

    interna()
    print(mensagem)
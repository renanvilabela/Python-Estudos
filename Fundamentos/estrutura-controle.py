#As estruturas de controle servem para tomar decisões e repetir blocos de código com base em condições ou regras.
#Dividimos em dois grandes grupos:
#1 - Estruturas Condicionais – tomam decisões
#2 - Estruturas de Repetição (Laços) – repetem blocos de código


#estruturas condicionais
#if, elif e else - condicional simples e encadeada
idade = 17
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")
#com múltiplas condições
nota = 7.5

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#Estuturas de repetição
#Executa um bloco de código enquanto uma condição for verdadeira
#while - laço de repetição
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador
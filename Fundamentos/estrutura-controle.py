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

#for - laço de repetição
#Itera sobre uma sequência (lista, tupla, string, etc.)
nomes = ["Ana", "Mariana", "Renan"]

for nome in nomes:
    print(f"Olá, {nome}!")
#com range - gera uma sequência de números
for i in range(1, 6):  # De 1 a 5
    print(f"Número: {i}")
#range(início, fim) --> fim não incluído

#palavras-chave complementares:
#break: interrompe o laço antes do fim
#continue: pula para a próxima iteração do laço
#pass: não faz nada, serve como um espaço reservado (placeholder)
#Exemplo de break e continue
for numero in range(1, 10):
    if numero == 5:
        break  # Interrompe o laço
    print(f"Número: ", numero)

for numero in range(1, 6):
    if numero == 3:
        continue  # Pula o número 3
    print(f"Número: ", numero)

#Estrutura de controle match
#funciona como um switch/case em outras linguagens
comando = "iniciar"

match comando:
    case "iniciar":
        print("Iniciando o sistema...")
    case "parar":
        print("Parando o sistema...")
    case _:
        print("Comando desconhecido.")
#case_: funciona como o "default" em outras linguagens, capturando qualquer outro caso não especificado.
def boas_vindas(nome):
    print("Olá, " + nome + "! Seja bem-vindo(a) ao nosso programa.")
boas_vindas("Renan")

def soma_dois_numeros(a, b):
    return a + b
resultado = soma_dois_numeros(5, 7)
print("A soma é:", resultado)

def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
print(fatorial(5))

def calcular_desconto(preco, porcentagem=10):
    desconto = preco * (porcentagem / 100)
    preco_final = preco - desconto
    return preco_final
print(calcular_desconto(100))
print(calcular_desconto(200, 20))

def soma_total(*valores):
    total = 0
    for valor in valores:
        total += valor
    return total
print(soma_total(1, 2, 3, 4, 5))

def exibir_usuario(**dados):
    print("Dados do usuário:")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")
exibir_usuario(nome="Renan", idade=21, cidade="recife")

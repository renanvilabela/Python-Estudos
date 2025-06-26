def boas_vindas(nome):
    print("Olá, " + nome + "! Seja bem-vindo(a) ao nosso programa.")
boas_vindas("Renan")

def soma_dois_numeros(a, b):
    return a + b
resultado = soma_dois_numeros(5, 7)
print("A soma é:", resultado)

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
fatorial



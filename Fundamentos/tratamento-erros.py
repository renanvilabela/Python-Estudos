# O que são Exceções?
# Em Python, uma exceção é um erro que ocorre durante a execução do programa. Quando ocorre, o Python interrompe o fluxo normal do programa, a menos que o erro seja tratado.

#exemplo de erro sem tratamento:
numero = int("abc")  # ValueError: invalid literal for int()

#Tratando erros com try, except
# try:
#     # código que pode gerar erro
# except TipoDeErro:
#     # código executado se o erro ocorrer

# exemplo:
try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou {numero}")
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")

#múltiplos excepts
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro de valor!")

#bloco else e finally
#else: executando se não ocorrer exceção
#finally: sempre executado, com ou sem erro

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro de valor.")
else:
    print("Número convertido com sucesso:", numero)
finally:
    print("Encerrando o programa.")

#Criando suas próprias exceções
#você pode definir erros personalizados com a palavra-chave raise
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print("Erro:", e)

# Erros mais comuns em Python:
# Erro	Significado
# SyntaxError	Erro de sintaxe
# NameError	Variável não definida
# TypeError	Tipo de dado incompatível
# ValueError	Valor incorreto
# IndexError	Índice fora do alcance da lista
# KeyError	Chave inexistente em dicionário
# ZeroDivisionError	Divisão por zero
# FileNotFoundError	Arquivo não encontrado

#Dica prática
#Sempre trate apenas os erros que você espera, evite capturar exceções genéricas demais como:
except:
    print("Deu erro!")
#prefira:
except FileNotFoundError:
    print("Arquivo não encontrado.")
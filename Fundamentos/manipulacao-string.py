#Definição e Criação de Strings
mensagem = "Olá, Mundo!"
#Strings em python são sequências imutáveis de caracteres. Você pode criar com:
#aspas simples: 'exemplo'
#aspas duplas: "exemplo"
#aspas triplas: '''exemplo''' ou """exemplo""" (permite múltiplas linhas)

#principais operações
#acessar caracteres
mensagem[0]  # 'O'
mensagem[-1]  # '!'

#fatiamento
mensagem[:5]  # 'Olá, '
mensagem[0:3]  # 'Olá'
mensagem[5:]  # ', Mundo!'

#Comprimento
len(mensagem)  # 13

#métodos úteis de strings
# .lower()  'converte para minúsculas'
# .upper()   'CONVERTE PARA MAIÚSCULAS'
# .capitalize()   'Converte a primeira letra para maiúscula'
# .title()   'Converte a primeira letra de cada palavra para maiúscula'
# .strip()   'Remove espaços no início e no final'
# .replace('Mundo', 'Python')   'substitui uma substring por outra'
# .split(', ')   ['Olá', 'Mundo!'] (divide a string em uma lista)
# .find('Mundo')  retorna índice da palavra(ou -1)
# .join(lista) junta elementos com separador

#exemplos

texto = "   Python é poderoso!    "
print(texto.strip())               # Remove espaços
print(texto.lower())               # python é poderoso!
print(texto.upper())               # PYTHON É PODEROSO!
print(texto.replace("poderoso", "incrível"))  # Substitui palavra
print("Python,Java,C++".split(","))           # ['Python', 'Java', 'C++']
print(" - ".join(["A", "B", "C"]))            # A - B - C

nome = "Renan"

print(nome.startswith("Re"))   # True
print(nome.endswith("n"))      # True
print(nome.isalpha())          # True (só letras)
print(nome.isnumeric())        # False
print(nome.isalnum())          # True (letras e números)

#interpolação e formatação de strings
nome = "Renan"
mensagem = "Olá, " + nome + "!"

#f-strings (Python 3.6+)
idade = 21
print(f"Olá, {nome}! Você tem {idade} anos.")  

#Método .format()
print("Olá, {}! Você tem {} anos.".format(nome, idade))

#Strings multilinha
texto = """
isso é uma string
com múltiplas linhas.
"""

#caracteres especiais
# \n	Nova linha
# \t	Tabulação (tab)
# \\	Barra invertida
# \'	Aspas simples
# \"	Aspas duplas
#exemplo:
print("Linha 1\nLinha2")

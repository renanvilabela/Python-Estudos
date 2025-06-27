# O que são Módulos?
# Um módulo em Python é simplesmente um arquivo .py que contém definições de funções, classes, variáveis, ou até códigos executáveis.

# Eles permitem que você divida seu código em múltiplos arquivos menores e mais organizados.

#Exemplo de criação e uso de módulo
#criando um módulo chamado meu_modulo.py
meu_modulo
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)"

import meu_modulo

mensagem = meu_modulo.saudacao("Renan")
print(mensagem)

#forams de importar módulos
import math  # Importa todo o módulo
from math import sqrt  # Importa apenas a função sqrt
from math import * # Importa tudo do módulo (não recomendado, pode causar conflitos de nomes)
import math as m # Importa com um alias

# O que são Pacotes?
# Um pacote é uma pasta que contém vários módulos e um arquivo especial chamado __init__.py.

# Isso facilita a organização de projetos grandes e cria uma hierarquia de importações.

# meu_pacote/
# ├── __init__.py
# ├── modulo1.py
# └── modulo2.py

#exemplo de uso de pacote
from meu_pacote.modulo1 import minha_funcao

# Módulos e pacotes da biblioteca padrão (built-in)
# Python já vem com muitos módulos úteis, como:

# Módulo	Função
# math	Funções matemáticas
# random	Gerar números aleatórios
# datetime	Manipular datas e horários
# os	Interagir com o sistema operacional
# sys	Parâmetros e funções do interpretador Python
# json	Ler e escrever dados em formato JSON
# re	Expressões regulares

#exemplo com math
import math
print(math.sqrt(16))                # Raiz quadrada
print(math.pi)                      # valor de pi
print(math.ceil(2.3))               #arredondamento para cima
print(math.floor(2.8))              #arredondamento para baixo

# Boas práticas com módulos e pacotes
# Nomeie seus arquivos de forma clara (ex: util.py, calculadora.py)

# Evite usar from módulo import *

# Use aliases com as quando os nomes forem longos ou conflitantes

# Agrupe funcionalidades relacionadas em um pacote

#verificando módulos disponíveis
help("modules")
#isso mostrará todos os módulos instalados no seu ambiente Python.
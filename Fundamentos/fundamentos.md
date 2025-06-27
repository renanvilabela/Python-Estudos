# 📘 Nível 1 – Fundamentos da Linguagem Python

Este diretório reúne todo o aprendizado inicial sobre a linguagem Python. Os exemplos e explicações aqui registrados cobrem os principais fundamentos para quem está construindo uma base sólida em programação.

---

## 🧠 Fundamentos com Exemplos

### ✅ Tipos de Variáveis

```python
# Inteiro
idade = 25

# Float
altura = 1.75

# String
nome = "Renan"

# Booleano
ativo = True

# Lista
frutas = ["maçã", "banana", "laranja"]

# Tupla
coordenadas = (10.0, 20.5)

# Dicionário
usuario = {"nome": "Renan", "idade": 21, "cidade": "Recife"}

# Conjunto (set)
numeros_unicos = {1, 2, 3, 3, 4}
```

### ✅ Estruturas de Controle 

```python
# Condicional
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Laço for
for fruta in frutas:
    print("Fruta:", fruta)

# Laço while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Uso do break e continue
for i in range(5):
    if i == 3:
        break  # Interrompe o laço
    if i == 1:
        continue  # Pula a iteração
    print(i)
```

### ✅Funções e Escopo de Variáveis

```python
# Função simples
def boas_vindas(nome):
    print(f"Olá, {nome}!")

boas_vindas("Renan")

# Função com retorno
def soma(a, b):
    return a + b

print("Resultado:", soma(3, 5))

# Função com parâmetros padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()
saudacao("Ana")

# *args e **kwargs
def soma_total(*numeros):
    return sum(numeros)

print(soma_total(1, 2, 3, 4))

def exibir_usuario(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

exibir_usuario(nome="Renan", idade=21, cidade="Recife")

# Escopo
x = 10

def mostrar_valor():
    x = 5  # variável local
    print("Dentro da função:", x)

mostrar_valor()
print("Fora da função:", x)
```

### ✅Manipulação de Strings

```python
texto = "  Olá, Python!  "

# Métodos úteis
print(texto.strip())        # Remove espaços nas pontas
print(texto.upper())        # Caixa alta
print(texto.lower())        # Caixa baixa
print(texto.replace("Python", "Mundo"))
print("Python" in texto)    # Verificação

# Fatiamento
print(texto[4:10])          # Pega caracteres entre as posições

# Interpolação
nome = "Renan"
print(f"Seja bem-vindo, {nome}!")
```

### ✅Manipulação de Arquivos

```python
# Escrita
with open("arquivo.txt", "w") as f:
    f.write("Primeira linha\nSegunda linha")

# Leitura
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

# Adição
with open("arquivo.txt", "a") as f:
    f.write("\nTerceira linha adicionada")
```

### ✅Módulos e Pacotes

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")
else:
    print("Executado com sucesso.")
finally:
    print("Finalizando operação.")

# Criando erro personalizado
def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b
```

### ✅Tratamento de Erros

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")
else:
    print("Executado com sucesso.")
finally:
    print("Finalizando operação.")

# Criando erro personalizado
def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b
```


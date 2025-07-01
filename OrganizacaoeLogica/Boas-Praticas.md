# 🧼 Boas Práticas em Python

Este documento reúne boas práticas essenciais para escrever código Python limpo, legível e de fácil manutenção. Seguir essas diretrizes facilita o trabalho em equipe e melhora a qualidade dos projetos.

---

## 📍 1. Siga a PEP 8

A [PEP 8](https://peps.python.org/pep-0008/) é o guia oficial de estilo para Python. Alguns pontos principais:

- Use **4 espaços** para indentação (não use TAB).
- Separe as funções com **duas linhas em branco**.
- Linhas com no máximo **79 caracteres**.
- Variáveis com nomes claros: `nome_usuario` em vez de `n`.
- Use `snake_case` para variáveis e funções, `PascalCase` para classes.

---

## 🔠 2. Nomeação clara e significativa

Evite abreviações confusas ou genéricas:

```python
# Ruim
def calc(d):
    return d * 2

# Melhor
def calcular_dobro(valor):
    return valor * 2
```
## 📦 3. Organize o código em funções e módulos

Evite deixar tudo no mesmo arquivo. Separe o código por responsabilidade:

projeto/
│
├── main.py
├── funcoes/
│   └── matematica.py
├── dados/
│   └── usuarios.py

## 📄 4. Documente com docstrings

```python
def calcular_media(lista):
    """
    Calcula a média de uma lista de números.

    Parâmetros:
    lista (list): Lista de números.

    Retorno:
    float: Média calculada.
    """
    return sum(lista) / len(lista)
```

## 🔐 5. Proteja o escopo principal

```python
def main():
    print("Programa iniciado.")

if __name__ == "__main__":
    main()
```

## 🧪 6. Faça tratamento de exceções
Evite que o programa quebre sem controle:

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
```

## ♻️ 7. Evite repetição de código
Prefira funções reutilizáveis:

```python
def exibir_mensagem(texto):
    print(f">>> {texto}")

exibir_mensagem("Bem-vindo")
exibir_mensagem("Erro ao carregar dados")
```

## 🧯 8. Use ambientes virtuais
Para isolar dependências do projeto:

```python
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
``` 

## 📋 9. Registre dependências

```python
pip freeze > requirements.txt
```

## 🧼 10. Formate e valide seu código
Ferramentas úteis:

- black – formata o código automaticamente.

- flake8 – verifica estilo conforme PEP 8.

- isort – organiza imports.

## ✅ Resumo
✔️ Código limpo
✔️ Bem nomeado
✔️ Separado em módulos
✔️ Documentado
✔️ Seguro com try/except
✔️ Pronto para crescer
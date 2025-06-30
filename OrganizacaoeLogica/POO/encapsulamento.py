# O que é?
# Encapsulamento é o princípio de ocultar os detalhes internos de funcionamento de um objeto e permitir que o acesso a esses dados seja feito apenas por meio de métodos (funções) definidos na classe.

# Objetivos principais:
# Proteger os dados (evitar acessos e alterações indevidas);

# Controlar o uso e comportamento dos atributos;

# Manter a integridade do estado do objeto.

# Python não possui modificadores de acesso como outras linguagens (ex: private, protected, public), mas sim convenções:

# | Convenção | Acesso                             | Exemplo     |
# | --------- | ---------------------------------- | ----------- |
# | Público   | Acessível de qualquer lugar        | `self.nome` |
# | Protegido | Acessível na classe e subclasses   | `_nome`     |
# | Privado   | Acessível apenas na própria classe | `__nome`    |

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular     # Atributo privado
        self.__saldo = saldo         # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Titular: {self.__titular} | Saldo: R$ {self.__saldo:.2f}")

# Tentativa de acesso externo direto:
conta = ContaBancaria("Renan", 1000)
print(conta.__saldo)  # Erro! Atributo privado.

# Aceso Correto:
conta.exibir_saldo()

# Getter e Setter (acessores e modificadores)
# Esses métodos controlam o acesso e modificação de atributos privados.

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço inválido!")

produto = Produto("Teclado", 150)
print(produto.get_preco())  # 150
produto.set_preco(180)
print(produto.get_preco())  # 180

# Encapsulamento não é só sobre “privado”:
# Ele engloba o princípio de organização e responsabilidade: deixar claro o que deve ser exposto e o que deve ser mantido interno.

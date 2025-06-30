# Conceito Envolvido: Encapsulamento
# Encapsulamento é o princípio de esconder os detalhes internos de funcionamento de uma classe, permitindo o acesso e a modificação dos atributos apenas por meio de métodos controlados (getters e setters).

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar (self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:.2f} relizado com sucesso.")
            else:
                print("saldo insuficiente.")
        else:
            print("Valor de saque inválido")

    def exibir_saldo(self):
        print(f"Titular: {self.__titular}, Saldo atual: R$ {self.__saldo:.2f}")

conta = ContaBancaria("Renan", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)  # Tentativa de saque maior que o saldo
conta.depositar(-200)  # Depósito inválido
conta.exibir_saldo()

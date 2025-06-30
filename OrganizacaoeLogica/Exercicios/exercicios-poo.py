class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = self.__preco * (percentual / 100)
            self.__preco -= desconto
        else:
            print("Percentual de desconto inválido.")
    def exibir_dados(self):
        print(f"Produto: {self.__nome}, Preço: R$ {self.__preco:.2f}")
    

p = Produto("Notebook", 2500.00)
p.exibir_dados()  # Saída: Produto: Notebook, Preço: R$ 2500.00
p.aplicar_desconto(10)
p.exibir_dados()  # Saída: Produto: Notebook, Preço: R$ 2250.00

class Aluno:
    def __init__(self, nome, notas):
        self.__nome = nome
        self.__notas = notas

    def calcular_media(self):
        if self.__notas:
            return sum(self.__notas) /len(self.__notas)
        return 0
    
    def exibir_status(self):
        media = self.calcular_media()
        print(f"Aluno: {self.__nome}")
        print(f"Notas: {self.__notas}")
        print(f"Média: {media: .2f}")
        if media >= 6:
            print("Status: Aprovado")
        else:
            print("Status: Reprovado")
a1 = Aluno("Renan", [7.5, 8.0, 6.5])
a1.exibir_status()  # Exibe os dados do aluno e seu status

print()

a2 = Aluno("Edivaldo", [5.0, 4.5, 6.0])
a2.exibir_status()  # Exibe os dados do aluno e seu status

class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = 0 # velocidade inicial é 0
    
    def acelerar(self, valor):
        if valor > 0:
            selfvelocidade += valor
        else:
            print("Valor de aceleração inválido.")
    
    def frear(self, valor):
        if valor > 0:
            self.__velocidade -= valor
            if self.__velocidadde < 0:
                self.__velocidade = 0
            
        else:
            print("Valor de frenagem inválido.")
    
    def exibir_status(self):
        print(f"Carro: {self.__marca} {self.__modelo} ({self.__ano}, Velocidade: {self.__velocidade} km/h)")

c1 = Carro("Toyota", "Corolla", 2020)
c1.exibir_status()  # Exibe os dados do carro

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    def ver_saldo(self):
        print(f"Saldo atual de {self.__titular}: R$ {self.__saldo:.2f}")
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

c2 = ContaBancaria("João", 1000.00)
c2.ver_saldo()  # Exibe o saldo atual
c2.depositar(500.00)  # Deposita R$ 500,00
c2.ver_saldo()  # Exibe o saldo atualizado
c2.sacar(200.00)  # Saca R$ 200,00
c2.ver_saldo()  # Exibe o saldo atualizado após o saque
c2.sacar(1500.00)  # Tenta sacar um valor maior que o saldo
c2.ver_saldo()  # Exibe o saldo após tentativa de saque inválido

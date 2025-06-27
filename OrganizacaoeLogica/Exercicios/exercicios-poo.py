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
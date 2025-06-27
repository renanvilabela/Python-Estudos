# Programação Orientada a Objetos (POO) é um paradigma de programação baseado em "objetos", que representam entidades do mundo real com propriedades (atributos) e comportamentos (métodos).

#Principais conceitos de POO:
#Classe e Objeto

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
p1 = Pessoa("Renan", 21)
p1.apresentar()

# __init é o construtor da classe, chamado automaticamente na criação do objeto
# self é a referência ao próprio objeto da classe (como o this em outras linguagens)

# Atributos de Instância vs Atributos de Classe
class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome # Atributo de instância

p1 = Pessoa("Renan")
p2 = Pessoa("Edivaldo")

print(p1.nome) # Saída: Renan
print(p2.especie) # Saída: Humano

# Encapsulamento
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado
    
    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta = Conta(1000)
conta.depositar(500)
conta.ver_saldo()  # Saída: Saldo atual: R$ 1500.00
# Atributos iniciados com __ são tratados como privados (embora acessíveis com técnicas específicas).

#Herança
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print("O animal fez um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro latiu.")

dog = Cachorro("Maylon")
dog.falar() # Saída: O cachorro latiu.
# A herança permite reutilizar e especializar o comportamento de uma classe base.

# Polimorfismo
def fazer_animal_falar(animal):
    animal.falar()
class Gato(Animal):
    def falar(self):
        print("O gato miou.")

gato = Gato("Mimi")
fazer_animal_falar(dog)  # Saída: O cachorro latiu.
fazer_animal_falar(gato)  # Saída: O gato miou.
# O mesmo método (falar) se comporta de maneira diferente dependendo da classe do objeto.

#Composição
class Motor:
    def ligar(self):
        print("Motor ligado.")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        self.motor.ligar()

meu_carro = Carro()
meu_carro.ligar()  # Saída: Motor ligado.
# A composição é usada quando uma classe contém outra como parte de sua estrutura.
# O que é?
# Polimorfismo significa "muitas formas". Na prática da POO, refere-se à capacidade de diferentes classes usarem métodos com o mesmo nome, mas com comportamentos diferentes.

# Em Python, isso geralmente é feito por meio da sobrescrita de métodos (override).

#  Sobrescrita de Método (Override)
# Quando uma classe filha implementa um método com o mesmo nome de um método da classe pai, mas com um comportamento próprio.

class Animal:
    def emitir_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Uso polimórfico
animais = [Cachorro(), Gato(), Animal()]

for animal in animais:
    animal.emitir_som()  # Cada um executa sua própria versão

# Benefício:
# Permite que você use o mesmo nome de método para representar ações que se comportam diferentemente dependendo do tipo do objeto, facilitando a manutenção e extensibilidade do código.

class Pessoa:
    def apresentar(self):
        print("Sou uma pessoa.")

class Estudante(Pessoa):
    def apresentar(self):
        super().apresentar()  # Chama o método da classe pai
        print("E também sou um estudante.")

e = Estudante()
e.apresentar()

# | Conceito     | O que faz                                                             |
# | ------------ | --------------------------------------------------------------------- |
# | Herança      | Permite uma classe filha herdar de uma classe pai                     |
# | Polimorfismo | Permite que métodos com o mesmo nome tenham comportamentos diferentes |
# | Sobrescrita  | A classe filha substitui o método herdado                             |
# | `super()`    | Acessa métodos e construtores da classe pai                           |

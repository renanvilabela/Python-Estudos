# Conceito Envolvido: Polimorfismo
# Polimorfismo significa "muitas formas". Em programação orientada a objetos, refere-se à capacidade de diferentes classes responderem ao mesmo método de formas diferentes.

# Em Python, isso é feito definindo métodos com o mesmo nome em diferentes classes, mas com comportamentos diferentes.

class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro latiu")

class Gato(Animal):
    def falar(self):
        print("O gato miou")

def fazer_animais_falarem(animais):
    for animal in animais:
        animal.falar() #cada classe executa seu próprio método falar()


animais = [Cachorro(), Gato(), Cachorro()]
fazer_animais_falarem(animais)

# Explicação
# A função fazer_animais_falarem() não precisa saber que tipo de animal está lidando.

# Ela apenas chama falar(), e o comportamento correto é executado, dependendo da classe.

# Isso é polimorfismo em ação: métodos com mesmo nome, mas implementações diferentes.
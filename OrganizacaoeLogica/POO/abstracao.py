# O que é?
# A abstração é o princípio de esconder os detalhes complexos de implementação e mostrar apenas o necessário ao usuário.
# Ou seja: focamos no "o que" um objeto faz e não "como" ele faz.

# Objetivo principal:
# Criar interfaces genéricas e reutilizáveis para objetos.

# Facilitar a manutenção e o entendimento do sistema.

# Garantir um contrato de comportamento entre classes.

# Abstração com Classes Abstratas em Python
# Em Python, usamos o módulo abc (Abstract Base Classes) para criar classes abstratas.
# Essas classes não podem ser instanciadas diretamente e servem como modelo para outras.

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

# Acima, temos uma classe abstrata Forma com dois métodos abstratos. Qualquer classe que herde Forma deve implementar esses métodos.

# Subclasses concretas:
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

forma = Forma()  # Erro: TypeError

# Vantagens da abstração
# Facilita o trabalho em equipe (cada um implementa uma parte conforme o contrato).

# Melhora a organização do código.

# Permite maior reutilização e flexibilidade.

# Analogias simples:
# Controle remoto: você sabe o que o botão "liga" faz, mas não precisa saber como o sinal é enviado para a TV.

# Interface de um carro: o motorista interage com volante, pedais e painel, sem conhecer o funcionamento interno do motor.

# | Conceito            | Como usar em Python                                  |
# | ------------------- | ---------------------------------------------------- |
# | Classe abstrata     | `class MinhaClasse(ABC):`                            |
# | Método abstrato     | `@abstractmethod` acima do método                    |
# | Evitar instanciação | Não se pode instanciar classes com métodos abstratos |

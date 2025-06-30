# Conceito Envolvido: Abstração
# Abstração é o processo de ocultar detalhes de implementação e mostrar apenas os aspectos essenciais de um objeto.
# Em Python, usamos a biblioteca abc (Abstract Base Class) para criar classes e métodos abstratos.

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10
    
def exibir_bonus(funcionarios):
    for funcionario in funcionarios:
        print(f"{funcionario.nome} - Bônus: R$ {funcionario.calcular_bonus():.2f}")


f1 = Gerente("Ana", 8000)
f2 = Desenvolvedor("Carlos", 6000)
f3 = Desenvolvedor("Bruna", 7000)

lista_funcionarios = [f1, f2, f3]
exibir_bonus(lista_funcionarios)


# Explicação
# A classe Funcionario define a estrutura base de qualquer tipo de funcionário.

# O método calcular_bonus() é obrigatório em todas as subclasses (graças ao decorador @abstractmethod).

# Isso garante que cada tipo de funcionário tenha sua própria implementação do cálculo de bônus.
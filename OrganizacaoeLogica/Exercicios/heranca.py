# Herança permite que uma classe (filha) herde atributos e métodos de outra classe (pai).
# Exemplo: Uma classe Funcionario pode ser base, e Gerente e Vendedor podem herdar dela.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self. salario = salario
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")

class Gerente(Funcionario):                                 # heranca
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)                     # Chama o construtor da classe base
        self.departamento = departamento

    def exibir_dados(self):                                 # Sobrescrita de método
        super().exibir_dados()                              # Reutiliza parte da lógica de base
        print(f"departamento: {self.departamento}")

g1 = Gerente("Renan", 2100.00, "TI")
g1.exibir_dados()

    
# Imagine que você tenha uma classe Pessoa, e queira criar várias classes como Aluno, Professor ou Funcionario. Todas têm nome, idade, e podem se apresentar. Ao invés de repetir tudo, você herda de Pessoa.

# Classe base
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

# Classe filha que herda de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # Chama o construtor da classe base
        self.matricula = matricula
    
    def mostrar_matricula(self):
        print(f"Matrícula do aluno: {self.matricula}")

# Classe filha que herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def lecionar(self):
        print(f"Estou lecionando a disciplina de {self.disciplina}.")

# Uso
a = Aluno("Renan", 21, "A1234")
p = Professor("João", 40, "Matemática")

a.apresentar()           # Da classe base
a.mostrar_matricula()    # Específico de Aluno

p.apresentar()           # Da classe base
p.lecionar()             # Específico de Professor

# O que está acontecendo aqui?
# Aluno e Professor herdam Pessoa → automaticamente ganham acesso a apresentar() e aos atributos nome e idade.

# A função super().__init__() garante que o construtor da classe base seja executado corretamente.

# Curiosidades:
# Python suporta herança múltipla (uma classe pode herdar de várias classes), mas é bom usar com cuidado.

# Você pode sobrescrever métodos herdados (veremos isso no Polimorfismo).
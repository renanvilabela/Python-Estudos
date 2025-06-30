# Na composição, uma classe é composta por uma ou mais instâncias de outras classes.
# Exemplo real: uma Pessoa tem um Endereço. O endereço não faz sentido isolado se a pessoa não existir nesse contexto.

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco.rua}, {self.endereco.cidade}")

meu_endreco = Endereco("Nordibe", "Olinda")

Pessoa1 = Pessoa("Renan", meu_endreco)

Pessoa1.exibir_dados()
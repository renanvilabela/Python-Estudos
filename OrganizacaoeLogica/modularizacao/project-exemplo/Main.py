from calculadora.operacoes import somar, subtrair
from calculadora.formatador import formatar_resultado

resultado1 = somar(10, 5)
print(formatar_resultado(resultado1))

resultado2 = subtrair(20, 3)
print(formatar_resultado(resultado2))

# Manipular arquivos significa ler ou escrever dados diretamente no sistema de arquivos (disco rígido, SSD etc), em vez de manter tudo apenas na memória (variáveis, listas, dicionários...).

# Isso permite:

# Armazenar dados permanentemente

# Carregar informações salvas anteriormente

# Gerar relatórios, logs ou exportações

#Abrindo arquivos com open()

# open(nome_arquivo, modo, encoding='utf-8')
#nome_arquivo: caminho do arquivo
#modo: o que você quer fazer com o arquivo
#encoding: define a codificação de caracteres (padrão é 'utf-8')

#modos de abertura:
# 'r'	Leitura (read)
# 'w'	Escrita (write) – sobrescreve
# 'a'	Adição (append) – acrescenta
# 'x'	Criação (erro se já existir)
# 'b'	Modo binário
# 't'	Modo texto (padrão)
# 'r+'	Leitura e escrita

#lendo arquivos
#exemplo 1: Lendo todo o conteúdo
arquivo = open("exemplo.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
# Importante: Sempre feche o arquivo após usá-lo com .close() ou use o with (mais recomendado).

#exemplo 2: lendo linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  

#Escrevendo em Arquivos
#Exemplo 1: sobrescrever conteúdo
with open("novo_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
#Se o arquivo já existir, o conteúdo anterior será apagado.

#Exemplo 2: adicionar conteúdo
with open("novo_arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Mais uma linha!\n")

#Lendo e Escrevendo ao mesmo tempo
with open("exemplo.txt", "r+", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.seek(0)
    arquivo.write("Nova linha\n" + conteudo)

# Algumas funções úteis
# Função	O que faz
# .read()	Lê tudo como uma string
# .readline()	Lê uma linha por vez
# .readlines()	Retorna uma lista de linhas
# .write("texto")	Escreve string no arquivo
# .writelines(lista)	Escreve várias linhas (de uma lista)
# .seek(0)	Move o cursor para o início do arquivo
# .close()	Fecha o arquivo (necessário se não usar with)

#Dica Extra: verificar se o arquivo existe
import os

if os.path.exists("dados.txt"):
    print("Arquivo existe!")
else:
    print("Arquivo não encontrado.")
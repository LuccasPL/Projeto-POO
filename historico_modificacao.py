# buscar e mostrar o histórico de modificações de um arquivo
import os
import time
# criar um arquivo
def criar_arquivo(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, "a") as arq:
            arq.write("Arquivo criado")
    else:
        print("O arquivo já existe")

criar_arquivo("arquivo.txt")

def historico_modificacao(arquivo):
    if os.path.exists(arquivo):
        print("O arquivo existe")
        print("O arquivo foi modificado pela última vez em: ", time.ctime(os.path.getmtime(arquivo)))
    else:
        print("O arquivo não existe")

historico_modificacao("arquivo.txt")

# inserir dados no arquivo
def inserir_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "a") as arq:
            arq.write("\nInserindo dados no arquivo")
    else:
        print("O arquivo não existe")

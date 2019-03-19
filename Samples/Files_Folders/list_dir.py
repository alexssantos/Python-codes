import os
import time


# Get actual file directory
file_path = os.path.dirname(os.path.abspath(__file__))
print('file path:', file_path)

# Current diretory
local = os.getcwd()
print('atual local: ', local)

lista = os.listdir()
dic = {}    # cria dicionário
for i in lista:     # Varia na lista dos arquivos e diretórios
    if os.path.isfile(i):  # checa se é um arquivo
        # Cria uma lista para cada arquivo. Esta lista contém o
        # tamanho, data de criação e data de modificação.
        dic[i] = []
        dic[i].append(os.stat(i).st_size)   # Tamanho
        dic[i].append(os.stat(i).st_atime)  # Tempo de criação
        dic[i].append(os.stat(i).st_mtime)  # Tempo de modificação


titulo = '{:27}'.format("Nome")  # 10 caracteres + 1 de espaço
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Modificação")
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Criação")
titulo = titulo + "tamanho"

print(titulo)

for i in dic:
    kb = dic[i][0]/1000
    tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
    print('{:26}'.format(i),
          time.ctime(dic[i][2]),
          " ",
          time.ctime(dic[i][1]),
          " ",
          tamanho)

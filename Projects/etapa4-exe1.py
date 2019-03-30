import os

# Pegar o diretório
#path = os.path.realpath(input(print(r'Digite o Diretório exemplo "C:\\Users\alex.silva\Downloads"'))) # 'r' antes significa pruduzir raw string ou Duplicar \\
path = os.path.dirname(input(print('Digite o nome do diretorio acima: '))) 

# Obtém lista de arquivos e diretórios do diretório corrente:
lista = os.listdir(path)
dic = {}  # cria dicionário
for i in lista:  # Varia na lista dos arquivos e diretórios
    if os.path.isfile(i):  # checa se é um arquivo
        # Cria uma lista para cada arquivo. Esta lista contém o
        # tamanho, data de criação e data de modificação.
        dic[i] = []
        dic[i].append(os.stat(i).st_size)  # Tamanho
        dic[i].append(os.stat(i).st_atime)  # Tempo de criação
        dic[i].append(os.stat(i).st_mtime)  # Tempo de modificação

print(dic)
# https://www.tutorialspoint.com/python/os_listdir.htm

# comar o tamanho de todos os arquivos dentro de um diretorio digitado
import os


dir_name = input('entre com o diretorio: ')
if os.path.isdir(dir_name):
    somador = 0
    lista = os.listdir(dir_name)
    for i in lista:
        path = os.path.join(dir_name, i)
        if os.path.isfile(path):
            somador = somador + os.stat(path).st_size
    
    print('Tamanho:', somador/1000, "KB")
else:
    print("O diretório", '\''+dir_name+'\'', "não existe.")
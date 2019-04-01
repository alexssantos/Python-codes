''' # AT-DR4
    3.  Escreva um programa em Python que:
        3.a) gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
        3.b) Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
        3.c) gere um arquivo texto com os valores desta estrutura ordenados.
'''

# ok - pegar o nome do diretorio dir_name.
# ok - vasculhar por dir_name a partir da pasta padrao do usuario. #os.chdir(path) : path = os.environ['HOMEPATH']
#   [exists] pegar todos os arquivos e seus tamanhos dentro do dir_name especificamente. Nao entrar nas pastas.
#   [exists] pegar a tamanho do dir_name
# escrever em um txt: 'nome:file.py - tamanho:777Kb' arquivo por linha.

import os
from glob import glob

PATH_START = '.'

dir_name = input('''\
    Digite o nome da pasta.
    >>> ''')

# Go to Desktop folder
os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
print(f'Vasculhando dentro de: {os.getcwd()}')

# vasculhar se a pasta existe e pegar o absolute-path
result = [y for x in os.walk(PATH_START)
          for y in glob(os.path.join(x[0], dir_name))]
files_dict = {}
if result and len(result) != 0:    
    full_path = os.path.join(os.getcwd(), result[0][2:])    # [2:] ignotrando erro de '.\\' da str
    files = os.listdir(full_path)
    for file_name in files:
        file_path = os.path.join(full_path, file_name)
        file_data = os.stat(file_path)
        files_dict[file_name] = int(file_data.st_size)

else:
    print('pasta nao encontrada!  :( ')

# lambda chave-valor => chave-valor organiza pelo item 2 ([1]) do valor do dicionario // [::-1] reverte a lista de retorno
result = sorted(files_dict.items(), key=lambda kv: kv[1])[::-1]
print(*result, sep='\n')
if len(result):
    new_file = open("Quest3_AT_R4.txt", "w")
    for data in result:
        line = f'name: {data[0]} - tamanho: {data[1]} \n'
        new_file.write(line)
    new_file.close()

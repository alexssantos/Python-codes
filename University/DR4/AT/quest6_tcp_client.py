''' # DR4-AT
    6. Escreva um programa cliente e servidor sobre TCP em Python em que:
        a) O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
        b) O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
'''

import socket
import pickle


# Cria o socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4200
host = '127.0.0.1'


folder_name = input('''
(Vamos procurar a pasta a partir da AREA DE TRABALHO para ser amis rapido)
Entre com o nome da pasta: 
>>> ''')
try:
    # Tenta se conectar ao servidor
    soc.connect((host, port))
    # Envia o nome do arquivo:
    soc.send(folder_name.encode('ascii'))
    # Recebe o tamanho do arquivo:
    data_recv = soc.recv(2048)
    response = pickle.loads(data_recv)
except Exception as erro:
    print(str(erro))


if response == '' or len(response) < 1:
    print('Nenhuma Pasta encotrada.')
else:
    path_keys = response.keys()
    for key in path_keys:
        files_list = response[key]
        print(f'Path: {key}')
        print('Files:')
        for file_ in files_list:
            print(f'\t{file_}')
        print()

# Fecha o socket
soc.close()
input("Pressione qualquer tecla para sair...")

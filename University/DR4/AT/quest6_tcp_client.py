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


folder_name = input('Entre com o nome da pasta: \n>>> ')
try:
    # Tenta se conectar ao servidor
    soc.connect((host, port))
    # Envia o nome do arquivo:
    soc.send(folder_name.encode('ascii'))
    # Recebe o tamanho do arquivo:
    data_recv = soc.recv(2048)
    files_list = pickle.loads(data_recv)

    '''TRATAMENTOS
    if len(files_list) > 0:
        # tem arquivos
        print('Arquivos: ')
    else:
        print('Arquivo não encontrado no servidor!')    '''

except Exception as erro:
    print(str(erro))

# Fecha o socket
soc.close()
print(*files_list, sep='\n')
input("Pressione qualquer tecla para sair...")

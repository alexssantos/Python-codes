''' # DR4-AT
    6. Escreva um programa cliente e servidor sobre TCP em Python em que:
        - O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
        - O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
'''

import socket
import sys
import os
import pickle


# Imprime o status de download
# def imprime_status(bytes, tam):
#     kbytes = bytes/1024
#     tam_bytes = tam/1024
#     texto = 'Baixando... '
#     texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
#     texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
#     print(texto)


# Cria o socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4200
nome_pasta = input('Entre com o nome da pasta: \n>>> ')
try:
    # Tenta se conectar ao servidor
    soc.connect((socket.gethostname(), port))
    # Envia o nome da pasta
    soc.send(nome_pasta.encode('ascii'))
    # Recebe 
    data_recv = soc.recv(MAX_BUFFER_SIZE=2048)
    files_list = pickle.loads(data_recv)
except Exception as erro:
    print(str(erro))

# Fecha o socket
soc.close()
print(f'''
-------------------------------------------------

-------------------------------------------------
''')
input("Pressione qualquer tecla para sair...")

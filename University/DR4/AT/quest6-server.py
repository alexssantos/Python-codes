''' # DR4-AT
    6. Escreva um programa cliente e servidor sobre TCP em Python em que:
        - O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
        - O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
'''

import socket
import sys
import pickle
import os
import glob


def search_folder(f_name):
    user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')       # >>> 'C:\\Users\\aarka\\Desktop'
    os.chdir(user_desktop)    
    result = [y for x in os.walk('') for y in glob(os.path.join(x[0], f_name))]    # empty list se não encotrar.    
    if not result or len(result) == 0:
        return ''
    full_path = os.path.join(user_desktop, result[0][2:])
    
    # SE ARQUIVO
    if os.path.isfile(full_path):
        file_path = result[0]
        file_data = os.stat(file_path)        
        return file_data, full_path, True

    full_path = os.path.join(user_desktop, result[1][2:])
    os.chdir(full_path)
    os.chdir('..')
    # SE PASTA
    if os.path.isdir(search_input):
        folder_data = os.listdir(search_input) #nome da pasta
        folders_dict_list = [x for x in folder_data if os.path.isdir(x)]  
        file_data = {}
        file_data['folders'] = folders_dict_list

        files_dict_list = [os.stat(x) for x in folder_data if os.path.isfile(x)]        
        file_data['files'] = files_dict_list
        return file_data, full_path, False #nao é arquivo


host = socket.gethostname()
port = 4200
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # IPv4 | TCP/IP
# SO_REUSEADDR -"Kernel, pfv, pega logo um socket local em espera (TIME_WAIT)"
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("INICIANDO conexão Socket...")

try:
    soc.bind((host, port))  # bind ("ligar/conectar")
    print("Server UP!\n")        
except:
    print("Bind failed. Error : " + str(sys.exc_info()))
    sys.exit()

soc.listen(5)       # queue up to 5 requests    // limite da FILA
print(f"Server ouvindo em {host}:{port}")
while True:
    connection, address = soc.accept()
    ip, port = str(address[0]), str(address[1])
    print(f'''
+----------------------------------------
|  Connected with: {ip}:{port}
+---------------------------------------- ''')


soc.close()
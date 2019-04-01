''' # DR4-AT
    6. Escreva um programa cliente e servidor sobre TCP em Python em que:
        a) O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
        b) O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
'''

import socket
import os
from glob import glob
import pickle


def get_files_in(full_path, folder_name):
    if not os.path.isdir(full_path):
        return ''

    os.chdir(full_path)
    os.chdir('..')
    folder_data = os.listdir(folder_name)  # nome da pasta
    # //folders_dict_list = [x for x in folder_data if os.path.isdir(x)]
    files_list = [os.stat(x)
                  for x in folder_data if os.path.isfile(x)]
    return files_list


def search_folder2(folder_name):
    if not folder_name or folder_name == '':
        return ''

    PATH = '.'
    # >>> 'C:\\Users\\aarka\\Desktop'
    user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    os.chdir(user_desktop)
    # empty list se não encotrar.
    result = [y for x in os.walk(PATH)
              for y in glob(os.path.join(x[0], folder_name))]

    if not result or len(result) == 0:
        return ''
    folder_paths = [os.path.join(user_desktop, x[2:]) for x in result]    
    
    return folder_paths



def search_folder(folder_name):
    if not folder_name or folder_name == '':
        return ''

    PATH = '.'
    # >>> 'C:\\Users\\aarka\\Desktop'
    user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    os.chdir(user_desktop)
    # empty list se não encotrar.
    result = [y for x in os.walk(PATH)
              for y in glob(os.path.join(x[0], folder_name))]

    if not result or len(result) == 0:
        return ''
    folder_paths = [os.path.join(user_desktop, x[2:]) for x in result]
    dir_itens_list = [os.listdir(x) for x in folder_paths]
    # delete dirs
    i_dir = 0
    for dir_itens in dir_itens_list:
        os.chdir(folder_paths[i_dir])    
        dir_itens_list[i_dir] = [item for item in dir_itens if not os.path.isdir(item)]
        i_dir += 1

    ''' BUILDING DICT
        dict = {
            'path':[files, file2, ...],
            'path2':[files, file2, ...]
        }'''
    retorno = dict((k, dir_itens_list[folder_paths.index(k)]) for k in folder_paths)
    return retorno


def print_connected_with(ip, port):
    tab = '-'*8
    print(f'''
+{tab*5}+
|  Connected with: {ip}:{port}\t |
+{tab*5}+''')


host = '127.0.0.1'
port = 4200
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # IPv4 | TCP/IP
# SO_REUSEADDR -"Kernel, pfv, pega logo um socket local em espera (TIME_WAIT)"
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    soc.bind((host, port))
    print("Server UP!\n")
except Exception as erro:
    print("Bind failed. Error : " + str(erro))

soc.listen()       # queue up to 5 requests    // limite da FILA
print(f"Server ouvindo em {host}:{port}")

client_conn, address = soc.accept()
ip, port = str(address[0]), str(address[1])
print_connected_with(ip, port)
msg_encoded = client_conn.recv(2048)
folder_name = msg_encoded.decode('ascii')

path_files_dict = search_folder(folder_name)

pickled = pickle.dumps(path_files_dict)
client_conn.send(pickled)

soc.close()

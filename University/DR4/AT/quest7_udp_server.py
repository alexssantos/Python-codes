''' # DR4-AT
   7.Escreva um programa cliente e servidor sobre UDP em Python que:
        a) O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
        b) O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
'''

import socket
import psutil
import pickle


HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 4200                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


def get_mem():
    free = psutil.virtual_memory().free
    total = psutil.virtual_memory().total
    return free, total


while True:
    print('Esperando receber na porta', PORT, '...')
    (msg, cliente) = udp.recvfrom(1024)    
    print(msg.decode('ascii'))
    # pegar o disco em que esta o processo
    free_mem, total_mem = get_mem()
    response = [total_mem, free_mem]

    print(f'''
+=============================================
|    Client:  \t{cliente[0]}:{cliente[1]} 
|    Response:\t{response}
+=============================================
    ''')
    bytes = pickle.dumps(response)
    udp.sendto(bytes, cliente)

udp.close()
input('Pressione qualquer tecla para sair...')
''' # DR4-AT
   7.Escreva um programa cliente e servidor sobre UDP em Python que:
        a) O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
        b) O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
'''

import socket, pickle, datetime


HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 4200                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)


def make_request(udp_soc, vez=1):  
    bytes = ''      
    udp_soc.settimeout(5.0)
    udp_soc.sendto(msg.encode('ascii'), address)    
    try:
        (bytes, client) = udp_soc.recvfrom(1024)
    except socket.timeout:        
        if vez == 5:        
            return bytes
        vez += 1        
        print('Excedeu tempo de espera.')
        print(f'tentando pela {vez}° vez.')
        make_request(udp_soc, vez=(vez))    
    return bytes


msg = "memory-total-free"
print("pedindo memoria total e disponivel.")

start = datetime.datetime.now()
bytes = make_request(udp)

if bytes != '':
    response = pickle.loads(bytes)
    dif = datetime.datetime.now() - start
    print('timeout: ', dif)
    udp.settimeout(None)

    MB = 1000**2
    total = round(response[0]/MB)
    dispo = round(response[1]/MB)

    print(f'''
    +-------------------------
    |       --- MEMORY ---
    |  Total:\t{total} Mb 
    |  Free: \t{dispo} Mb
    +-------------------------''')

print('''
-------------------------------
Conexão Encerrada.
-------------------------------
''')
udp.close()
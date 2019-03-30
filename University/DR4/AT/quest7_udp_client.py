''' # DR4-AT
   7.Escreva um programa cliente e servidor sobre UDP em Python que:
        a) O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
        b) O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
'''

import socket, pickle

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 4200                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)
msg = "memory-total-free"
print("pedindo armazenamento total e disponivel do disco principal.")
udp.sendto(msg.encode('ascii'), address)
(bytes, client) = udp.recvfrom(1024)
response = pickle.loads(bytes)
MB = 1000**2
total = round(response[0]/MB)
dispo = round(response[1]/MB)

print(f'''
+-------------------------
|MEMORY:
|Total: {total}Mb 
|Free: {dispo}Mb
+-------------------------''')
udp.close()
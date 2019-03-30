import socket, psutil, os

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 9991                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    print('Esperando receber na porta', PORT, '...')
    (msg, cliente) = udp.recvfrom(1024)    
    # pegar o disco em que esta o processo
    p = psutil.Process()
    full_path = p.cwd()
    #pegar as insfo do disco
    path = full_path.split("\\")[0]
    total = psutil.disk_usage(path).total / 1024**3
    dispo = psutil.disk_usage(path).free / 1024**3
    response = [total, dispo]
    print(cliente, response)
    udp.sendto(response, cliente)

udp.close()
input('Pressione qualquer tecla para sair...')


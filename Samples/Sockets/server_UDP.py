import socket, psutil, os

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 9991                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')
(msg, cliente) = udp.recvfrom(1024)
reponse = []
# pegar o disco em que esta o processo
PID = os.getpid()
print(PID)
p = psutil.Process()
full_path = p.pid #p.cwd(PID)
#pegar as insfo do disco
path = full_path.split("/")[0]
main_disk = psutil.disk_partitions()[0]
print('main disk:', msg)
total = psutil.disk_usage(path).total
dispo = psutil.disk_usage(path).free
print(cliente, msg.decode('ascii'))

udp.sendto(response, cliente)
udp.close()
input('Pressione qualquer tecla para sair...')


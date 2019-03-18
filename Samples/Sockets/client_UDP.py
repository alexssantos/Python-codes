import socket

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = "disk"
print("pedindo armazenamento total e disponivel do disco principal.")
udp.sendto (msg.encode('ascii'), dest)
(msg, client) = udp.recvfrom(1024)
total = msg.decore('ascii')
dispo = msg.decore('ascii')

print(f"armazenamento total: {total} e disponivel: {dispo}")
udp.close()
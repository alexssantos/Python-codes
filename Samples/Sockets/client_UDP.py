import socket, pickle

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = "disk"
print("pedindo armazenamento total e disponivel do disco principal.")
udp.sendto(msg.encode('ascii'), dest)
(bytes, client) = udp.recvfrom(1024)
response = pickle.load(bytes)
total = response[0]
dispo = response[1]

print(f"armazenamento total: {total}Gb e disponivel: {dispo}Gb")
udp.close()
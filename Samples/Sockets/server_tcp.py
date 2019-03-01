import socket, sys

#create socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # testa conexao
    s.connect(socket.gethostbyname(), 9999)
except Exception as errorMsf:
    print(str(errorMsf))
    sys.exit(1) 


print("Para encerrar, digite '$'")
msg = input()

s.send()
amigos = ()

amigo = input("ENTER p/ SAIR ou Nome do amigo: ")

while amigo != "":
    amigos += (amigo, )
    amigo = input("ENTER p/ SAIR ou Nome do amigo: ")

for amigo in amigos:
    print("My friend: ", amigo)
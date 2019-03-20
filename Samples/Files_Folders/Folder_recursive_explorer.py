import os


lista_dir = []
entrada = input("Entre com o diretório: ")

if os.path.isdir(entrada):  
    lista_dir.append(entrada)
    somador = 0
    p_dir = ""

    #Get all dir
    while lista_dir:
        diretorio = lista_dir[0]
        p_dir = os.path.join(p_dir, diretorio)
        lista = os.listdir(p_dir)   # Listando dentro do diretorio nivel1        

        for i in lista:     # varre subpasta
            p = os.path.join(p_dir, i)  # sub path

            if os.path.isdir(p):
                lista_dir.append(i)     # add todos os diretorios encontrados na lista.

            elif os.path.isfile(p):
                somador = somador + os.stat(p).st_size
                lista_dir.remove(diretorio)
                print(str(somador/1000) + " KB")

            else:
                print("O diretório", '\''+p_dir+'\'', "não existe.")

import os


lista = os.listdir()

lista_arq = []
lista_dir = []

for i in lista:
    if os.path.isfile(i):
        lista_arq.append(i)
    else:
        lista_dir.append(i)

if len(lista_arq) > 0:
    print("Arquivos: ")
    for i in lista_arq:
        print('\t'+i)
    print('')

if len(lista_dir) > 0:
    print('Diretorios: ')
    for i in lista_dir:
        print('\t'+i)
    print('')
        
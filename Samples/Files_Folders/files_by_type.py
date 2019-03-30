import os

print(os.path.splitext("exemplo.arq.txt"))
# >>> ('exemplo.arq', '.txt')

lista = os.listdir()

dic_arq = {}
list_dir = []
for i in lista:
    if os.path.isfile(i):
        # pega a extensao
        # TODO: tratar para arquivos ocultos ( .file )
        ext = os.path.splitext(i)[1]

        # ja add ?
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i)
    else:
        list_dir.append(i)

for key in dic_arq:
    print('arquivos ', key)
    for item in dic_arq[key]:
        print('\t' + item)

print('Pastas:')
for pasta in list_dir:
    print('\t' + pasta)

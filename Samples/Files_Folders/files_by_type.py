import os

print(os.path.splitext("exemplo.arq.txt"))
# >>> ('exemplo.arq', '.txt')

lista = os.listdir()

dic_arq = {}
for i in lista:
    if os.path.isfile(i):
        # pega a extensao
        ext = os.path.splitext(i)[1]    # TODO: tratar para arquivos ocultos ( .file )

        # ja add ?
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i)

for key in dic_arq:
    print('\
          ', key)
    for item in dic_arq[key]:
        print('\
              ', item)

print(dic_arq)
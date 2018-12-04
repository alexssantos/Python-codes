def miracle(intT: tuple):
    impList = [x for x in intT if(x % 2 != 0)]
    posParT = tuple(x for x in intT if intT.index(x) % 2 == 0)      # pos: 0, 2, 4, ...
    return impList, posParT


numbsT = tuple(str.split(input('Digite numeros: ')))
numbsT = tuple(int(x) for x in numbsT)
implist, posParT = miracle(numbsT)
print('lista com impares: ', implist)
print('tupla de index par: ', posParT)

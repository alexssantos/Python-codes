t = tuple(str.split(input(print('Digite 3 numeros: '))))
t = [int(x) for x in t]

aux = []
for i in t:
    for x in t:
        if i > x:
            aux.insert(0, i)
    

print(t)
print(aux)

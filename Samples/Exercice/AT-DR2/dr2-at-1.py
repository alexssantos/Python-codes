t = tuple(str.split(input(print('Digite 3 numeros: '))))

aux = []
for i in len(t):
    for x in t:
        if i > x:
            aux.insert(i)
    

print(t)

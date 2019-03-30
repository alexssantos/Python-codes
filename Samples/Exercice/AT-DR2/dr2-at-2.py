numb = int(input(print('Digite um numero: ')))
numb = abs(numb)

aux = []
for x in range(1, numb+1):
    if x % 2 == 0:
        aux.append(x)

print("soma: ", sum(aux))

aux2 = 0
for x in aux:
    aux2 += x
    print(aux2 - x, " + ", x, " = ", aux2)

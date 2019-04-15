myList = str.split(input('type numbers: '))
myList = [int(x) for x in myList]
# myList = list(range(6))   //jeito 2
print('ordem inversa: ', myList[::-1])

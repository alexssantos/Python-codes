myList = []

for element in range(5):
    myList.append(element)

print(myList)

if 3 in myList:
    myList.remove(3)
else:
    print('myList do not have item 3')

if 6 in myList:
    myList.remove(6)
else:
    print('myList do not have item 6')

print(myList)
print('Length of myList: ', len(myList))

myList[-1] = 6
print(myList)
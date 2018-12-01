key = True
t = 0
numbList = []

while key:
    while key:
        a = int(input(print('type the vetor length: ')))
        try:
            t = int(a)
            key = False
        except ValueError:
            print(a, 'is not a number')
    key = True
    while key:
        myList = str.split(
            input(print('type ', a, 'numbers separeted by space: ')))
        if len(myList) == a:
            for isNumb in myList:
                try:
                    numbList.append(int(isNumb))
                except ValueError:
                    print('Error: "', isNumb, '" is not a number!')
            key = False
        else:
            print('You do not type ', a, ' number!')

numbList = [x for x in numbList if x == 0]
print('quatities of "0" typed: ', len(numbList))

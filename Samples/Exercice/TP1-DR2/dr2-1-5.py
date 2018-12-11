
# REFAZER 
# fazer uma func para cada item pedido. 

print("Press ENTER to exit! ")

print("Tuple = (a-z)")
letters = ("jamais podemos esquecer de amar")

flag = True
while flag:
    print("Type 1 to SEARCH \n")
    print("Type 2 to DIVEDE \n")
    print("Type 3 to DELETE \n")
    print("Type 4 to INVERT \n")
    x = input("Menu: ")

    if x == "":
        flag = False
        break

    x = int(x)
    if x == 1:
        letter = str(input("type something to search: "))
        index = letters.index(letter)
        print(index)

    elif x == 2:
        lenght = len(letters)
        first = 0
        middle = lenght//2
        firstLetters, lastLetters = ()
        if lenght % 2 > 0:
            middle += 1
            while first < middle:
                firstLetter = (letters[first], )
                lastLetters = (letters[-first], )     # percorrer ao contrario
                first += 1
            print("1° metade: ", firstLetter)
            print("2° metade: ", lastLetters)
        else:
            while first < middle:
                firstLetter = (letters[first], )
                lastLetters = (letters[first+middle], )
                first += 1
            print("1° metade: ", firstLetter)
            print("2° metade: ", lastLetters)

    elif x == 3:
        letter = str(input("type something to search: "))
        a = letters.index(letter)
        del letters[a]
        print(letters)
    elif x == 4:
        invertLetters = letters[::-1]
        print(invertLetters)

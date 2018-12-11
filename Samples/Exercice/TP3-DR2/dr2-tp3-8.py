import random

jogadas = [random.randint(1, 6) for x in range(100*100)]
dadosDict = dict((x, 0) for x in range(1, 7))       # mock - dadosCount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
print('dadosDict: ', dadosDict)

for jogada in jogadas:
    if jogada in dadosDict:
        dadosDict[jogada] += 1
    else:
        dadosDict[jogada] = 1

for dado in dadosDict:
    print(dado, ' - ', dadosDict[dado], ' vezes \n')

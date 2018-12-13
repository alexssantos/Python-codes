stayIn = True
phrases = []

while stayIn:
    print('Digite "sair" para sair!')
    phrase = input('Frase:  ')
    if phrase == '' or phrase == 'sair':
        stayIn = False
        break
    phrase = str.split(phrase)
    phrases.append(phrase)

print(phrases)
contains_EU = []
for phrase in phrases:
    for item in phrase:        
        if 'eu' == item:
            _str = ' '.join(phrase)
            print('JOIN: ', _str)
            contains_EU.append(_str)

for phrase in contains_EU:
    print('\n Frase contendo "eu" -> ', phrase)

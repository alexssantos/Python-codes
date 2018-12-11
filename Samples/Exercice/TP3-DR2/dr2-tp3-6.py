stayIn = True
phrases = []

while stayIn:
    print('Digite "sair" para sair!')
    phrase = input(print('Frase:  '))
    if phrase == '' or phrase == 'sair':
        stayIn = False
        break
    phrase = str.split(phrase)
    phrases.append(phrase)

print(phrases)
contains_EU = []
for phrase in phrases:
    if any('eu' in x for x in phrase):
        _str = ' '.join(phrase)
        print('JOIN: ', _str)
        contains_EU.append(_str)
    # for word in phrase:
    #     if word == 'eu':
    #         _str = ' '.join(phrase)
    #         contains_EU.append(_str)

    # contains_EU = [x for x in phrase if x == 'eu']
for phrase in contains_EU:
    print('\n', phrase)

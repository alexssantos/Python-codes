stayIn = True

myList = []

while stayIn:
    print(
        '-----------------------------------\n'
        '               MENU                \n'
        '-----------------------------------\n'
        '      (1) Mostrar Lista            \n'
        '      (2) Add Elemento             \n'
        '      (3) Remover Elemento         \n'
        '      (4) Remover ALL Elementos    \n'
        '      (5) Sair                     \n'
    )
    try:
        choice = int(input())        
    except ValueError:
        print(
            'Escolha Invalida \n'
            'FIM DO PROGRAMA  \n'
            )
        break
    if choice in range(6):
        if choice == 1:
            print(
                '\n'
                '------------- MY LIST -------------\n',
                myList,                             '\n'
                                                    '\n'
            )
        elif choice == 2:
            print('Add: ')
            myList.append(input())
        elif choice == 3:
            print('Remover: ')
            try:
                myList.remove(input())
            except ValueError:
                print('\n Valor não encontrado. \n')
        elif choice == 4:
            myList.clear()
        elif choice == 5:
            stayIn = False
    else:
        print(
              '                                       \n'
              '---------- Escolha Invalida! ----------\n'
              )

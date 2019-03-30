''' # DR4-AT
    5. Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
        a.txt   = 19 56 -43 23 -7 -11 33 21 61 9
        b.txt   = 1  15 -42 33 -7 -2  39  8
    Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
'''

import os

# Go to Desktop folder
os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
print('lendo arquivos (a.txt e b.txt) no Desktop...\n')

file_a = 'a.txt'
file_b = 'b.txt'


def get_bigger(list1, list2):
    if len(list1) > len(list2):
        return list1, list2
    elif len(list2) > len(list1):
        return list2, list1
    else:
        return 0, 0


sum_list = []
if os.path.exists(file_a) and os.path.exists(file_b):
    data_a = open(file_a, 'r')
    line_a = [int(a) for a in data_a.readline().split(' ')]
    data_b = open(file_b, 'r')
    line_b = [int(b) for b in data_b.readline().split(' ')]
    result = get_bigger(line_a, line_b)     # retoena (maior, menors)
    if result[0] == 0:  # iguais
        sum_list = [a + result[1][result[0].index(a)] for a in result[0]]
        print(sum_list)
    else:        
        ix = len(result[1])
        for x in result[0]:            
            if not ix <= 0:     # 0 itens para iterar                
                sum_list.append(x + result[1][result[0].index(x)])
                ix -= 1
            else:
                sum_list.append(x + 0)
    print(sum_list)

else:
    print('Arquivos não encontrados.')
import requests
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data //table formats - 1 tabulate - 2 prettytable  - 3 texttable
from prettytable import PrettyTable


url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text

linhas = csv.splitlines()   # list<string> - Cada string com info separadas por ','
header = linhas[0].split(',')
dataLists = [x for x in linhas[1:]]


def LinesAndposuns(linhas):
    for lin in linhas:      # lin = string - info separadas por ','
        posunas = lin.split(',')  # extrai valores separados por virgula
        print(posunas)


# CUIDADO COM A QUANTIDADE DE posUNAS - PODE FICAR AGLOMERADO
def PrintTable(_headerList, _dataLists):
    # _dataLists list<string>

    _table = PrettyTable(_headerList)
    for line in _dataLists:
        dataLineList = line.split(',')
        _table.add_row(dataLineList)

    print(_table)


# LinesAndposuns(linhas)
# PrintTable(header, dataLists)

'''
# Fazer a Média Anual

>Numeros (por index da lista)
    linhas usadas: 1 -> final
    posunas usadas: 4 -> final
'''

for linha in range(1, len(linhas)):
    colunas = linhas[linha].split(',')

    soma = 0
    for pos in range(4, len(colunas)):
        soma += float(colunas[pos])

    media = soma/(len(colunas)-4)
    print('MÉDIA: ', media)

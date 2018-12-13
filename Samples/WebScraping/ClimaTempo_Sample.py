import requests
from prettytable import PrettyTable

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text

linhas = csv.splitlines()   # list<string> - Cada string com info separadas por ','
header = linhas[0].split()
dataLists = [x for x in linhas[1:]]


def LinesAndColuns(linhas):
    print(
        '-------------LINHAS------------\n\n',
        linhas,
        '\n-------------------------\n')

    for lin in linhas:      # lin = string - info separadas por ','
        index = linhas.index(lin) + 1

        print(  # cada linha
            '-------------LINHA %d ------------\n\n' % index,
            lin, '\n')

        colunas = lin.split(',')  # extrai valores separados por virgula
        print(  # cada coluna
            '-------------COLUNA %d ------------\n\n' % index,
            colunas, '\n')


def PrintTable(_headerList, _dataLists):
    # _dataLists inclui varias linhas

    _table = PrettyTable(_headerList)
    for line in _dataLists:
        dataLineList = line.split()
        _table.add_row(dataLineList)

    print(_table)


# LinesAndColuns(linhas)
PrintTable(header, dataLists)

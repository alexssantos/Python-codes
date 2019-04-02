import requests
from prettytable import PrettyTable     # PRECISA INSTALAR
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
# Dentro: 5 DIV - 1 titulo, 4 linhas


def PrintTable(_headerList, _dataLists):
    # _dataLists list<string>

    _table = PrettyTable(_headerList)
    for line in _dataLists:
        _table.add_row(line)

    print(_table)


titulo = soup.find_all('div', attrs={"class": "titulo"})
titleList = titulo[0].text.split('\n')[1:-1]
linhas = soup.find_all('div', attrs={"class": "linha"})

linhasDict = {}
ix = 1
for linha in linhas:
    linhasDict[ix] = linha.text.split('\n')[1:-1]
    ix += 1

dataLine = []
for i in range(1, 5):
    dataLine.append(linhasDict[i])
PrintTable(titleList, dataLine)

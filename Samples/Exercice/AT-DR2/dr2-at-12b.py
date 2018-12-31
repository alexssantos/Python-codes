import requests
from prettytable import PrettyTable      # PRECISA INSTALAR
from bs4 import BeautifulSoup

listSigla = ['DF', 'GO', 'MT', 'MS']

choise = ""
getOut = False
while not getOut:
    choise = input('Digite uma Sigla da região Centro-Oeste (GO): ')
    if choise in listSigla:
        getOut = True
    else:
        print('Sigla Errada! \n')

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')


def PrintTable(_headerList, _dataLists):
    # _dataLists list<string>

    _table = PrettyTable(_headerList)   
    _table.add_row(_dataLists)

    print(_table)


titulo = soup.find_all('div', attrs={"class": "titulo"})
titleList = titulo[0].text.split('\n')[1:-1]
linhas = soup.find_all('div', attrs={"class": "linha"})

linhasDict = {}
for linha in linhas:
    linhaValue = linha.text.split('\n')[1:-1]
    linhasDict[linhaValue[0]] = linhaValue

PrintTable(titleList, linhasDict[choise])

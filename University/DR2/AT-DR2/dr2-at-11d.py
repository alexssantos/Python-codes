import requests

url_csv = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

try:
    resp = requests.get(url_csv, timeout=5)
    if resp.status_code != requests.codes.ok:     # or != 200
        resp.raise_for_status()
    else:
        print("Conectado com sucesso!")
except Exception as e:
    print('Exception: ', e)

csvFile = resp.text
gamesByLineList = csvFile.splitlines()

# D) Genero X,Y,... - Marca que mais VENDEU


def getSalesGame(saleslist):
    totalGameSale = 0.0
    for venda in saleslist:
        if venda and venda.strip() and len(venda) <= 5:     # empty ou ' '
            try:
                vendaInt = float(venda)
                totalGameSale += vendaInt

            except Exception as e:
                print('Exception: getSalesGame | Linhas mal preenchida | ', e)

    return totalGameSale


def getTotalSales(brand):
    totalSales = 0.0
    for line in gamesByLineList[1:]:
        lineValuesList = line.split(',')
        brandLineValue = lineValuesList[4]

        if brand == brandLineValue:
            for venda in lineValuesList[5:10]:
                if venda and venda.strip():
                    try:
                        vendaInt = float(venda)
                        totalSales += vendaInt

                    except Exception as e:
                        print('Exception: getTotalSales -- ', e)
    return totalSales


def isNumber(candidate):
    lista = list(range(10))
    numberRx = [str(x) for x in lista]
    if candidate[-1] in numberRx and candidate[0] in numberRx:
        return True
    else:
        return False


# Dict< string, Dict<string, int >>
# totalSalesByGenreDict< genre, < marca, publicaçõesNoGenero >>
noRightFormatLineList = []
totalSalesByGenreDict = {}


YEAR_FILTER = 2018 - 10         # coluna 3
COUNTRY_FILTER = 'Japão'        # Coluna não encontrada.

for line in gamesByLineList[1:]:
    lineValuesList = line.split(',')

    i = 0    
    try:
        for candidate in lineValuesList:
            if isNumber(candidate) and len(candidate) == 4:
                i = lineValuesList.index(candidate)
                break

        yearValue = int(lineValuesList[i])

    except Exception as e:
        # get item YEAR index 05 or 03
        print('Exception: ', e)
        yearValue = 0
        noRightFormatLineList.append(lineValuesList)
    
    genreValue = lineValuesList[3]
    brandLineValue = lineValuesList[4]

    if (isNumber(lineValuesList[5])):
        totalSales = getSalesGame(lineValuesList[5:10])
    else:
        noRightFormatLineList.append(lineValuesList)
        ix = lineValuesList.index(str(yearValue))
        i = ix + 1

        for candidate in lineValuesList[i:]:    # Ano é numero.
            if isNumber(candidate):
                i = lineValuesList.index(candidate)
                break
        
        totalSales = getSalesGame(lineValuesList[i:i+5])

    if yearValue >= YEAR_FILTER:
        # existe o genero
        if genreValue in totalSalesByGenreDict:
            # existe a marca
            if brandLineValue in totalSalesByGenreDict[genreValue]:
                totalSalesByGenreDict[genreValue][brandLineValue] += totalSales
            else:
                totalSalesByGenreDict[genreValue][brandLineValue] = totalSales

        else:
            totalSalesByGenreDict[genreValue] = {}
            totalSalesByGenreDict[genreValue][brandLineValue] = totalSales


rankingsList = []
salesRankingList = []
for genreTag in totalSalesByGenreDict:

    # list of tuples sorted
    rankingMarcasBySales = [(k, totalSalesByGenreDict[genreTag][k]) for k in sorted(
        totalSalesByGenreDict[genreTag],
        key=totalSalesByGenreDict[genreTag].get,
        reverse=True)]

    rankingsList.append(rankingMarcasBySales)
    salesRankingList.append(genreTag)

i = 0
for genre in salesRankingList:

    topOfGenreList = rankingsList[i]
    brand = topOfGenreList[0][0]
    totalSaledInGenre = topOfGenreList[0][1]

    print('\n ----------- %s ----------- \n' % genre)
    print('Total Venda: %5.2f | Marca: %s' %
          (totalSaledInGenre, brand))

    totalSales = getTotalSales(brand)
    print('\nTotal de Vendas da marca  " %s ": %5.2f \n' % (brand, totalSales))

    print('\n ----------- TOP 3: %s ----------- \n' % genre)
    for _tuple in rankingsList[i][:3]:
        print('Vendido: %5.2f | Marca: %s' % (_tuple[1], _tuple[0]))

    i += 1


# referencias:
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values

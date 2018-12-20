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

genreFiler = ['Action', 'Shooter', 'Platform']      # coluna4

# B) Mais VENDERAM - coluna 6 a 10

marcasDict = {}
for line in gamesByLineList:
    lineValuesList = line.split(',')

    genreValue = lineValuesList[3]
    marcaLineValue = lineValuesList[4]

    if genreValue in genreFiler:

        # SALLES - coluna 5 a 9
        totalGameSale = 0.0
        for venda in lineValuesList[5:10]:
            if venda and venda.strip():
                try:
                    vendaInt = float(venda)
                    totalGameSale += vendaInt

                except Exception as e:
                    print('Exception: Parse to INT.', e)

        if marcaLineValue in marcasDict:
            marcasDict[marcaLineValue] += totalGameSale
        else:
            marcasDict[marcaLineValue] = totalGameSale

# list of tuples
rankingMarcasBySales = [(k, marcasDict[k]) for k in sorted(
    marcasDict, key=marcasDict.get, reverse=True)]

print(' ----------- TOP 3 -----------')
for key, value in rankingMarcasBySales[:3]:
    print('VENDAS: %6.2f - %s ' % (value, key))

print('\n ----------- TOTAL VENDIDO -----------')
for key, value in rankingMarcasBySales:
    print('VENDAS: %6.2f - %s ' % (value, key))


# referencias:
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values

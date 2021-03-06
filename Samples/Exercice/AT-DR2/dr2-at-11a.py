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

# A) Mais PUBLICARAM - coluna 5

marcasDict = {}
for line in gamesByLineList:
    lineValuesList = line.split(',')

    genreValue = lineValuesList[3]
    marcaLineValue = lineValuesList[4]

    if genreValue in genreFiler:
        if marcaLineValue in marcasDict:
            marcasDict[marcaLineValue] += 1
        else:
            marcasDict[marcaLineValue] = 1

# list of tuples
rankingMarcasByPublish = [(k, marcasDict[k]) for k in sorted(marcasDict, key=marcasDict.get, reverse=True)]

print(' ----------- TOP 3 -----------')
for key, value in rankingMarcasByPublish[:3]:
    print('PUBLICAÇÔES: %d - %s ' % (value, key))

print('\n ----------- TOTAL PUBLICADO -----------')
for key, value in rankingMarcasByPublish:
    print('PUBLICAÇÔES: %d - %s ' % (value, key))



# referencias:
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values

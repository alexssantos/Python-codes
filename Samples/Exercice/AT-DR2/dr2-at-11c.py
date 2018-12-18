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

YEAR_FILTER = 2018 - 10         # coluna 3
COUNTRY_FILTER = 'Japão'        # Coluna não encontrada.

# C) Genero X,Y,... - Marca com Maior PUBLICAÇÃO

# Dict< string, Dict<string, int >>
# totalpublishByGenreDict< genre, < marca, publicaçõesNoGenero >>

marcasDict = {}
totalpublishByGenreDict = {}

for line in gamesByLineList[1:]:
    lineValuesList = line.split(',')

    yearValue = int(lineValuesList[2])
    genreValue = lineValuesList[3]
    marcaLineValue = lineValuesList[4]

    if yearValue >= YEAR_FILTER:
        # if marcaLineValue in marcasDict:
        #     marcasDict[marcaLineValue] += 1
        # else:
        #     marcasDict[marcaLineValue] = 1

        if genreValue in totalpublishByGenreDict:
            totalpublishByGenreDict[genreValue][marcaLineValue] += 1
        else:
            totalpublishByGenreDict[genreValue][marcaLineValue] = 1

rankingsList = []
for Dict in totalpublishByGenreDict:

    # list of tuples
    rankingMarcasBySales = [(k, Dict[k]) for k in sorted(
        Dict, key=Dict.get, reverse=True)]
    rankingsList.append(rankingMarcasBySales)

print(' ----------- TOP 3 -----------')
for key, value in rankingMarcasBySales[:3]:
    print('PUBLICAÇÔES: %6.2f - %s ' % (value, key))

print('\n ----------- TOTAL VENDIDO -----------')
for key, value in rankingMarcasBySales:
    print('PUBLICAÇÔES: %6.2f - %s ' % (value, key))


# referencias:
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values

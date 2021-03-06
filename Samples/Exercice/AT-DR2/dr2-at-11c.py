import requests

'''
OBS: 
Não encontre semelhança enrte PUBLICAÇÂO e VENDAS. 
Logo, o filtro do país JAPAO não m efaz sentido visto que cada jogo 
tem sua priblicação, diferente do njumero de vendas em cada país. 
Nesse arquivo eu faço um filtro para vendas relacionadas somente a Japão
pois parece que publicações pode ser a quantidade de venda em cada país. 
'''


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

noYearGameList = []
totalpublishByGenreDict = {}


def getAllPublishedBrand(brand):
    countGamePublish = 0
    
    for line in gamesByLineList[1:]:
        lineValuesList = line.split(',')
        brandValue = lineValuesList[4]

        if brand == brandValue:
            countGamePublish += 1

    return countGamePublish


def toFloat(value):
    intValue = 0
    if value and value.strip():
        try:
            intValue += float(value)

        except Exception as e:
            print('toFloat Exception | ', e)
            intValue = 0
    return intValue


for line in gamesByLineList[1:]:
    lineValuesList = line.split(',')

    # Ano pode vir vazio
    if lineValuesList[2] and lineValuesList[2].strip() and len(lineValuesList[2]) == 4:
        try:
            yearValue = int(lineValuesList[2])
        except Exception as e:
            # get item YEAR index 05 or 03
            print('Exception: ', e)
            yearValue = 0
            noYearGameList.append(lineValuesList)
    else:
        yearValue = 0

    genreValue = lineValuesList[3]
    brandLineValue = lineValuesList[4]

    if yearValue >= YEAR_FILTER:

        # SALLES - coluna 5 a 9
        totalGameSale = toFloat(lineValuesList[7])    # JP Sales

        # existe o genero
        if genreValue in totalpublishByGenreDict:
            # existe a marca
            if brandLineValue in totalpublishByGenreDict[genreValue]:
                totalpublishByGenreDict[genreValue][brandLineValue] += totalGameSale
            else:
                totalpublishByGenreDict[genreValue][brandLineValue] = totalGameSale

        else:
            totalpublishByGenreDict[genreValue] = {}
            totalpublishByGenreDict[genreValue][brandLineValue] = totalGameSale


rankingsList = []
genresRankingList = []
for genreTag in totalpublishByGenreDict:

    # list of tuples sorted
    rankingMarcasBySales = [(k, totalpublishByGenreDict[genreTag][k]) for k in sorted(
        totalpublishByGenreDict[genreTag],
        key=totalpublishByGenreDict[genreTag].get,
        reverse=True)]

    rankingsList.append(rankingMarcasBySales)
    genresRankingList.append(genreTag)

i = 0
for genre in genresRankingList:
    topOfGenreList = rankingsList[i]
    brand = topOfGenreList[0][0]
    totalPublishedInGenre = topOfGenreList[0][1]

    print('\n ----------- %s ----------- \n' % genre)
    print('Jogos Publicados: %d | Marca: %s' %
          (totalPublishedInGenre, brand))

    totalJogos = getAllPublishedBrand(brand)
    print('\nTotal Jogos Publicados em todas Caregorias: %d \n' % totalJogos)

    print('\n ----------- TOP 3: %s ----------- \n' % genre)
    for _tuple in rankingsList[i][:3]:
        print('Publicados: %d | Marca: %s' % (_tuple[1], _tuple[0]))

    i += 1


# referencias:
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values

import requests

''' QUEM, ENTRE OS PAISES, FOI O MEIOR MEDALISTA DE OURO

Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega,
verifique: No século XXI(a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades...
modalidades:
        1. Curling
        2. Patinação no gelo(skating)
        3. Esqui(skiing)
        4. Hóquei sobre o gelo(ice hockey)
'''


url_csv = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

try:
    conn = requests.get(url_csv, timeout=5)
    if conn.status_code != requests.codes.ok:     # or != 200
        conn.raise_for_status()
    else:
        print("Conectado com sucesso!")

except Exception as e:
    print('Exception: ', e)


class country():
    def __init__(self, _name: str):
        self.medalsDict = {"Gold": 0, "Bronze": 0, "Silver": 0}
        self.sportsDict = {'Curling': [], 'Skating': [],
                           'Skiing': [], 'Ice Hockey': []}
        self.name = _name

    def totalGoldMedal(self):
        return self.medalsDict['Gold']


csvFile = requests.get(url_csv).text
csvLinesList = csvFile.splitlines()
countrySWE = country('SWE')
countryNOR = country('NOR')
countryFIN = country('FIN')


def tarefa10a():

    paises = ['SWE', 'NOR', 'FIN']
    esportes = ['Curling', 'Skating', 'Skiing', 'Ice Hockey']

    for line in csvLinesList:
        lineValuesList = line.split(',')

        sportValue = lineValuesList[2]
        countryValue = lineValuesList[4]
        yearValue = lineValuesList[0]
        awardValue = lineValuesList[7]

        if countryValue in paises and yearValue > '2000' and sportValue in esportes and awardValue == 'Gold':
            if countryValue == 'SWE':
                countrySWE.sportsDict[sportValue] = int(yearValue)
                countrySWE.medalsDict['Gold'] += 1

            elif countryValue == 'NOR':
                countryNOR.sportsDict[sportValue] = int(yearValue)
                countryNOR.medalsDict['Gold'] += 1

            elif countryValue == 'FIN':
                countryFIN.sportsDict[sportValue] = int(yearValue)
                countryFIN.medalsDict['Gold'] += 1

            else:
                print('Pais não identificado!')


tarefa10a()

rankingDict = {countrySWE.totalGoldMedal(): 'SWE',
               countryNOR.totalGoldMedal(): 'NOR',
               countryFIN.totalGoldMedal(): 'FIN'}

# totalOuroSWE = countrySWE.totalGoldMedal()
# totalOuroNOR = countryNOR.totalGoldMedal()
# totalOuroFIN = countryFIN.totalGoldMedal()

totalsList = sorted([countrySWE.totalGoldMedal(), countryNOR.totalGoldMedal(), countryFIN.totalGoldMedal()], reverse=True)

for total in totalsList:
    print(rankingDict[total], " ganhou: %d" % total, ' Medals ')

print('ranking : ', sorted(totalsList, reverse=True))

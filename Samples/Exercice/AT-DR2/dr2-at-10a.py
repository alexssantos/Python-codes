import requests

'''
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
        self.countParticipations = 0

    def totalGold(self):
        return self.largura + self. valtura

    def ParticipationYears(self):
        yearsCurling = [self.sportsDict['Curling']]
        yearsSkating = [self.sportsDict['Skating']]
        yearsSkiing = [self.sportsDict['Skiing']]
        yearsIceHockey = [self.sportsDict['Ice Hockey']]

        s1 = set(yearsCurling)
        s2 = set(yearsIceHockey)
        s3 = set(yearsSkating)
        s4 = set(yearsSkiing)        

        sets = [s1, s2, s3, s4]
        yearsList = set.intersection(*sets)
        return len(yearsList)


csvFile = requests.get(url_csv).text
csvLinesList = csvFile.splitlines()
countrySWE = country('SWE')
countryNOR = country('NOR')
countryFIN = country('FIN')


def tarefa10a():
    numGoldSwe = 0
    numGoldNor = 0
    numGoldFin = 0

    numSwe = 0
    numNor = 0
    numFin = 0
    numTotal = 0

    numCurlingSwe = 0
    numSkatingSwe = 0
    numSkiingSwe = 0
    numIceHockeySwe = 0

    numCurlingNor = 0
    numSkatingNor = 0
    numSkiingNor = 0
    numIceHockeyNor = 0

    numCurlingFin = 0
    numSkatingFin = 0
    numSkiingFin = 0
    numIceHockeyFin = 0

    paises = ['SWE', 'NOR', 'FIN']
    esportes = ['Curling', 'Skating', 'Skiing', 'Ice Hockey']

    for line in csvLinesList:
        lineValuesList = line.split(',')

        sportValue = lineValuesList[2]
        countryValue = lineValuesList[4]
        yearValue = lineValuesList[0]
        awardValue = lineValuesList[7]

        if countryValue in paises and yearValue > '2000' and sportValue in esportes and awardValue == 'Gold':            
            numTotal += sportValue == sportValue

            # print(lineValuesList)

            if countryValue == 'SWE':

                countrySWE.countParticipations += 1
                countrySWE.sportsDict[sportValue] = int(yearValue)
                if awardValue == 'Gold':
                    countrySWE.medalsDict['Gold'] += 1
                

                # numCurlingSwe += sportValue == 'Curling'
                # numSkatingSwe += sportValue == 'Skating'
                # numSkiingSwe += sportValue == 'Skiing'
                # numIceHockeySwe += sportValue == 'Ice Hockey'

            elif countryValue == 'NOR':

                numGoldNor += 1
                numNor += countryValue == 'NOR'
                numCurlingNor += sportValue == 'Curling'
                numSkatingNor += sportValue == 'Skating'
                numSkiingNor += sportValue == 'Skiing'
                numIceHockeyNor += sportValue == 'Ice Hockey'

            elif countryValue == 'FIN':

                numGoldFin += 1
                numFin += countryValue == 'FIN'
                numCurlingFin += sportValue == 'Curling'
                numSkatingFin += sportValue == 'Skating'
                numSkiingFin += sportValue == 'Skiing'
                numIceHockeyFin += sportValue == 'Ice Hockey'

            else:
                print('Pais não identificado!')

    print(countrySWE.ParticipationYears())
    print(
        '\nParticipação da Suécia: {} \n'
        'Suécia \n'
        'Curling: {} \n'
        'Skating: {} \n'
        'Skiing: {} \n'
        'Ice Hockey: {} \n'
        'Medalha de Ouro: {}'
        .format(numSwe, numCurlingSwe, numSkatingSwe, numSkiingSwe, numIceHockeySwe, numGoldSwe))
    print('\nParticipação da Noruega: {} \nNoruega \nCurling: {} \nSkating: {} \nSkiing: {} \nIce Hockey: {} \nMedalha de Ouro: {}'.format(
        numNor, numCurlingNor, numSkatingNor, numSkiingNor, numIceHockeyNor, numGoldNor))
    print('\nParticipação da Finlândia: {} \nFinlândia \nCurling: {} \nSkating: {} \nSkiing: {} \nIce Hockey: {} \nMedalha de Ouro: {}'.format(
        numFin, numCurlingFin, numSkatingFin, numSkiingFin, numIceHockeyFin, numGoldFin))

    print('\n\nTotal de participação: ', numTotal)





tarefa10a()

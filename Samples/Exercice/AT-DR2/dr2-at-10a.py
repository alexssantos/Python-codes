import requests

pathString = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv?attredirects=0'
conn = requests.get(pathString, timeout=5)

if conn.status_code != 200:
    conn.raise_for_status()
else:
    print("Conectado com sucesso!")

getFile = requests.get(pathString).text
getData = getFile.splitlines()


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
    for esporte in esportes:
        for pais in paises:
            for line in getData:
                cells = line.split(',')

                if cells[4] == pais and cells[0] > '2000' and cells[2] == esporte and cells[7] == 'Gold':
                    numTotal += cells[2] == esporte
                    print(cells)

                    if cells[4] == 'SWE':

                        numGoldSwe += cells[7] == 'Gold'
                        numSwe += cells[4] == 'SWE'
                        numCurlingSwe += cells[2] == 'Curling'
                        numSkatingSwe += cells[2] == 'Skating'
                        numSkiingSwe += cells[2] == 'Skiing'
                        numIceHockeySwe += cells[2] == 'Ice Hockey'

                    elif cells[4] == 'NOR':

                        numGoldNor += cells[7] == 'Gold'
                        numNor += cells[4] == 'NOR'
                        numCurlingNor += cells[2] == 'Curling'
                        numSkatingNor += cells[2] == 'Skating'
                        numSkiingNor += cells[2] == 'Skiing'
                        numIceHockeyNor += cells[2] == 'Ice Hockey'

                    elif cells[4] == 'FIN':

                        numGoldFin += cells[7] == 'Gold'
                        numFin += cells[4] == 'FIN'
                        numCurlingFin += cells[2] == 'Curling'
                        numSkatingFin += cells[2] == 'Skating'
                        numSkiingFin += cells[2] == 'Skiing'
                        numIceHockeyFin += cells[2] == 'Ice Hockey'

                    else:
                        print('Pais não identificado!')

    print('\nParticipação da Suécia: {} \nSuécia \nCurling: {} \nSkating: {} \nSkiing: {} \nIce Hockey: {} \nMedalha de Ouro: {}'.format(
        numSwe, numCurlingSwe, numSkatingSwe, numSkiingSwe, numIceHockeySwe, numGoldSwe))
    print('\nParticipação da Noruega: {} \nNoruega \nCurling: {} \nSkating: {} \nSkiing: {} \nIce Hockey: {} \nMedalha de Ouro: {}'.format(
        numNor, numCurlingNor, numSkatingNor, numSkiingNor, numIceHockeyNor, numGoldNor))
    print('\nParticipação da Finlândia: {} \nFinlândia \nCurling: {} \nSkating: {} \nSkiing: {} \nIce Hockey: {} \nMedalha de Ouro: {}'.format(
        numFin, numCurlingFin, numSkatingFin, numSkiingFin, numIceHockeyFin, numGoldFin))

    print('\n\nTotal de participação: ', numTotal)


tarefa10a()

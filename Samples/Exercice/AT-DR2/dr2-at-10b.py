import requests
import json
from collections import Counter

CSV_URL = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv?attredirects=0"
response = requests.Session().get(CSV_URL)

# separando o texto do CSV pelo char "\n" e depois
# cada linha separando pelo char ","
linhas = [x.split(",")
          for x in response.text.split("\n")]

# tirando o cabeçalho e guradando em uma variavel
header = linhas.pop(0)
csv = []

# colocando cada item de cada coluna com a key
# do seu respectivo cabeçalho
for linha in linhas:
    csv.append({header[idx]: item for idx, item in enumerate(linha)})


def b(json_format=False):
    # contagem de medalhas semelhante do exe A
    medal_count = dict(Counter([item["NOC"] for item in csv]))

    relatorio = {}

    # percorrendo cada pais e
    # retirando o valor diretamente do dicionario e botando um uma key
    # ex {"BRA": 2} vira {"BRA": {"Total de Medalhas": 2}}
    # para depois poder adicionar a lista de medalhas junto
    for key in medal_count.keys():
        relatorio[key] = {}
        relatorio[key]["Total de Medalhas"] = medal_count[key]

    # percorrendo cada pais e
    # colocando suas medalhas
    for key in relatorio.keys():
        relatorio[key]["Medalhas"] = []

        # montando a lista de medalhas percorrendo o csv
        # filtrado ja pelo pais que é a key
        for medalha in [item for item in csv if item["NOC"] == key]:
            medalha_campos = {"Esporte": medalha["Sport"],
                              "Ano": medalha["Year"],
                              "Cidade": medalha["City"],
                              "Genero": "Masculino" if medalha["Event gender"] == "M" else "Femenino"}

            relatorio[key]["Medalhas"].append(medalha_campos)

    if json_format:
        print(json.dumps(relatorio, indent=1))

    else:
        for pais in relatorio.keys():
            print("\n")
            print("%s---------------------------------------" % pais)
            print("Total de Medalhas: %d" %
                  relatorio[pais]["Total de Medalhas"])

            formato = "{:<14} {:<6} {:<10} {:<22}"
            print(formato.format('Esporte', 'Ano', "Genero", 'Cidade'))
            for medalha in relatorio[pais]["Medalhas"]:
                print(formato.format(
                    medalha['Esporte'], medalha['Ano'], medalha["Genero"], medalha['Cidade']))

            print("---------------------------------------%s" % pais)


b()


pathString = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"
conn = requests.Session().get(pathString, timeout=5)

'''if conn.status_code != 200:
    conn.raise_for_status()
else:
    print("Conectado com sucesso!")'''

getDatas = [data.split(',') for data in conn.text.split('\n')]

header = getDatas.pop(0)
lister = []

for getdata in getDatas:
    lister.append({header[index]: item for index, item in enumerate(getdata)})


def tarefa11a(jsonFormat=False):
    global medalRows
    CountMedal = dict(Counter([item["NOC"] for item in lister]))

    talkative = {}

    for keys in CountMedal.keys():
        talkative[keys] = {}
        talkative[keys]['Total de medalhas'] = CountMedal[keys]

    for keys in talkative.keys():
        talkative[keys]['Medalhas'] = []

        for medal in [item for item in lister if item['NOC'] == keys]:
            medalRows = {
                'Esporte': medal['Sport'],
                'Ano': medal['Year'],
                'Cidade': medal['City'],
                'Genero': 'Masculino' if medal['Event gender'] == 'M' else 'Feminino'
            }

        talkative[keys]['Medalhas'].append(medalRows)

        if jsonFormat:
            print(json.dumps(talkative, indent=1))

        """else:
            for country in talkative.keys():
                print('\n')
                print('%s---------------------------------------------------' % country)
                print('Total de Medalhas: %d' % talkative[country]['Total de Medalhas'])

                defaultForms = '{:<14}{:<6}{:<10}{:<22}'

                print(defaultForms.format('Esporte', 'Ano', 'Genero', 'Cidade'))

                for medals in talkative[country]['Medalhas']:
                    print(defaultForms.format(
                        medals['Esporte'], medals['Ano'], medals['Gênero'], medals['Cidade']))

                print('---------------------------------------------------%s' % country)"""


tarefa11a()

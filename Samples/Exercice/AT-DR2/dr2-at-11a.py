import requests
import json
from collections import Counter

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


tarefa11a()

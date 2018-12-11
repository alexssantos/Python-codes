import requests
from bs4 import BeautifulSoup
import re

url = "http://brasil.pyladies.com/about"
regxWord_ladies = "(:?L|l)adies"
regx_ladies = "ladies"
regx_Ladies = "Ladies"
regxWord_allWords = "\w+"


# Usando requests + Beautiful Soup
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")


def topWords(allwords):
    dictCountWords = {}

    for word in allwords:
        # already exist ?
        if word in dictCountWords:
            # print(word)
            dictCountWords[word] += 1
        else:
            dictCountWords[word] = 1
    # print(dictCountWords)
    return dictCountWords


allWords = re.findall(regxWord_allWords, soup.get_text())
# print(allWords)

topWords = topWords(allWords)

total_ladies = topWords['ladies']
total_Ladies = topWords['Ladies']

print('length topWords ladies: ', total_ladies)
print('length topWords Ladies: ', total_Ladies)
# ladies = [x for x in topWords if (topWords[LADIES] or topWords[LaDIES])]

# args: 'size=50;size=51;' =  'size=(?:50|51)'      # https://stackoverflow.com/questions/18425386/re-findall-not-returning-full-match
qtddWord_ladies = len(re.findall(
    regxWord_ladies, soup.get_text()))

qtdd_ladies = len(re.findall(
    regx_ladies, soup.get_text()))  # get Amount

qtdd_Ladies = len(re.findall(
    regx_Ladies, soup.get_text()))  # get Amount

print("com regex (:?L|l)adies :", qtddWord_ladies)
print("com regex  ladies' :", qtdd_ladies)
print("com regex  Ladies' :", qtdd_Ladies)

# RESPOSTA:
#       De acordo com o site, fazendo um find na pagina, encontramos 1 'Ladies' e 2 'ladies'

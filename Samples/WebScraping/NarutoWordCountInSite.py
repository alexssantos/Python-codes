import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict

url = "https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Naruto_Shippuden"
regxWord_Naruto = "(:?N|n)aruto"
regxWord_Sasuke = "(:?S|s)asuke"
regexAll_Words = "\w+"


def topWords(allwords):
    dictCountWords = {}
    topWords = [0, ]
    for word in allwords:
        if word in dictCountWords:                  # already exist ?
            dictCountWords[word] += 1
        else:
            dictCountWords[word] = 1
    for word in dictCountWords:                     #dict com palavras contadas
        if dictCountWords[word] >= topWords[0]:
            topWords.insert(0, dictCountWords[word])
    topScore3 = topWords[0:2]
    print('top scores: ', topScore3)    
    top3Words = [x for x, y in dictCountWords.items() if y in topScore3]     # pegar top3 words
    #for target_list in expression_list:
     
    print('top 3 scores: ', topWords)
    dictTop3 = {}
    for a in top3Words:
        dictTop3[a] = dictCountWords[a]
    print(dictTop3)
    # print(' -- ANTES de Ordenar: \n', dictCountWords)
    # dictCountWords = OrderedDict(dictCountWords)
    # for a, b in dictCountWords.items():
        # print(a, "  ", b)
    # if len(topWords) == 0:
        # for word in dictCountWords:

    # print(dictCountWords)
    # return array3TopWords   # array com 3 listas


# Usando requests + Beautiful Soup
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
topWords(soup.get_text())


# args: 'size=50;size=51;' =  'size=(?:50|51)'      # https://stackoverflow.com/questions/18425386/re-findall-not-returning-full-match
c = len(re.findall(regxWord_Naruto, soup.get_text()))   # get Amount
d = len(re.findall(regxWord_Sasuke, soup.get_text()))   # get Amount
allwords = re.findall(regexAll_Words, soup.get_text())

print("Ocorrências da palavra 'Naruto' :", c)
print("Ocorrências da palavra 'Sasuke' :", d)
# print("Todas Palavras : \n", allwords)


# LINKS
# https://stackoverflow.com/questions/36268749/remove-multiple-items-from-a-python-list-in-just-one-statement
# 
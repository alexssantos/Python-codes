import requests
from bs4 import BeautifulSoup
import re

url = "https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Naruto_Shippuden"
regxWord_Naruto = "(:?N|n)aruto"
regxWord_Sasuke = "(:?S|s)asuke"

# Usando requests + Beautiful Soup
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

def topWords(allwords):
    array3TopWords = []
    dictCountWords = {}
    for word in allwords:
        # already exist ?
        if word in dictCountWords:
            # print(word)
            dictCountWords[word] += 1
        else:
            dictCountWords[word] = 1
    print(dictCountWords)
    # return array3TopWords   # array com 3 listas

allwords = re.findall('', soup.get_text())
# topWords(allwords)

# args: 'size=50;size=51;' =  'size=(?:50|51)'      # https://stackoverflow.com/questions/18425386/re-findall-not-returning-full-match
c = len(re.findall(regxWord_Naruto, soup.get_text()))   # get Amount
d = len(re.findall(regxWord_Sasuke, soup.get_text()))   # get Amount

print("Ocorrências da palavra 'Naruto' :", c)
print("Ocorrências da palavra 'Sasuke' :", d)




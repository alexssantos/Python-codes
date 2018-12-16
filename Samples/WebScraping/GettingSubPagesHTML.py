import requests
from bs4 import BeautifulSoup

url = "https://www.tecmundo.com.br/"
url2 = "https://www.gta.ufrj.br/grad/06_1/wap/"

html = requests.get(url+"index.html").text
soup = BeautifulSoup(html, "lxml")

bodyPage = soup.html.body

# LINKS
# > find_all() - lista contendo todas as TAGs
links = bodyPage.find_all('a')

# exibir todos os titulos

# for linkTag in links:
#     print('LINK %d: ' % links.index(linkTag), linkTag.text)

# Get a atribute of TAG - TAG.get()
hrefLis = []
for linkTag in bodyPage.find_all('a'):
    hrefLis.append(linkTag.get('href'))

# print(hrefLis)

# GET SUBPAGES
subpagesHomeList = []
for link in links:
    pageUrl = link.get('href')
    try:
        pageHtml = requests.get(pageUrl).text
        soup = BeautifulSoup(pageHtml, 'lxml')
        subpagesHomeList.append(soup)

    except Exception as e:
        print(
            'ERRO Request URL \n',
            'URL: ', pageUrl, '\n',
            'Message: ', e)

    try:
        titleText = soup.html.head.title.text
    except Exception as e:
        titleText = '-- Não tem Titulo --'        
        print('Excelption: ', e)

    if titleText and titleText.strip():  # isNotNoneOrEmpty https://stackoverflow.com/a/24534152/8941680
        print('TITULO DA PAGINA: ', titleText)
    print(pageUrl, '\n')


print('qtt subpaginas da Home capturados: ', len(subpagesHomeList))

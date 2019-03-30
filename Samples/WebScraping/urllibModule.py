import urllib3

# INSTALL MODDELU
# py -m pip install urllib3

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando urllib3
http = urllib3.PoolManager()    # Instanciando o http que faz o meio de campo nas requisições http;
response = http.request('GET', url)
csv = response.data     # o parametro .data do objeto 'resposnse' tem todo o conteudo pego na requisição. 

print(csv)
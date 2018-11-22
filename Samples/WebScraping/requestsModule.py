import requests

# INSTALL MODDELU 
# py -m pip install requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text

print(csv)
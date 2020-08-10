import requests
import json
import xml.etree.ElementTree as ET

import xmltodict
import pprint

response = requests.get("https://www3.bcb.gov.br/bc_moeda/rest/moeda/data")

with open('convertjson.json') as json_file:
    responseCountry = json.load(json_file)
    #print(responseCountry[0]['C?d. Pa?s'])

dt = str(input("Digite a data de consulta:"))

jsonResponseContent = json.dumps(xmltodict.parse(response.content))

dtYear = str(dt[0:4])
dtMonth = str(dt[5:6])
dtDay = str(dt[7:8])

#print(dtYear)
#print(dtMonth)
#print(dtDay)

dtConvert = dtYear + "-" + dtMonth + "-" + dtDay
menorCotacao = 1000
codigoCotacao = 0
simboloCotacao = ''
paisCotacao = ''
nomePais = ''

#print("Json >> ", jsonResponseContent)

dataRes = json.loads(jsonResponseContent)
i = 0
for codigo in dataRes['moedas']['moeda']:
    codigo = dataRes['moedas']['moeda'][i]['codigo']
    responseCotacao = requests.get("https://www3.bcb.gov.br/bc_moeda/rest/converter/1/1/" + codigo + "/220/" + dtConvert)
    #print("resp >>", responseCotacao.content)
    #print("codigo >>> ", codigo)
    if(responseCotacao.status_code == 200):
        jsonCotacao = json.dumps(xmltodict.parse(responseCotacao.content))
        cotacaoRes = json.loads(jsonCotacao)
        cotacaoValor = cotacaoRes['valor-convertido']
        if(float(cotacaoValor) < float(menorCotacao)):
            menorCotacao = cotacaoValor
            codigoCotacao = codigo
            simboloCotacao = dataRes['moedas']['moeda'][i]['simbolo']
            paisCotacao = dataRes['moedas']['moeda'][i]['codigoPais']
    #print('valorConvertido >>>', cotacaoValor)
    i += 1

j = 0
#responseCountry = requests.get("https://ptax.bcb.gov.br/ptax_internet/consultarTabelaMoedas.do?method=consultaTabelaMoedas")
for codeCountry in responseCountry:
    codeCountry = responseCountry[j]['C?d. Pa?s']
    #print("CodeCountry ",codeCountry)
    #print("PaisCotacao ", paisCotacao)
    if(int(codeCountry) == int(paisCotacao)):
        nomePais = responseCountry[j]['Pa?s']
    j += 1
#print("pais >>> ", responseCountry.content)
#jsonCountryResponseContent = json.dumps(responseCountry.text)
#print(jsonCountryResponseContent)

#print(", Cotacao >>> ", menorCotacao, ", Pais >>> ", paisCotacao, ", Simbolo >>> ", simboloCotacao)

print(simboloCotacao, ", ", nomePais, ", ", menorCotacao)

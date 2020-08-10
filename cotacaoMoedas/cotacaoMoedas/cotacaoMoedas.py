import requests
import json
import xml.etree.ElementTree as ET

import xmltodict
import pprint

#requição para json de moedas
response = requests.get("https://www3.bcb.gov.br/bc_moeda/rest/moeda/data")

#Abrir e ler arquivo json da tabela de paises
with open('convertjson.json') as json_file:
    responseCountry = json.load(json_file)

#Entrada da data via teclado
dt = str(input("Digite a data de consulta:"))

#Response convertido de xml para json
jsonResponseContent = json.dumps(xmltodict.parse(response.content))

#Pegando os 4 primeiros digitos para o ano
dtYear = str(dt[0:4])
#Pegando os 2 digitos seguintes para o mes
dtMonth = str(dt[5:6])
#Pegando os 2 digitos seguintes para o dia
dtDay = str(dt[7:8])

#Convertendo data para novo formato
dtConvert = dtYear + "-" + dtMonth + "-" + dtDay

#Instaciando Variaveis
menorCotacao = 1000
codigoCotacao = 0
simboloCotacao = ''
paisCotacao = ''
nomePais = ''

#Carregando json do response convertido do xml
dataRes = json.loads(jsonResponseContent)

#Instaciando contador
i = 0

#Percorrendo as moedas
for codigo in dataRes['moedas']['moeda']:
    #Pegando o codigo de cada moeda
    codigo = dataRes['moedas']['moeda'][i]['codigo']
    #Requisição para pegar cotacao da moeda em relação ao dolar na data digitada
    responseCotacao = requests.get("https://www3.bcb.gov.br/bc_moeda/rest/converter/1/1/" + codigo + "/220/" + dtConvert)
    #Validando se a api responde corretamente
    if(responseCotacao.status_code == 200):
        #Convertendo response de xml para json
        jsonCotacao = json.dumps(xmltodict.parse(responseCotacao.content))
        #Carregando json da cotação convertido do xml
        cotacaoRes = json.loads(jsonCotacao)
        #Setando variavel com o valor da cotação vindo do response
        cotacaoValor = cotacaoRes['valor-convertido']
        #Verificando se o valor da menor cotação atual é maior que a cotação retornada no response
        if(float(cotacaoValor) < float(menorCotacao)):
            #Setando menorCotacao com o valor retornado no response
            menorCotacao = cotacaoValor
            #Setando codigoCotação com o codigo da moeda
            codigoCotacao = codigo
            #Setando simboloCotação com o simbolo da moeda
            simboloCotacao = dataRes['moedas']['moeda'][i]['simbolo']
            #Setando paisCotação com o codigo do pais
            paisCotacao = dataRes['moedas']['moeda'][i]['codigoPais']
    #Aumentando o contador
    i += 1

#Instaciando contador para pais
j = 0
#Percorrendo paises
for codeCountry in responseCountry:
    #Pegando o codigo do pais
    codeCountry = responseCountry[j]['C?d. Pa?s']
    #Verificando se o valor do codigo do pais é igual ao codigo do pais da cotacao da menor moeda em relação ao dolar
    if(int(codeCountry) == int(paisCotacao)):
        #Setando o nome do pais
        nomePais = responseCountry[j]['Pa?s']
    #Aumentando Contador Pais
    j += 1

#Printando resultados

print(simboloCotacao, ", ", nomePais, ", ", menorCotacao)

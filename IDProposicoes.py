import requests
import re
import pprint
import json

#Funcao para criar listas baseadas em arquivos .txt
#Parametro1 = nome do arquivo .txt
#Parametro2 = List de destino dos elementos do arquivo .txt
def getlista(txtfile, lista):
  #Loop para iterar linhas dentro do arquivo .txt
  for i in txtfile:
    #Retira caracter especial da string
    i = i.replace("\n", "")
    #Adiciona a linha ao final da lista
    lista.append(i)

#URL da API da camara
#O r antes da string funciona para escapar os elementos especiais da String
#URL dividida em indices para composicao de cada requisicao
URL = [r'https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=',r'&numero=',r'&ano=', r'&ordem=ASC&ordenarPor=id']

#Comando para abertura de arquivos .txt em modo de leitura
fileType = open("type.txt","r")
fileNo = open("no.txt","r")
fileYear = open("year.txt","r")

tipo = [] #Lista para armazenar tipo da proposicao
no = [] #Lista para armazenar numero da proposicao
ano = [] #Lista para armazenar o ano da proposicao
codigo = [] #Lista para armazenar o codigo id buscado na requisicao

#Utilizacao da funcao getlista para transformar os arquivos .txt em listas
getlista(fileType, tipo)
getlista(fileNo, no)
getlista(fileYear, ano)
fileType.close()
fileNo.close()
fileYear.close()

#Loop para gerar numero de requisicoes igual ao numero de elementos nas listas
for i in range(len(tipo)):
  #Composicao da URL para a busca
  requisicao = requests.get(URL[0] + tipo[i] + URL[1] + no[i] + URL[2] + ano[i] + URL[3])
  #Resgate do texto resultado da requisicao
  requisicao = requisicao.text
  #Comando para transformar texto da requisicao em um Dicionario
  requisicao = json.loads(requisicao)
  #Adiciona o elemento especificado na Lista Codigo
  codigo.append(requisicao['dados'][0]['id'])

#Criacao de arquivo .txt contendo o id das proposicoes
fileId = open("IdProposicao.txt", "w")
fileId.write(codigo)
fileId.close()


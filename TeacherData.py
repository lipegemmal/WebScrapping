from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import json

Dicionario = dict(dict())


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h2
    except AttributeError as e:
        return None
    return title


def setNames(nameList):
    for name in nameList:
        print(name)
        Dicionario[name.get_text()] = None


def getNames(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    #try:
    bsObj = BeautifulSoup(html.read(), "lxml")
    nameList = bsObj.findAll("td", {"class": "views-field views-field-title active"})
    setNames(nameList)


def getData(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    #try:
    bsObj = BeautifulSoup(html.read(), "lxml")
    classList = bsObj.findAll("td", {"class": "views-field views-field-title active"})
    
    for name in classList:
        nome = str(name.get_text())[1:]
        link = re.search("/node/[0-9]*", str(name))
        Dicionario[nome] = {}
        Dicionario[nome]['Nome'] = nome
        Dicionario[nome]['Link'] = "www.inf.ufg.br"+link.group() 
    
    return classList


linkList = getData("http://www.inf.ufg.br/docentes")

#for link in linkList:
#        #print(str(link))
#        x = re.search("/node/[0-9]*",str(link))
#        print(x.group())
#        print()

#print(*Dicionario,sep="\n")
#print(list(Dicionario))

for tupla in Dicionario:
    print (Dicionario[tupla])
   #x =list(tupla.values())
   # print(x)

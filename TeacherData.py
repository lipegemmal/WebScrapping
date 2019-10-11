from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

Dicionario = {

}



def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body.h2  
    except AttributeError as e:
        return None
    return title


def getGreen(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    #try:
    bsObj = BeautifulSoup(html.read(),"lxml")
    nameList = bsObj.findAll("td", {"class" : "views-field views-field-title active"})
    return nameList
    
    #for name in nameList:
     #   print(name.get_text())


#title = getTitle("http://www.inf.ufg.br")
 
#if title == None:
#    print("No title")
#else:
#    print(title)

nameList = getGreen("http://www.inf.ufg.br/docentes")
for name in nameList:
        Dicionario[name.get_text()] = None
        
#print("bu")
print(*Dicionario.keys())

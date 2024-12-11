from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import json
import random
import time
import requests
import tqdm

URL_BASE_EQUIPOS = "https://www.dofus-touch.com/es/mmorpg/enciclopedia/equipos?page="
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
URL_CORE = "https://www.dofus-touch.com"

for numero_pagina in tqdm.tqdm(range(66,87)):
    #Escribimos por página
    diccionario={}
    
    page = requests.get(URL_BASE_EQUIPOS+str(numero_pagina), headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")
    link= str(soup.find_all("span", {"class": "ak-linker"}))
    matches = re.findall(r"<a.*?>", link)
    
    lista_links=[]
    for match in matches:
        link = re.findall(r"\".*?\"",match)
        if link not in lista_links:
            lista_links.append(link[0].replace('"',""))
    lista_links=list(set(lista_links))

    for link in tqdm.tqdm(lista_links):
        full_link=URL_CORE+link
        page = requests.get(full_link,headers=HEADERS)
        soup = BeautifulSoup(page.text, "html.parser")
        
        div_tipo = str(soup.find_all("div", {"class": "ak-encyclo-detail-type"}))
        tipo=re.findall(r"span>(.*?)</span", div_tipo, flags=re.DOTALL)
        
        div_nivel = str(soup.find_all("div", {"class": "ak-encyclo-detail-level"}))
        nivel=re.findall(r"text-right\">(.*?)<", div_nivel, flags=re.DOTALL)
        
        info= str(soup.find_all("div", {"class": "ak-list-element"}))
        matches = re.findall(r"title\">(.*?)<", info, flags=re.DOTALL)
        stats=[]
        for match in matches:
            stat=match.strip("\n").strip()
            if stat:
                stats.append(stat)
        stats.append(nivel)
        stats.append(tipo)
        nombre=" ".join(link.split("/")[-1].split("-")[1:])
        diccionario[nombre]=stats
        time.sleep(random.uniform(5, 10))
        
    with open("Storage/output.json", "a") as file:
        json.dump(diccionario, file, indent=4)
        
    with open("Storage/ultima_pagina.txt","w") as file:
        file.write(str(numero_pagina))
        
    time.sleep(random.uniform(30,60))
    
    
    

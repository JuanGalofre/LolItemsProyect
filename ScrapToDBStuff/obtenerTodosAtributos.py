import json
import re

    
def is_integer(s):
    try:
        s=s.strip()
        if "%" in s:
            s=s.replace("%","")
        int(s)
        return True
    except ValueError:
        return False

def convertir_porcentaje_a_porcentual(string:str) -> str:
    PATTERN = r"([\d])(%)"
    if re.search(PATTERN,string):
        string = re.sub(PATTERN,r"\1 ",string)
        string = string + " porcentual"
    return string

def arreglar_lista_de_atributos(lista_de_atributos:list) -> list:
    if lista_de_atributos:
        for index in range(len(lista_de_atributos)):
            lista_de_atributos[index] = convertir_porcentaje_a_porcentual(lista_de_atributos[index])
    return lista_de_atributos

def revisar_diccionario_por_atributos_vacios(diccionario:dict):
    for key,value in diccionario.items():
        if not value['atributos']:
            """ print(key) """
            
def generar_objetos_con_atributos() -> dict:
    with open("objetos.json", "r") as file:
        data = json.load(file)

    for key,value in data.items():
        lista_de_atributos = value['atributos']
        lista_de_atributos = arreglar_lista_de_atributos(lista_de_atributos)
        value['atributos'] = lista_de_atributos
        
    return data

def corregir_atributos_con_base_a_lista(lista_de_atributos,lista_de_atributos_disponibles) -> list:
    atributos_disponibles = dict()
    for atributo in lista_de_atributos:
        for atributo_disponible in lista_de_atributos_disponibles:
            if re.search(re.compile(r"\d\s*"+re.escape(atributo_disponible)+r"$"),atributo):
                atributos_disponibles[atributo_disponible]=atributo.replace(atributo_disponible,"").strip()
    return atributos_disponibles


def generar_atributos() -> list:
    
    data = generar_objetos_con_atributos()
    frecuenario=dict()
    for key,value in data.items():
        for linea in value["atributos"]:
            palabras = linea.split()
            palabras_invertidas= palabras[::-1]
            primer_digito=""
            for palabra in palabras_invertidas:
                if is_integer(palabra):
                    primer_digito=palabra
                    break
            if primer_digito:
                index=palabras.index(primer_digito)
                supuesto_atributo = " ".join(palabras[index+1:])
                #No tenemos encuenta los requerimientos
                if supuesto_atributo not in frecuenario:
                    frecuenario[supuesto_atributo]=1
                else:
                    frecuenario[supuesto_atributo] += 1
            else:
                continue
    #filttramos hasta 60

    lista_de_atributos= []

    for key,value in frecuenario.items():
        if value > 59:
            lista_de_atributos.append(key)

    lista_de_atributos_limpia = [item for item in lista_de_atributos if item != '']

    return lista_de_atributos_limpia


def generar_objetos_con_atributos_limpios():
    diccionario_de_objetos_con_atributos = generar_objetos_con_atributos()
    lista_de_atributos_limpios = generar_atributos()
    
    for key,value in diccionario_de_objetos_con_atributos.items():
        lista_de_atributos = value['atributos']
        lista_de_atributos = corregir_atributos_con_base_a_lista(lista_de_atributos,lista_de_atributos_limpios)
        value['atributos'] = lista_de_atributos
    
    return diccionario_de_objetos_con_atributos
        
generar_objetos_con_atributos_limpios()


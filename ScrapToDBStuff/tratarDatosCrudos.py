import json
import unidecode
def devolver_atributos_unidecode(lista_atributos:list):
    return [unidecode.unidecode(x) for x in lista_atributos]

def devolver_nivel_en_int(string:str):
    return int(string.split(":")[-1].strip())

def tratar_datos_crudos(diccionario_crudo:dict):
    diccionario_limpio=dict()
    for key,value in diccionario_crudo.items():
        #Retiramos emblemas
        if (not key in diccionario_limpio) and ("emblema" not in key):
            try:
                diccionario_limpio[key]={"tipo":unidecode.unidecode(value[-1][0]),
                                         "nivel":devolver_nivel_en_int(value[-2][0]),
                                         "atributos":devolver_atributos_unidecode(value[:-2])}
            except:
                print(key,value)
                quit()    
    return diccionario_limpio


with open("Storage/output.json", "r") as file:
    data = json.load(file)

diccionario_limpio = tratar_datos_crudos(data)

with open("Storage7objetos.json", "w") as file:
    json.dump(diccionario_limpio, file, indent=4)

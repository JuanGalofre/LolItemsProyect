import SessionAdmin
from Models.CentralModels import Atributo, Objeto, Valor
import ScrapToDBStuff.obtenerTodosAtributos as obtenerTodosAtributos

session = SessionAdmin.generate_session()

diccionario_de_objetos_con_atributos = obtenerTodosAtributos.generar_objetos_con_atributos_limpios()
def limpiar_string_y_devolver_numero(string) -> str:
    return int(string.strip().replace("  ","").replace(" ",""))

def obtener_maximo(string) -> int:
    return limpiar_string_y_devolver_numero(string.split("a")[1])

def obtener_minimo(string) -> int:
    return limpiar_string_y_devolver_numero(string.split("a")[0])

def tratar_valores(string) -> dict:
    if "a" in string:
        return {'minimo':obtener_minimo(string),'maximo':obtener_maximo(string),'valor':obtener_maximo(string)}
    else:
        return {'minimo':None,'maximo':None,'valor':limpiar_string_y_devolver_numero(string)}

for key,value in diccionario_de_objetos_con_atributos.items():
    nuevo_objeto = Objeto(nombre=key, tipo=value['tipo'], nivel=value['nivel'])
    session.add(nuevo_objeto)
    for nombre_atributo, valor in value['atributos'].items():
        atributo = session.query(Atributo).filter_by(nombre=nombre_atributo).first()
        valores = tratar_valores(valor)
        valor = Valor(objeto=nuevo_objeto, atributo=atributo, valor=valores['valor'], maximo=valores['maximo'], minimo=valores['minimo'])
        session.add(valor)
SessionAdmin.try_save_and_close_session(session)
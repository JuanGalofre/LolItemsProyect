import ScrapToDBStuff.obtenerTodosAtributos as obtenerTodosAtributos
import SessionAdmin
from Models.CentralModels import Atributo

session = SessionAdmin.generate_session()

lista_atributos = obtenerTodosAtributos.generar_atributos()
for atributo in lista_atributos:
    nuevo_atributo = Atributo(nombre = atributo)
    session.add(nuevo_atributo)

SessionAdmin.try_save_and_close_session(session)

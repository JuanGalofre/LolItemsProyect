import SessionAdmin
import Models.CentralModels as CM



#La sesion es la que se utilizar para realizar las llamadas a la DB.
session = SessionAdmin.generate_session()

#Query basica 1
capas = session.query(CM.Objeto).filter(CM.Objeto.nombre.ilike("%Capa%")).all()
""" print(capas) """
#Utilizo el metodo que se definió en Objeto para cambiar de objeto a dict
capas = [capa.to_dict() for capa in capas]
""" print(capas) """

#Query basica 2
stuffs= session.query(CM.Atributo).filter_by(nombre = "vitalidad").all()
vitalidad = [stuff.to_dict() for stuff in stuffs]
""" print(vitalidad) """

#Query basica 3

objeto = session.query(CM.Objeto).filter(CM.Objeto.id == 1).first()
# Acceder a los valores relacionados
for valor in objeto.valores:
    print(f"Atributo: {valor.atributo.nombre}, Valor: {valor.valor}, Máximo: {valor.maximo}, Mínimo: {valor.minimo}")
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .CentralModels import Base

class Valor(Base):
    __tablename__ = 'objeto_atributo'
    
    objeto_id = Column(Integer, ForeignKey('objeto.id'), primary_key=True)
    atributo_id = Column(Integer, ForeignKey('atributo.id'), primary_key=True)
    
    valor = Column(Integer, nullable=False)
    maximo = Column(Integer, nullable=True)
    minimo = Column(Integer, nullable=True)
    
    # Bidirectional relationships
    objeto = relationship("Objeto", back_populates="valores")
    atributo = relationship("Atributo", back_populates="valores")

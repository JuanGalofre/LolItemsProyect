from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .CentralModels import Base

class Atributo(Base):
    __tablename__ = 'atributo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
    
    
    # Many-to-many relationship with Objeto
    objetos = relationship(
        "Objeto",
        secondary="objeto_atributo",  # Use the association table name
        back_populates="atributos",
        viewonly=False  # Ensure write access
    )
    
    # Relationship with Valor
    valores = relationship("Valor", back_populates="atributo")
    
    

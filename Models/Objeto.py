from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .CentralModels import Base


class Objeto(Base):
    __tablename__ = 'objeto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    nivel = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            'nivel':self.nivel,
            'tipo':self.tipo
        }
    
    
    # Many-to-many relationship with Atributo
    atributos = relationship(
        "Atributo",
        secondary="objeto_atributo",  # Use the association table name
        back_populates="objetos",
        viewonly=False  # Ensure write access
    )
    
    # Relationship with Valor
    valores = relationship("Valor", back_populates="objeto")

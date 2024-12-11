from sqlalchemy.ext.declarative import declarative_base

# Declare the base class for models
Base = declarative_base()

# Optionally import models here to ensure they are registered
from .Atributo import Atributo
from .Objeto import Objeto
from .Valor import Valor

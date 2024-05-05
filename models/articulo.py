from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Articulo(BaseModel):
    id: Optional[int] = None
    titulo: str
    autor: str
    contenido: str
    creado: datetime
    categoria: str

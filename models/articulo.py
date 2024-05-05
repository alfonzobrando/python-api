from pydantic import BaseModel
from typing import Optional
from typing import Text


class Articulo(BaseModel):
    id: Optional[str] = None
    titulo: str
    autor: str
    contenido: Text
    categoria: str

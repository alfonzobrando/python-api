from fastapi import APIRouter, HTTPException, status
from models.articulo import Articulo
from uuid import uuid4 as uuid;


router = APIRouter()

articulos = [
    {
        "id": str(uuid()),
        "titulo": "Python",
        "autor": "Alfonzo",
        "contenido": "Mi primera API con FastAPI",
        "categoria": "Backend"
    },
    {
        "id": str(uuid()),
        "titulo": "FastAPI",
        "autor": "Alfonzo Brando",
        "contenido": "CRUD con FastAPI",
        "categoria": "Web"
    }
]

@router.get('/articulos')
def get_articulos():
    return articulos

@router.get('/articulos/{id}')
def get_articulo(id: str):
    # return list(filter(lambda item: item['id'] == id, articulos)) -> Otra forma
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    raise HTTPException(status_code=404, detail="Articulo Not Found")


@router.post('/articulos', status_code=status.HTTP_201_CREATED)
def create_articulo(articulo: Articulo):
    articulo.id = str(uuid())
    articulos.append(articulo.model_dump())
    return articulos[-1]


@router.put('/articulos/{id}')
def update_articulo(id: str, articulo: Articulo):
    for index, item in enumerate(articulos):
        if item['id'] == id:
            articulos[index]['titulo'] = articulo.titulo
            articulos[index]['autor'] = articulo.autor
            articulos[index]['contenido'] = articulo.contenido
            articulos[index]['categoria'] = articulo.categoria
    return articulos


@router.delete('/articulos/{id}')
def delete_articulo(id: str):
    for item in articulos:
        if item['id'] == id:
            articulos.remove(item)
    return articulos
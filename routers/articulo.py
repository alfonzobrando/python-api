from fastapi import APIRouter

from models.articulo import Articulo

router = APIRouter()

articulos = [

]

@router.get('/articulos')
def get_articulos():
    return articulos

@router.get('/articulos/{id}')
def get_articulo(id: int):
    return list(filter(lambda item: item['id'] == id, articulos))


@router.post('/articulos')
def create_articulo(articulo: Articulo):
    articulos.append(articulo)
    return articulos

@router.put('/articulos/{id}')
def update_articulo(id: int, articulo: Articulo):
    for index, item in enumerate(articulos):
        if item['id'] == id:
            articulos[index]['titulo'] = articulo.titulo
            articulos[index]['autor'] = articulo.autor
            articulos[index]['contenido'] = articulo.contenido
            articulos[index]['creado'] = articulo.creado
            articulos[index]['categoria'] = articulo.categoria
    return articulos


@router.delete('/articulos/{id}')
def delete_articulo(id: int):
    for item in articulos:
        if item['id'] == id:
            articulos.remove(item)
    return articulos
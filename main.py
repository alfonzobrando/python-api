from fastapi import FastAPI
from routers.articulo import router as articulo_router

app = FastAPI()
app.include_router(articulo_router)


@app.get('/')
def root():
    return { "welcome": "welcome to REST API" }
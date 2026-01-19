from .utils_texto import normalizar

catalogo = {}

def crear(titulo, anio, generos):
    clave = normalizar(titulo)
    catalogo[clave] = {
        "titulo": titulo,
        "anio": anio,
        "genero": set(generos)
    }

def leer():
    return catalogo

def actualizar(titulo,ob=None):
    clave = normalizar(titulo)
    if clave in catalogo and ob:
        catalogo[clave].update(ob)

def eliminar(titulo):
    catalogo.pop(normalizar(titulo), None)

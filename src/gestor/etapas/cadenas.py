from .tuplas import obtener_videojuegos
from ..utils_texto import normalizar

def buscar_videojuego():
    nombre = input("Nombre del videojuego: ")
    clave = normalizar(nombre)

    for titulo, anio, genero in obtener_videojuegos():
        if normalizar(titulo) == clave:
            print(f"Título: {titulo} | Género: {genero} | Año: {anio}")
            return

    print("Videojuego no encontrado")

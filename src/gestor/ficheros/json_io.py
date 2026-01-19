import json
from ..utils_texto import normalizar


def guardar_json(nombre_fichero, catalogo):
    serializable = {}

    for k, v in catalogo.items():
        serializable[k] = {
            "titulo": v["titulo"],
            "anio": v["anio"],
            "genero": list(v["genero"])
        }

    with open(nombre_fichero, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=4, ensure_ascii=False)


def cargar_json(nombre_fichero):
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        data = json.load(f)

    catalogo = {}
    for k, v in data.items():
        catalogo[k] = {
            "titulo": v["titulo"],
            "anio": v["anio"],
            "genero": set(v["genero"])
        }

    return catalogo

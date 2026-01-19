import csv
from ..utils_texto import normalizar


def guardar_csv(nombre_fichero, catalogo):
    with open(nombre_fichero, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["titulo", "anio", "generos"])

        for v in catalogo.values():
            writer.writerow([
                v["titulo"],
                v["anio"],
                ";".join(v["genero"])
            ])


def cargar_csv(nombre_fichero):
    catalogo = {}

    with open(nombre_fichero, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            clave = normalizar(fila["titulo"])
            catalogo[clave] = {
                "titulo": fila["titulo"],
                "anio": int(fila["anio"]),
                "genero": set(fila["generos"].split(";"))
            }

    return catalogo

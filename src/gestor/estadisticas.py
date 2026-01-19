def total_videojuegos(cat):
    return len(cat)

def conteo_por_genero(cat):
    resultado = {}
    for v in cat.values():
        for g in v["genero"]:
            resultado[g] = resultado.get(g, 0) + 1
    return resultado

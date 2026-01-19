from .utils_texto import normalizar

def buscar_exacto(cat, titulo):
    return cat.get(normalizar(titulo))

def buscar_parcial(cat, texto):
    texto = normalizar(texto)
    return [
        v for k, v in cat.items()
        if texto in k
    ]

def buscar_por_genero(cat, genero):
    return [v for v in cat.values() if genero in v["genero"]]

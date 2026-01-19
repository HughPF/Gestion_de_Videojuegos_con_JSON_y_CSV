def etapa_conjuntos():
    generos = {"Rol", "Plataformas", "Acción"}

    generos.add("Aventura")
    generos.discard("Plataformas")

    favorito = input("Género favorito: ")
    print("Está en tu lista" if favorito in generos else "No está")

    amigo = {"Rol", "Estrategia"}

    print("Unión:", generos | amigo)
    print("Intersección:", generos & amigo)
    print("Diferencia:", generos - amigo)

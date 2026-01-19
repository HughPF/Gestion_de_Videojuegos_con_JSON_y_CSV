def obtener_videojuegos():
    return [
        ("The Legend of Zelda", 1986, "Rol"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("Final Fantasy VII", 1997, "Rol"),
        ("The Witcher 3", 2015, "Rol")
    ]


def etapa_tuplas():
    for titulo, anio, genero in obtener_videojuegos():
        print(f"{titulo} ({anio}) {genero}")

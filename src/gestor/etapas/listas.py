def etapa_listas():
    videojuegos = [
        "The Legend of Zelda",
        "Super Mario Bros",
        "Final Fantasy VII",
        "Minecraft",
        "The Witcher 3"
    ]

    videojuegos.append("Elden Ring")
    videojuegos.insert(2, "Dark Souls")
    videojuegos.remove("Minecraft")

    print("\nLista de videojuegos:")
    for i, v in enumerate(videojuegos, start=1):
        print(f"{i}. {v}")

    print("\nOrdenados alfabéticamente:")
    for v in sorted(videojuegos):
        print(v)
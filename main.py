from src.gestor import (
    crear,
    leer,
    eliminar,
    buscar_exacto,
    total_videojuegos
)

def menu():
    print("""
1. Añadir videojuego
2. Buscar videojuego
3. Listar catálogo
4. Eliminar videojuego
5. Estadísticas
0. Salir
""")

while True:
    menu()
    opcion = input("Opción: ")

    if opcion == "1":
        t = input("Título: ")
        a = int(input("Año: "))
        g = input("Géneros (coma): ").split(",")
        crear(t, a, g)

    elif opcion == "2":
        t = input("Título: ")
        print(buscar_exacto(leer(), t))

    elif opcion == "3":
        for v in leer().values():
            print(v)

    elif opcion == "4":
        eliminar(input("Título: "))

    elif opcion == "5":
        print("Total:", total_videojuegos(leer()))

    elif opcion == "0":
        break

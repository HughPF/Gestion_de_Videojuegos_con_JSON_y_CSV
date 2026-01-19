from src.gestor import (
    crear, leer, eliminar,
    buscar_exacto,
    total_videojuegos,
    guardar_csv, cargar_csv,
    guardar_json, cargar_json
)

catalogo_global = {}

def menu():
    print("""
1. Añadir videojuego
2. Buscar videojuego
3. Listar catálogo
4. Eliminar videojuego
5. Guardar CSV
6. Cargar CSV
7. Guardar JSON
8. Cargar JSON
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
        nombre = input("Nombre del fichero CSV: ")
        guardar_csv(nombre, leer())

    elif opcion == "6":
        nombre = input("Nombre del fichero CSV: ")
        datos = cargar_csv(nombre)
        for k, v in datos.items():
            catalogo_global[k] = v

    elif opcion == "7":
        nombre = input("Nombre del fichero JSON: ")
        guardar_json(nombre, leer())

    elif opcion == "8":
        nombre = input("Nombre del fichero JSON: ")
        datos = cargar_json(nombre)
        for k, v in datos.items():
            catalogo_global[k] = v

    elif opcion == "0":
        break

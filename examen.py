# Inicializamos una lista vacía para almacenar los nombres
nombres = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar nombre")
    print("2. Eliminar nombre")
    print("3. Mostrar lista de nombres")
    print("4. Salir")

while True:
    mostrar_menu()
    
    # Solicitamos la opción al usuario
    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == "1":
        # Agregar un nombre
        nombre = input("Ingresa un nombre: ")
        nombres.append(nombre)
        print(f"{nombre} ha sido agregado a la lista.")
    elif opcion == "2":
        # Eliminar un nombre
        nombre = input("Ingresa el nombre que deseas eliminar: ")
        if nombre in nombres:
            nombres.remove(nombre)
            print(f"{nombre} ha sido eliminado de la lista.")
        else:
            print(f"{nombre} no se encuentra en la lista.")
    elif opcion == "3":
        # Mostrar la lista de nombres
        print("Lista de nombres:")
        for nombre in nombres:
            print(nombre)
    elif opcion == "4":
        # Salir del programa
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1, 2, 3, o 4).")

    # Pregunta al usuario si desea regresar al menú principal o salir
    continuar = input("¿Deseas regresar al menú principal (Sí/No)? ").strip().lower()
    if continuar != "si":
        print("Saliendo del programa.")
        break
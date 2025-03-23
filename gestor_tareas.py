import json 

# Lista donde almacenarán las tareas
tareas = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n🎯  Gestor de Tareas")
    print("1️⃣  Agregar tarea")
    print("2️⃣  Ver tareas")
    print("3️⃣  Eliminar tarea")
    print("4️⃣  Salir")

# Función principal
def main():
  
  while True:
    mostrar_menu()
    opcion = input("Selecciona un opcion:  ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("Saliendo del gestor. ¡Hasta pronto!")
        break
    else:
        print("⛔ Opción no válido. Intenta de nuevo.")



# Función Agregar Tarea
def agregar_tarea():
    tarea = input("Escribe la nueva tarea:")
    tareas.append(tarea)
    guardar_tareas()
    print(f"✅ Tarea '{tarea}' agregada con éxito.")


# Función Ver Tareas
def ver_tareas():
    if not tareas:
        print("📫  No hay tareas pendientes.")
    else:
        print("\n📋  Lista de tareas: ")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")



# Función Eliminar Tarea
def eliminar_tarea():
    ver_tareas()
    try:
        indice = int(input("⛔  Ingresa el número de la tarea a eliminar:  ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            guardar_tareas()
            print(f"🗑️   Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("⚠️  Número fuera de rango.")
    except ValueError:
        print("⚠️  Ingresa un número válido.")


# Guardar tareas en un archivo JSON
def guardar_tareas():
    with open("tareas.json", "w") as file:
        json.dump(tareas, file)

# Cargar tareas desde el archivo JSON
def cargar_tareas():
    global tareas

    try:
        with open("tareas.json", "r") as file:
            tareas = json.load(file)
    except FileNotFoundError:
        tareas = []

# Iniciar el programa
if __name__ == "__main__":
    cargar_tareas()
    main()
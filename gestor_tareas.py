import json 
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

# Lista donde almacenarán las tareas
tareas = []

# Función para mostrar el menú
def mostrar_menu():
    print(Fore.BLUE + Style.BRIGHT + "\n🎯   Gestor de Tareas" + Style.RESET_ALL)
    print(Fore.CYAN +  "1️⃣   Agregar tarea" + Style.RESET_ALL)
    print(Fore.CYAN +  "2️⃣   Ver tareas" + Style.RESET_ALL)
    print(Fore.CYAN +  "3️⃣   Eliminar tarea" + Style.RESET_ALL)
    print(Fore.CYAN +  "4️⃣   Salir" + Style.RESET_ALL)

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
        print(Fore.GREEN + Style.BRIGHT + "Saliendo del gestor. ¡Hasta pronto! 👋" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "⛔ Opción no válido. Intenta de nuevo." + Style.RESET_ALL)



# Función Agregar Tarea
def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")

    # Valida que no este vacia o solo contenga espacios en blanco.
    if not tarea.strip():
        print(Fore.RED + "⚠️ No puedes agregar una tarea vacía." + Style.RESET_ALL)
        return
    
    # Fecha de creacion  y fecha de vencimiento.
    fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fecha_vencimiento = input("📅  Ingresa fecha de vencimiento (YYYY-MM-DD) o presionar Enter para omitir: ")

    # Validar fecha de vencimiento o si no coloca fecha indicar el valor de "Sin fecha"
    if fecha_vencimiento.strip() == "":
        fecha_vencimiento = "Sin fecha"
    
    
    # Guardamos la tarea con fechas en el JSON 
    tareas.append({"tarea": tarea, "creado": fecha_creacion, "vence": fecha_vencimiento})
    guardar_tareas()
    print(Fore.GREEN + Style.BRIGHT +f"✅ Tarea '{tarea}' agregada con éxito. (creada el {fecha_creacion})" + Style.RESET_ALL)


# Función Ver Tareas
def ver_tareas():
    if not tareas:
        print(Fore.RED + "📫  No hay tareas pendientes." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "\n📋  Lista de tareas: " + Style.RESET_ALL)
        for i, t in enumerate(tareas, start=1):
            print(Fore.CYAN + f"{i}. 📝 {t['tarea']} (📅 Creado: {t['creado']} - ⌛ Vence: {t['vence']})" + Style.RESET_ALL)



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
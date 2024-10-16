# equipos.py

equipos = {}

def registrar_equipo():
    nombre = input("Ingrese el nombre del equipo: ")
    if nombre in equipos:
        print("El equipo ya existe.")
        return
    
    equipos[nombre] = {
        "cuerpo_tecnico": {},
        "jugadores": {},
        "estadisticas": {
            "partidos_jugados": 0,
            "partidos_ganados": 0,
            "partidos_perdidos": 0,
            "partidos_empatados": 0,
            "goles_favor": 0,
            "goles_contra": 0,
            "puntos": 0
        }
    }
    print(f"Equipo {nombre} registrado exitosamente.")

def registrar_cuerpo_tecnico():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return
    
    rol = input("Ingrese el rol (Técnico/Asistente técnico/Preparador físico/Médico): ")
    nombre = input(f"Ingrese el nombre del {rol}: ")
    equipos[nombre_equipo]["cuerpo_tecnico"][rol] = nombre
    print(f"{rol} {nombre} registrado para el equipo {nombre_equipo}.")

def ver_equipos():
    if not equipos:
        print("No hay equipos registrados.")
        return
    
    for nombre, datos in equipos.items():
        print(f"\nEquipo: {nombre}")
        print("Cuerpo técnico:")
        for rol, nombre_miembro in datos["cuerpo_tecnico"].items():
            print(f"  {rol}: {nombre_miembro}")
        print(f"Jugadores: {len(datos['jugadores'])}")
        print("Estadísticas:")
        for stat, valor in datos["estadisticas"].items():
            print(f"  {stat}: {valor}")

def menu_equipos():
    while True:
        print("\n--- Gestión de Equipos ---")
        print("1. Registrar equipo")
        print("2. Registrar cuerpo técnico")
        print("3. Ver equipos")
        print("4. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrar_equipo()
            elif opcion == 2:
                registrar_cuerpo_tecnico()
            elif opcion == 3:
                ver_equipos()
            elif opcion == 4:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")   
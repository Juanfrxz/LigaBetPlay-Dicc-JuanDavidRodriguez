# jugadores.py
from equipos import equipos

def registrar_jugador():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return
    
    nombre = input("Ingrese el nombre del jugador: ")
    dorsal = input("Ingrese el número dorsal: ")
    posicion = input("Ingrese la posición de juego: ")
    
    equipos[nombre_equipo]["jugadores"][dorsal] = {
        "nombre": nombre,
        "posicion": posicion,
        "estadisticas": {
            "goles": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "faltas": 0
        }
    }
    print(f"Jugador {nombre} registrado para el equipo {nombre_equipo}.")

def ver_jugadores():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return
    
    jugadores = equipos[nombre_equipo]["jugadores"]
    if not jugadores:
        print(f"No hay jugadores registrados para el equipo {nombre_equipo}.")
        return
    
    print(f"\nJugadores del equipo {nombre_equipo}:")
    for dorsal, datos in jugadores.items():
        print(f"Dorsal: {dorsal}")
        print(f"  Nombre: {datos['nombre']}")
        print(f"  Posición: {datos['posicion']}")
        print("  Estadísticas:")
        for stat, valor in datos['estadisticas'].items():
            print(f"    {stat}: {valor}")
        print()

def registrar_eventos_jugador():
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    if nombre_equipo not in equipos:
        print("El equipo no existe.")
        return

    dorsal = input("Ingrese el número dorsal del jugador: ")
    if dorsal not in equipos[nombre_equipo]["jugadores"]:
        print("El jugador no existe.")
        return

    jugador = equipos[nombre_equipo]["jugadores"][dorsal]

    print(f"\nRegistrando eventos para {jugador['nombre']} del equipo {nombre_equipo}")
    
    try:
        goles = int(input("Número de goles: "))
        tarjetas_amarillas = int(input("Número de tarjetas amarillas: "))
        tarjetas_rojas = int(input("Número de tarjetas rojas: "))
        faltas = int(input("Número de faltas: "))

        jugador["estadisticas"]["goles"] += goles
        jugador["estadisticas"]["tarjetas_amarillas"] += tarjetas_amarillas
        jugador["estadisticas"]["tarjetas_rojas"] += tarjetas_rojas
        jugador["estadisticas"]["faltas"] += faltas

        print("\nEventos registrados:")
        if goles > 0:
            print(f"  Goles: {goles}")
        if tarjetas_amarillas > 0:
            print(f"  Tarjetas amarillas: {tarjetas_amarillas}")
        if tarjetas_rojas > 0:
            print(f"  Tarjetas rojas: {tarjetas_rojas}")
        if faltas > 0:
            print(f"  Faltas: {faltas}")

    except ValueError:
        print("Por favor, ingrese números válidos para todos los campos.")

def menu_jugadores():
    while True:
        print("\n--- Gestión de Jugadores ---")
        print("1. Registrar jugador")
        print("2. Ver jugadores de un equipo")
        print("3. Registrar eventos de jugador")
        print("4. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrar_jugador()
            elif opcion == 2:
                ver_jugadores()
            elif opcion == 3:
                registrar_eventos_jugador()
            elif opcion == 4:
                
                break  
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
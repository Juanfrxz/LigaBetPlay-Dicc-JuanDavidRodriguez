# estadisticas.py
from equipos import equipos

def equipo_mas_goles():
    if not equipos:
        return "No hay equipos registrados."
    
    max_goles = max(equipos.items(), key=lambda x: x[1]['estadisticas']['goles_favor'])
    return f"El equipo que más goles ha marcado es {max_goles[0]} con {max_goles[1]['estadisticas']['goles_favor']} goles."

def equipo_mas_goles_contra():
    if not equipos:
        return "No hay equipos registrados."
    
    max_goles_contra = max(equipos.items(), key=lambda x: x[1]['estadisticas']['goles_contra'])
    return f"El equipo que más goles ha recibido es {max_goles_contra[0]} con {max_goles_contra[1]['estadisticas']['goles_contra']} goles en contra."

def equipo_ultimo_puesto():
    if not equipos:
        return "No hay equipos registrados."
    
    ultimo = min(equipos.items(), key=lambda x: x[1]['estadisticas']['puntos'])
    return f"El equipo en último lugar es {ultimo[0]} con {ultimo[1]['estadisticas']['puntos']} puntos."

def jugador_mas_faltas():
    max_faltas = 0
    jugador_max_faltas = None
    equipo_max_faltas = None

    for nombre_equipo, datos_equipo in equipos.items():
        for dorsal, jugador in datos_equipo['jugadores'].items():
            if jugador['estadisticas']['faltas'] > max_faltas:
                max_faltas = jugador['estadisticas']['faltas']
                jugador_max_faltas = jugador['nombre']
                equipo_max_faltas = nombre_equipo

    if jugador_max_faltas:
        return f"El jugador que más faltas ha cometido es {jugador_max_faltas} del equipo {equipo_max_faltas} con {max_faltas} faltas."
    else:
        return "No hay datos de faltas registrados."

def jugador_mas_tarjetas_amarillas():
    max_amarillas = 0
    jugador_max_amarillas = None
    equipo_max_amarillas = None

    for nombre_equipo, datos_equipo in equipos.items():
        for dorsal, jugador in datos_equipo['jugadores'].items():
            if jugador['estadisticas']['tarjetas_amarillas'] > max_amarillas:
                max_amarillas = jugador['estadisticas']['tarjetas_amarillas']
                jugador_max_amarillas = jugador['nombre']
                equipo_max_amarillas = nombre_equipo

    if jugador_max_amarillas:
        return f"El jugador que más tarjetas amarillas ha recibido es {jugador_max_amarillas} del equipo {equipo_max_amarillas} con {max_amarillas} tarjetas amarillas."
    else:
        return "No hay datos de tarjetas amarillas registrados."

def menu_estadisticas():
    while True:
        print("\n--- Estadísticas ---")
        print("1. Equipo que más goles ha marcado")
        print("2. Equipo que más goles ha recibido")
        print("3. Equipo en último lugar")
        print("4. Jugador que más faltas ha cometido")
        print("5. Jugador que más tarjetas amarillas ha recibido")
        print("6. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print(equipo_mas_goles())
            elif opcion == 2:
                print(equipo_mas_goles_contra())
            elif opcion == 3:
                print(equipo_ultimo_puesto())
            elif opcion == 4:
                print(jugador_mas_faltas())
            elif opcion == 5:
                print(jugador_mas_tarjetas_amarillas())
            elif opcion == 6:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
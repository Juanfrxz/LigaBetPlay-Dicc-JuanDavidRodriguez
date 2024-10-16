# partidos.py
from equipos import equipos
from jugadores import registrar_eventos_jugador
import os

partidos = {}

def programar_partido():
    fecha = input("Ingrese la fecha del partido (DD/MM/AAAA): ")
    local = input("Ingrese el nombre del equipo local: ")
    visitante = input("Ingrese el nombre del equipo visitante: ")
    
    if local not in equipos or visitante not in equipos:
        print("Uno o ambos equipos no existen.")
        return
    
    if fecha not in partidos:
        partidos[fecha] = []
    
    partidos[fecha].append({
        "local": local,
        "visitante": visitante,
        "resultado": None,
        "eventos": []
    })
    print(f"Partido entre {local} y {visitante} programado para el {fecha}.")

def registrar_resultado():
    fecha = input("Ingrese la fecha del partido (DD/MM/AAAA): ")
    if fecha not in partidos:
        print("No hay partidos programados para esa fecha.")
        return
    
    print(f"Partidos programados para el {fecha}:")
    for i, partido in enumerate(partidos[fecha]):
        print(f"{i+1}. {partido['local']} vs {partido['visitante']}")
    
    try:
        indice = int(input("Seleccione el número del partido: ")) - 1
        partido = partidos[fecha][indice]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return
    
    goles_local = int(input(f"Goles de {partido['local']}: "))
    goles_visitante = int(input(f"Goles de {partido['visitante']}: "))
    
    partido['resultado'] = (goles_local, goles_visitante)
    
    # Actualizar estadísticas de los equipos
    for equipo, goles_favor, goles_contra in [
        (partido['local'], goles_local, goles_visitante),
        (partido['visitante'], goles_visitante, goles_local)
    ]:
        equipos[equipo]['estadisticas']['partidos_jugados'] += 1
        equipos[equipo]['estadisticas']['goles_favor'] += goles_favor
        equipos[equipo]['estadisticas']['goles_contra'] += goles_contra
        
        if goles_favor > goles_contra:
            equipos[equipo]['estadisticas']['partidos_ganados'] += 1
            equipos[equipo]['estadisticas']['puntos'] += 3
        elif goles_favor < goles_contra:
            equipos[equipo]['estadisticas']['partidos_perdidos'] += 1
        else:
            equipos[equipo]['estadisticas']['partidos_empatados'] += 1
            equipos[equipo]['estadisticas']['puntos'] += 1
    
    print("Resultado registrado y estadísticas actualizadas.")
    
    # Registrar eventos del partido
    while True:
        respuesta = input("¿Desea registrar eventos para un jugador? (s/n): ")
        if respuesta.lower() != 's':
            break
        registrar_eventos_jugador()
        partido['eventos'].append("Eventos registrados")

def ver_partidos():
    for fecha, partidos_fecha in partidos.items():
        print(f"\nFecha: {fecha}")
        for partido in partidos_fecha:
            resultado = partido['resultado'] if partido['resultado'] else "No jugado"
            print(f"{partido['local']} vs {partido['visitante']} - Resultado: {resultado}")
            if partido['eventos']:
                print(f"  Eventos registrados: {len(partido['eventos'])}")

def menu_partidos():
    while True:
        print("\n--- Gestión de Partidos ---")
        print("1. Programar partido")
        print("2. Registrar resultado")
        print("3. Ver partidos")
        print("4. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                programar_partido()
            elif opcion == 2:
                registrar_resultado()
            elif opcion == 3:
                ver_partidos()
            elif opcion == 4: 
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
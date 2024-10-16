# main.py
                                                                #JUAN DAVID RODRIGUEZ CARDENAS
import os
import equipos as equi
import jugadores as jg
import partidos as par
import estadisticas as std

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("\n--- Liga BetPlay ---")
        print("1. Gestionar equipos")
        print("2. Gestionar jugadores")
        print("3. Gestionar partidos")
        print("4. Ver estadísticas")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                equi.menu_equipos()
            elif opcion == 2:
                jg.menu_jugadores()
            elif opcion == 3:
                par.menu_partidos()
            elif opcion == 4:
                std.menu_estadisticas()
            elif opcion == 5:
                print("Gracias por usar el sistema de la Liga BetPlay.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    # Crear estructura de directorios
    if not os.path.exists("datos"):
        os.makedirs("datos")
    menu_principal()
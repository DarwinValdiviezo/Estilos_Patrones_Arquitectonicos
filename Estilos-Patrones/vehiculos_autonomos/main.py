from fachada.control_fachada import ControlFachada

def main():
    control = ControlFachada()

    # Agregar vehículos a la flota
    control.agregar_drone("Drone Alfa")
    control.agregar_barco("Barco Bravo")

    # Intentar mover la flota con una clave incorrecta
    print("Intentando mover la flota con clave incorrecta:")
    print(control.mover_flota("incorrecta123"))

    # Intentar mover la flota con la clave correcta
    print("\nIntentando mover la flota con clave correcta:")
    print(control.mover_flota("seguro123"))

if __name__ == "__main__":
    main()

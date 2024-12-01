from gestor_tareas import GestorTareas
from comandos.comando_agregar import ComandoAgregarTarea
from comandos.comando_completar import ComandoCompletarTarea
from observadores.observador import Usuario
from estrategias.estrategia_fecha import EstrategiaFecha

def main():
    # Inicializar el gestor de tareas
    gestor = GestorTareas()

    # Crear usuarios observadores
    usuario1 = Usuario("Ana")
    usuario2 = Usuario("Carlos")

    # Agregar observadores al gestor
    gestor.agregar_observador(usuario1)
    gestor.agregar_observador(usuario2)

    # Crear y ejecutar comandos
    comando_agregar1 = ComandoAgregarTarea(gestor, {"id": 1, "nombre": "Revisar informes", "prioridad": 3, "completada": False})
    comando_agregar2 = ComandoAgregarTarea(gestor, {"id": 2, "nombre": "Preparar presentación", "prioridad": 5, "completada": False})
    comando_agregar1.ejecutar()
    comando_agregar2.ejecutar()

    # Listar tareas por prioridad (estrategia por defecto)
    print("\nTareas ordenadas por prioridad:")
    for tarea in gestor.listar_tareas():
        print(tarea)

    # Cambiar estrategia a orden por fecha
    gestor.cambiar_estrategia(EstrategiaFecha())
    print("\nTareas ordenadas por fecha:")
    for tarea in gestor.listar_tareas():
        print(tarea)

    # Completar una tarea
    comando_completar = ComandoCompletarTarea(gestor, 1)
    comando_completar.ejecutar()

if __name__ == "__main__":
    main()

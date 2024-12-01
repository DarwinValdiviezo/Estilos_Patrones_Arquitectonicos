from observadores.observador import Usuario
from estrategias.estrategia_prioridad import EstrategiaPrioridad
from estrategias.estrategia_fecha import EstrategiaFecha
import datetime

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.observadores = []
        self.estrategia = EstrategiaPrioridad()  # Estrategia por defecto: priorizar tareas

    # Métodos para el patrón Observer
    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

    # Métodos de gestión de tareas
    def agregar_tarea(self, tarea):
        tarea["fecha"] = datetime.datetime.now()  # Se agrega la fecha automáticamente
        self.tareas.append(tarea)
        self.notificar_observadores(f"Tarea '{tarea['nombre']}' agregada.")

    def completar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea["id"] == tarea_id:
                tarea["completada"] = True
                self.notificar_observadores(f"Tarea '{tarea['nombre']}' completada.")
                break

    # Métodos del patrón Strategy
    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

    def listar_tareas(self):
        tareas_ordenadas = self.estrategia.ordenar(self.tareas)
        return tareas_ordenadas

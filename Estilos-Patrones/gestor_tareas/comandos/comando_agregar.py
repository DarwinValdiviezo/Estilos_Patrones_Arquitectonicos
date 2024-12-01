from comandos.comando_base import ComandoBase

class ComandoAgregarTarea(ComandoBase):
    def __init__(self, gestor, tarea):
        self.gestor = gestor
        self.tarea = tarea

    def ejecutar(self):
        self.gestor.agregar_tarea(self.tarea)

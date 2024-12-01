from comandos.comando_base import ComandoBase

class ComandoCompletarTarea(ComandoBase):
    def __init__(self, gestor, tarea_id):
        self.gestor = gestor
        self.tarea_id = tarea_id

    def ejecutar(self):
        self.gestor.completar_tarea(self.tarea_id)

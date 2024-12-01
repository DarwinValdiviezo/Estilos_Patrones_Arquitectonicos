class EstrategiaPrioridad:
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t["prioridad"], reverse=True)

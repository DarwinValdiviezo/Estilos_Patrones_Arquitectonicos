class EstrategiaFecha:
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t["fecha"])

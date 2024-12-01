class VehiculoBase:
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

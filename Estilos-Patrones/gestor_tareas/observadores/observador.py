class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

class Usuario(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] Notificación: {mensaje}")

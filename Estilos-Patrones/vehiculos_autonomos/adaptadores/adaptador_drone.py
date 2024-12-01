from componentes.vehiculo_base import VehiculoBase

class DroneAdapter(VehiculoBase):
    def __init__(self, nombre, sistema_drone):
        super().__init__(nombre)
        self.sistema_drone = sistema_drone

    def mover(self):
        return self.sistema_drone.volar()

class SistemaDrone:
    def volar(self):
        return f"El drone está volando en el aire."

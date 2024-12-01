from componentes.vehiculo_base import VehiculoBase

class FlotaComposite(VehiculoBase):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vehiculos = []

    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mover(self):
        acciones = [vehiculo.mover() for vehiculo in self.vehiculos]
        return f"Flota '{self.nombre}' en acción:\n" + "\n".join(acciones)

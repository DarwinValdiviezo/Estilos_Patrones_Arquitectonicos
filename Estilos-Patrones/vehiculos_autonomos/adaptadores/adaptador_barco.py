from componentes.vehiculo_base import VehiculoBase

class BarcoAdapter(VehiculoBase):
    def __init__(self, nombre, sistema_barco):
        super().__init__(nombre)
        self.sistema_barco = sistema_barco

    def mover(self):
        return self.sistema_barco.navegar()

class SistemaBarco:
    def navegar(self):
        return f"El barco está navegando en el agua."

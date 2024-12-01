from adaptadores.adaptador_drone import DroneAdapter, SistemaDrone
from adaptadores.adaptador_barco import BarcoAdapter, SistemaBarco
from componentes.flota_composite import FlotaComposite
from proxies.proxy_seguridad import ProxySeguridad

class ControlFachada:
    def __init__(self):
        self.flota = FlotaComposite("Principal")

    def agregar_drone(self, nombre):
        drone = DroneAdapter(nombre, SistemaDrone())
        self.flota.agregar(drone)

    def agregar_barco(self, nombre):
        barco = BarcoAdapter(nombre, SistemaBarco())
        self.flota.agregar(barco)

    def mover_flota(self, clave):
        proxy = ProxySeguridad(self.flota, clave)
        return proxy.mover()

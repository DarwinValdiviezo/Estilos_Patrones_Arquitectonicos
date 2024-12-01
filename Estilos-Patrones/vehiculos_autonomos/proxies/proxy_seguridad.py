class ProxySeguridad:
    def __init__(self, vehiculo, clave):
        self.vehiculo = vehiculo
        self.clave_correcta = "seguro123"
        self.clave = clave

    def mover(self):
        if self.clave == self.clave_correcta:
            return self.vehiculo.mover()
        else:
            return f"Acceso denegado al vehículo '{self.vehiculo.nombre}'."

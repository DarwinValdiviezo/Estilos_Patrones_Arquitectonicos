class PersonajeBase:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def describir(self):
        return f"{self.nombre} tiene un nivel de poder de {self.poder}."

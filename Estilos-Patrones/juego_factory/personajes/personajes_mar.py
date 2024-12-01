from .personaje_base import PersonajeBase

class Sirena(PersonajeBase):
    def habilidad_especial(self):
        return "Canta para atraer a los marineros."

class Tiburon(PersonajeBase):
    def habilidad_especial(self):
        return "Depredador rápido y letal."

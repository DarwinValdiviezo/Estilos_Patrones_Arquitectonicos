from .personaje_base import PersonajeBase

class Escorpion(PersonajeBase):
    def habilidad_especial(self):
        return "Picadura venenosa."

class Camello(PersonajeBase):
    def habilidad_especial(self):
        return "Resistencia al agua y al calor."

from .personaje_base import PersonajeBase

class Elfo(PersonajeBase):
    def habilidad_especial(self):
        return "Visión aguda y habilidad con el arco."

class Oso(PersonajeBase):
    def habilidad_especial(self):
        return "Fuerza bruta y resistencia."

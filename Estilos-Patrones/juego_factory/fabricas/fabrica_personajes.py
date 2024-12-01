from personajes.personajes_mar import Sirena, Tiburon
from personajes.personajes_bosque import Elfo, Oso
from personajes.personajes_desierto import Escorpion, Camello

class FabricaPersonajes:
    @staticmethod
    def crear_personajes(entorno):
        if entorno == "mar":
            return [Sirena("Sirena", 80), Tiburon("Tiburón", 90)]
        elif entorno == "bosque":
            return [Elfo("Elfo", 70), Oso("Oso", 100)]
        elif entorno == "desierto":
            return [Escorpion("Escorpión", 60), Camello("Camello", 50)]
        else:
            raise ValueError("¡Entorno desconocido!")

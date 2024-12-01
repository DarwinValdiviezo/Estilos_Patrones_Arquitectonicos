from entornos.entorno_mar import EntornoMar
from entornos.entorno_bosque import EntornoBosque
from entornos.entorno_desierto import EntornoDesierto

class FabricaEntornos:
    @staticmethod
    def crear_entorno(entorno):
        if entorno == "mar":
            return EntornoMar()
        elif entorno == "bosque":
            return EntornoBosque()
        elif entorno == "desierto":
            return EntornoDesierto()
        else:
            raise ValueError("¡Entorno desconocido!")

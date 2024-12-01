from fabricas.fabrica_personajes import FabricaPersonajes
from fabricas.fabrica_entornos import FabricaEntornos

def main():
    entorno_elegido = input("Elige un entorno (mar, bosque, desierto): ").strip().lower()
    
    try:
        entorno = FabricaEntornos.crear_entorno(entorno_elegido)
        personajes = FabricaPersonajes.crear_personajes(entorno_elegido)
        
        print(f"\nEntorno: {entorno.descripcion()}")
        print("\nPersonajes:")
        for personaje in personajes:
            print(f"- {personaje.describir()} | Habilidad Especial: {personaje.habilidad_especial()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

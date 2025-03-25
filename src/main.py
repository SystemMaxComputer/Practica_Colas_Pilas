import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.simulador import iniciar_simulacion

if __name__ == "__main__":
    try:
        iniciar_simulacion()
    except KeyboardInterrupt:
        print("\nSimulación finalizada por el usuario.")
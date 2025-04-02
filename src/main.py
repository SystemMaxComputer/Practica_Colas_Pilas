import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from simulador import iniciar_simulacion

if __name__ == "__main__":
    try:
        iniciar_simulacion()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulación finalizada por el usuario.")
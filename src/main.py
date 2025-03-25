from src.simulador import iniciar_simulacion

if __name__ == "__main__":
    try:
        iniciar_simulacion()
    except KeyboardInterrupt:
        print("\nSimulación finalizada correctamente.")
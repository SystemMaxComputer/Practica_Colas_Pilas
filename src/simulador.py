import threading
import time
from cola_prioridad import ColaPrioridad
from procesador_mensajes import leer_mensajes
from agente import Agente

cola = None
agentes = []

def iniciar_simulacion():
    global cola, agentes
    cola = leer_mensajes()
    agentes = [Agente(i, nivel) for i, nivel in enumerate(["experto", "intermedio", "básico"], start=1)]
    
    threading.Thread(target=procesar_mensajes, daemon=True).start()

def procesar_mensajes():
    while True:
        mensajes_pendientes = False
        for agente in agentes:
            if not agente.ocupado:
                mensaje = cola.extraer()
                if mensaje:
                    print(f"Agente {agente.id} ({agente.nivel}) revisando mensaje: {mensaje}")
                    mensajes_pendientes = True
                    threading.Thread(target=agente.atender_mensaje, args=(mensaje,), daemon=True).start()
        
        if not mensajes_pendientes:
            print("No hay más mensajes en la cola. Simulación terminada.")
            break
        
        time.sleep(1)
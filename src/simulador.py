import threading
from src.cola_prioridad import ColaPrioridad
from src.procesador_mensajes import leer_mensajes
from src.agente import Agente

def iniciar_simulacion():
    cola = ColaPrioridad()
    agentes = [Agente(i, nivel) for i, nivel in enumerate(["experto", "intermedio", "básico"], start=1)]
    
    def procesar_mensajes():
        while True:
            for agente in agentes:
                if not agente.ocupado:
                    mensaje = cola.extraer()
                    if mensaje:
                        threading.Thread(target=agente.atender_mensaje, args=(mensaje,)).start()
            time.sleep(1)

    def monitorear_mensajes():
        for mensaje, prioridad in leer_mensajes():
            cola.insertar(mensaje, prioridad)

    threading.Thread(target=procesar_mensajes, daemon=True).start()
    threading.Thread(target=monitorear_mensajes, daemon=True).start()

    return cola  # Agregado para evitar un posible error de importación

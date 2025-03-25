import threading
import time
from cola_prioridad import ColaPrioridad
from procesador_mensajes import leer_mensajes
from agente import Agente

ejecutando = True  # Control de ejecución

def iniciar_simulacion():
    global ejecutando
    cola = ColaPrioridad()
    agentes = [Agente(i, nivel) for i, nivel in enumerate(["experto", "intermedio", "básico"], start=1)]

    def procesar_mensajes():
        while ejecutando:
            for agente in agentes:
                if not agente.ocupado:
                    mensaje = cola.extraer()
                    if mensaje:
                        hilo = threading.Thread(target=agente.atender_mensaje, args=(mensaje,))
                        hilo.start()
                        hilo.join()  # Esperar a que termine el hilo
            time.sleep(1)

    def monitorear_mensajes():
        for mensaje, prioridad in leer_mensajes():
            if not ejecutando:
                break
            cola.insertar(mensaje, prioridad)

    # Crear hilos sin `daemon=True`
    hilo_mensajes = threading.Thread(target=procesar_mensajes)
    hilo_monitor = threading.Thread(target=monitorear_mensajes)

    hilo_mensajes.start()
    hilo_monitor.start()

    try:
        hilo_mensajes.join()
        hilo_monitor.join()
    except KeyboardInterrupt:
        print("\nFinalizando simulación...")
        ejecutando = False

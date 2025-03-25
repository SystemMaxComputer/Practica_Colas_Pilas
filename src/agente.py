import time
import threading
from procesador_mensajes import palabras_clave

class Agente:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel
        self.ocupado = False
        self.factor = {"básico": 1.0, "intermedio": 0.75, "experto": 0.5}[nivel]
    
    def atender_mensaje(self, mensaje):
        tiempo_estimado = (len(mensaje.split()) / 10) + (sum(palabras_clave.get(p, 0) for p in mensaje.split()) / 2)
        tiempo_final = tiempo_estimado * self.factor
        print(f"Agente {self.id} ({self.nivel}) atendiendo: {mensaje} | Tiempo: {tiempo_final:.2f}s")
        self.ocupado = True
        time.sleep(tiempo_final)
        self.ocupado = False
        with open("log_atenciones.txt", "a", encoding="utf-8") as log:
            log.write(f"Agente {self.id} ({self.nivel}) atendió: {mensaje} en {tiempo_final:.2f}s\n")

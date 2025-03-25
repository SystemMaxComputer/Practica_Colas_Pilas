import os
import time

tiempos_espera = 5
palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
}

def calcular_prioridad(mensaje):
    prioridad = sum(palabras_clave.get(palabra, 0) for palabra in mensaje.lower().split())
    return prioridad

def leer_mensajes(carpeta="data/mensajes"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    mensajes = []
    for archivo in os.listdir(carpeta):
        with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            prioridad = calcular_prioridad(contenido)
            mensajes.append((contenido, prioridad))
        os.remove(os.path.join(carpeta, archivo))
    return mensajes
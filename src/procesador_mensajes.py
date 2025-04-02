import os
from cola_prioridad  import ColaPrioridad

palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
}

def calcular_prioridad(mensaje):
    prioridad_total = 0
    palabras = mensaje.lower().split()
    
    for palabra in palabras:
        prioridad_total += palabras_clave.get(palabra, 0)
    return prioridad_total

def leer_mensajes(ruta_archivo="data/mensajes.txt"):
    if not os.path.exists(ruta_archivo):
        return ColaPrioridad()
    
    cola = ColaPrioridad()
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            mensaje = " ".join(linea.strip().split()[1:])  # Eliminar numeración
            prioridad = calcular_prioridad(mensaje)
            cola.insertar(mensaje, prioridad)
    
    cola.imprimir_cola()  # Mostrar la cola priorizada
    return cola
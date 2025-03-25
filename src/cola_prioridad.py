import threading

class Nodo:
    def __init__(self, mensaje, prioridad):
        self.mensaje = mensaje
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.primero = None
        self.lock = threading.Lock()

    def insertar(self, mensaje, prioridad):
        with self.lock:
            nuevo_nodo = Nodo(mensaje, prioridad)
            if not self.primero or self.primero.prioridad < prioridad:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                actual = self.primero
                while actual.siguiente and actual.siguiente.prioridad >= prioridad:
                    actual = actual.siguiente
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo

    def extraer(self):
        with self.lock:
            if not self.primero:
                return None
            mensaje = self.primero.mensaje
            self.primero = self.primero.siguiente
            return mensaje
import threading

class Nodo:
    def __init__(self, mensaje, prioridad):
        self.mensaje = mensaje
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.primero = None  # Nodo con mayor prioridad
        self.ultimo = None  # Último nodo en la cola
        self.lock = threading.Lock()

    def insertar(self, mensaje, prioridad):
        with self.lock:
            nuevo_nodo = Nodo(mensaje, prioridad)
            if not self.primero or self.primero.prioridad < prioridad:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
                if not self.ultimo:  # Si la cola estaba vacía
                    self.ultimo = nuevo_nodo
            else:
                actual = self.primero
                while actual.siguiente and actual.siguiente.prioridad >= prioridad:
                    actual = actual.siguiente
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                if not nuevo_nodo.siguiente:  # Si se insertó al final
                    self.ultimo = nuevo_nodo

    def extraer(self):
        with self.lock:
            if not self.primero:
                return None
            mensaje = self.primero.mensaje
            self.primero = self.primero.siguiente
            if not self.primero:  # Si la cola quedó vacía
                self.ultimo = None
            return mensaje
        
    def imprimir_cola(self):
        with self.lock:
            actual = self.primero
            print("Cola de mensajes priorizados:")
            while actual:
                print(f"  - [{actual.prioridad}] {actual.mensaje}")
                actual = actual.siguiente

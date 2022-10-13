# Creacion de la clase Nodo que contiene el dato, el puntero al siguiente nodo y el puntero al nodo anterior

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Creacion de la clase PilaLIFO que contiene el puntero(head) al primer nodo

class PilaLIFO:
    def __init__(self):
        self.head = None

    # Metodo para insertar un nodo al final de la pila

    def Push(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo

        # Sino, se inserta al inicio de la pila
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head.prev = nuevoNodo
            self.head = nuevoNodo

    # Metodo para eliminar el ultimo nodo que ingreso a la pila

    def Pop(self):
        # Si la lista esta vacia no se puede eliminar el ultimo nodo
        if self.head is None:
            return None

        # Sino, se elimina el ultimo nodo que ingreso a la pila
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def printPila(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # acceder al dato cabeza de la pila
    def getHead(self):
        return self.head.data

    # Largo de la pila
    def getLargo(self):
        temp = self.head
        largo = 0
        while temp is not None:
            largo += 1
            temp = temp.next
        return largo


pila = PilaLIFO()
pila.Push(1)
pila.Push(3)
pila.Push(4)
pila.Push(5)
pila.Push(6)

pila.printPila()
print(pila.getLargo())

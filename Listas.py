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
    def mostrarlista(self):
        
        puntero = self.head
        siguiente = puntero.next
        while siguiente != None:
            print(puntero)
            
            puntero = siguiente
            siguiente = puntero.next
            
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


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None

    def getLargo(self):
        temp = self.head
        largo = 0
        while temp is not None:
            largo += 1
            temp = temp.next
        return largo

    def mostrarlista(self):
        
        puntero = self.head
        siguiente = puntero.next
        while siguiente != None:
            print(puntero)
            
            puntero = siguiente
            siguiente = puntero.next
              
                
        
        
    # Metodo para insertar un nodo al inicio de la lista

    def insertarInicio(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        # Sino se crea un nuevo nodo y se inserta al inicio de la lista
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head.prev = nuevoNodo
            self.head = nuevoNodo

    # Metodo para insertar un nodo al final de la lista

    def insertarFinalNodo(self, elemento):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
            return
        #  Sino se crea un nuevo nodo y se inserta al final de la lista con la condicion de que el siguiente nodo no sea None
        temp = self.head
        while (temp.next) is not None:
            temp = temp.next
        nuevoNodo = Nodo(elemento)
        temp.next = nuevoNodo
        nuevoNodo.prev = temp

    # Metodo para insertar un nodo en una posicion determinada de la lista

    def insertarPos(self, elemento, pos):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        # Sino se crea un nuevo nodo y se inserta en la posicion de la lista con la condicion de que el siguiente nodo no sea None
        else:
            nuevoNodo = Nodo(elemento)
            elemento = self.head
            i = 0
            while (i < pos - 1):
                i += 1
                elemento = elemento.next
            if pos == 0:
                nuevoNodo.next = self.head
                self.head.prev = nuevoNodo
                self.head = nuevoNodo
            else:
                nuevoNodo.next = elemento.next
                elemento.next.prev = nuevoNodo
                elemento.next = nuevoNodo
                nuevoNodo.prev = elemento

    # Metodo para eliminar un nodo determinado de la lista

    def eleminarPos(self, pos):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            print("La lista esta vacia")
            return

        elemento = self.head
        if pos == 0:
            self.head = elemento.next
            elemento.next.prev = None
            return elemento.data

        i = 0
        while (i < pos):
            i += 1
            elemento = elemento.next

        else:
            elemento.prev.next = elemento.next
            elemento.next.prev = elemento.prev
            return elemento.data

    # Metodo para acceder a la posicion de un nodo determinado de la lista

    def accederPos(self, pos):
        if self.head is None:
            print("La lista esta vacia")
            return
        elemento = self.head
        i = 0
        while (i < pos):
            i += 1
            elemento = elemento.next
        return elemento.data

    # Metodo para recoorrer la lista desde el inicio hasta el final

    def recorrerInicioFin(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        apuntar = self.head
        while (apuntar):
            print(apuntar.data)
            apuntar = apuntar.next

    # Metodo para recoorrer la lista desde el final hasta el inicio

    def recorrerFinalInicio(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        apuntar = self.head
        while (apuntar.next):
            apuntar = apuntar.next
        while (apuntar):
            print(apuntar.data)
            apuntar = apuntar.prev
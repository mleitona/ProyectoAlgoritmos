print("Hola desde el tablero")


class Tablero():
    
    def __init__(self,Dimencion):
        self.Dimencion = Dimencion
        self.Tablero = None
    def getDimencion(self):
        return self.Dimencion
    def getTablero(self):
        
        if self.Tablero == None:
            print("Debe generar el tablero")
            return 0
        else:
            print("Muestra tablero ")
            return self.Tablero

#    Reglas generales para los tipos de comida.

    #  Comida Tipo 1: al comerlo, este se añade a la cola 
    #  Comida Tipo 2: al comerlo, este se añade en la posición indicada por su número. 
    #  Comida Tipo 3: al comerlo, se agrega a la cabeza 
    #  Comida Tipo 4: esta comida se mueve por pantalla en forma aleatoria 
    #  Comida Tipo 5: Cierta comida solo se puede comer si la snake encierra dicha comida
    #                  haciendo tocar su cabeza con el último elemento de la cola.
    #                  En ese momento la snake se invierte, todos los elementos de la lista se invierten, es decir, comienza a girar en sentido contrario y recibe bonificación de puntaje. 

    #  Comida Tipo 6: Existen al menos, 3 pares de comida que se pueden comer en forma pareada y
    #                  dan bonificación de puntaje. Entre más compleja sean enlazados los pares, mayor es la bonificación de puntaje. Por ejemplo, si estos tres pares se simbolizan por {}, [], (), entonces la comida en secuencia {[({}[]())]}* tiene mayor puntaje cuando se obtiene el ultimo par (se cierra el último paréntesis y luego se come un * que indica el final).            
    #                  Si la comida de este tipo no se come en secuencia correcta, entonces se realiza un descuento del puntaje. 
    
    
    
    
################################################################################################################################
import random
import pygame

class Comidas():

    def __init__(self,puntos,TipodeComida):
        self.puntos = puntos
        self.tipo_comida = TipodeComida
        self.Contenido = None

    def GetT_comida(self):
        return self.tipo_comida
    def GetPuntos(self):
        return self.puntos
    def Comida_T_1(self):
        #Se agrega el contenido al tipo de comida 1, sera representado por TP1
        self.Contenido = 'TP1'
        return self.Contenido
    
    def Comida_T_2(self,LargoSnake):
        #Se agrega el contenido al tipo de comida 2, sera representado por un valor numerico aleatorio con limite del largo del gusano 
        self.Contenido = random(0,LargoSnake)
        return self.Contenido
    def Comida_T_3(self):
        #Se agrega el contenido al tipo de comida 3, sera representado por TP3
        self.Contenido = 'TP3'
        return self.Contenido

    def Comida_T_4(self, surface, serpiente): # Este código es más o menos el comportamiento que debiese tener la comida tipo 4
        # Velocidad Comida
        comida_velocidad_x = 5
        comida_velocidad_y = 5
        # Coordenadas Comida
        comida_coordX = random.randint(0, 600)
        comida_coordY = random.randint(0, 600)
        while(True):
            comida4 = pygame.draw.rect(surface, (255, 0, 128), (comida_coordX, comida_coordY), (20, 20)) # GRIDSIZE = 20
            if(comida_coordX > 600 or comida_coordX < 0):
                comida_velocidad_x = comida_velocidad_x * -1
    
            if(comida_coordY > 600 or comida_coordY < 0):
                comida_velocidad_y = comida_velocidad_y * -1
            
            if(comida4.collidedict(serpiente)):
                self.contenido = 'TP4'
                return self.contenido

    def Comida_T_5(self):
        pass
    def Comida_T_6(self):
        pass
        
        



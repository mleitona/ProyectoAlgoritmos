
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
print("hola desde comidas")
class Comidas():
    
    def __init__(self,Tipo_comida,puntos):
        
        self.T_comida = Tipo_comida
        self.Puntos = puntos
        
    def GetT_comida(self):
        return self.T_comida
    def GetPuntos(self):
        return self.Puntos
    
    
    def Comida_T_1(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 1: al comerlo, este se añade a la cola ")
        return 0
    
    def Comida_T_2(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 2: al comerlo, este se añade en la posición indicada por su número. ")
        return 0
    
    def Comida_T_3(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 3: al comerlo, se agrega a la cabeza")
        return 0
    
    def Comida_T_4(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 4: esta comida se mueve por pantalla en forma aleatoria")
        return 0
    def Comida_T_5(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 5: Cierta comida solo se puede comer si la snake encierra dicha comida haciendo tocar su cabeza con el último elemento de la cola. En ese momento la snake se invierte, todos los elementos de la lista se invierten, es decir, comienza a girar en sentido contrario y recibe bonificación de puntaje. ")
        return 0
    def Comida_T_6(self):
        
        print("se define este tipo de comida segun: ")
        print("Comida Tipo 6: Existen al menos, 3 pares de comida que se pueden comer en forma pareada y dan bonificación de puntaje. Entre más compleja sean enlazados los pares, mayor es la bonificación de puntaje. Por ejemplo, si estos tres pares se simbolizan por {}, [], (), entonces la comida en secuencia {[({}[]())]}* tiene mayor puntaje cuando se obtiene el ultimo par (se cierra el último paréntesis y luego se come un * que indica el final Si la comida de este tipo no se come en secuencia correcta, entonces se realiza un descuento del puntaje. ")
        return 0
        
        



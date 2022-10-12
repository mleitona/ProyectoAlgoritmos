# ProyectoAlgoritmos
Proyecto de algoritmos del segundo semestre del año 2022
PROYECTO JUEGO SNAKE 
El juego “Snake” El juego de la víbora por todos conocidos, es un juego donde inicialmente se comienza con un cuadrado que 
siempre está en movimiento, el cual podemos guiar hacia la derecha, izquierda, arriba o abajo. Al mismo tiempo aparecen al 
azar cuadrados inmóviles que cuando la víbora “se los come”, la víbora aumenta la cantidad de cuadros en 1 asemejándose a 
una víbora o serpiente. La víbora no puede comerse así misma ni tampoco chocar contra las paredes. 
Sin embargo, ahora se requiere construir un nuevo juego Snake donde existen nuevas reglas: 

     Comida Tipo 1: al comerlo, este se añade a la cola 
     Comida Tipo 2: al comerlo, este se añade en la posición indicada por su número. 
     Comida Tipo 3: al comerlo, se agrega a la cabeza 
     Comida Tipo 4: esta comida se mueve por pantalla en forma aleatoria 
     Comida Tipo 5: Cierta comida solo se puede comer si la snake encierra dicha comida haciendo tocar su cabeza con el último elemento de la cola.

En ese momento la snake se invierte, todos los elementos de la lista se invierten, es decir, 
comienza a girar en sentido contrario y recibe bonificación de puntaje. 

     Comida Tipo 6: Existen al menos, 3 pares de comida que se pueden comer en forma pareada y dan bonificación de 
                     puntaje. Entre más compleja sean enlazados los pares, mayor es la bonificación de puntaje. Por ejemplo, si estos tres pares se simbolizan por {}, [], (), entonces la comida en secuencia {[({}[]())]}* tiene mayor puntaje cuando se obtiene el ultimo par (se cierra el último paréntesis y luego se come un * que indica el final). Si la comida de este tipo no se come en secuencia correcta, entonces se realiza un descuento del puntaje. 
    
     Usted debe decidir la forma de otorgar el puntaje, pero debe respetar el funcionamiento de comida Tipo 5 y 6. 
     Usted decide la forma gráfica y sonora del juego. 
     La posición y tipo de la comida se genera al azar y existe más de una comida al mismo tiempo 
     Las reglas del juego pueden ser adaptadas para mejorar la jugabilidad, pero no simplificadas. 

Aspectos Algorítmicos general: 

     No puede utilizar ningún tipo de estructura de datos provista por el lenguaje o que sean parte del retorno de 
      funciones/métodos (listas, vectores, matrices, diccionarios, etc.), pues usted debe implementar cualquiera que 
      necesite mediante listas enlazadas dobles y simples. 
     Toda la funcionalidad de la snake es una representación gráfica 1 a 1 de la estructura de dato que la contiene. 
     No se puede utilizar ningún tipo de algoritmo de ordenamiento provisto por el lenguaje, debe implementar el    que usted necesite si fuese necesario. 
     Utilice las capacidades de orientación al objeto del lenguaje 
     Se debe implementar, por lo menos, un tipo de lista enlazada simple y un tipo de lista enlazada doble
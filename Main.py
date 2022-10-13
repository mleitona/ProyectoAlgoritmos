

###########################################################################################
# importamos los demas objetos.

import sys
import pygame

from constantes import *

pygame.init()
screen = pygame.display.set_mode((WITH, HEIGHT))
pygame.display.set_caption("Skake Game")
screen.fill((180, 220, 10))

class Game:
    def __init__(self):
        self.constructor_lineas()

    def constructor_lineas(self):

        # Crear marco de juego tipo snake nokia
        # Crear lineas horizontales
        for i in range(0, WITH, 20):
            pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, HEIGHT))
            pygame.display.flip()

        # Crear lineas verticales
        for i in range(0, HEIGHT, 20):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (WITH, i))
            pygame.display.flip()

        # Crear lineas diagonales
        for i in range(0, HEIGHT, 20):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (WITH, i))
            pygame.display.flip()

        # Puntaje del juego
        font = pygame.font.Font(None, 36)
        text = font.render(f"Puntaje: {None}", 1, (10, 10, 10))
        screen.blit(text, (10, 10))
        pygame.display.flip()








        # Marco Snake nokia centro pagina central











def main():

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()

if __name__ == '__main__':
    #Main
    main()

#############################################

print("cambio para que lo bajen los demas :)")
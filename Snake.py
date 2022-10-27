import sys
import pygame
import random
from PIL import Image, ImageSequence

from Constantes import *
from Listas import *


class Snake:    # Gusano 
    def __init__(self):
        self.length = PilaLIFO()
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (20, 20, 0)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]
    def turn(self, point):
        if self.length.getLargo() > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
            
            
    def move(self):  # Se mueve constantemente el gusano
        
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRIDSIZE)) % WIDTH), (cur[1] + (y * GRIDSIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            print("Choco el gusano")
            
            self.reset()
        else:
         
            self.positions.insert(0, new)
            if len(self.positions) > self.length.getLargo():
                self.positions.pop()
   
   
   
    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
    def draw(self, surface):
        
        for p in self.positions:
            
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (100, 100, 0), r, 1)
    def handle_keys(self):
        
 
        for event in pygame.event.get():  # ford que mueve los controles
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
    def InsertaComida1():
        return 0
    def InsertaComida2():
        return 0
    def InsertaComida3():
        return 0
    def InsertaComida4():
        return 0
    def InsertaComida5():
        return 0
    def InsertaComida6():
        return 0



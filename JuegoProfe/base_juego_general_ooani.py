# base_juego_general.py
#
# Base para juego general . Prof. Darío Rojas / Programación
# Este código es un ejemplo para:
#  + Mostrar inicialización de Pygame
#  + Mostrar cómo dibujar en pantalla con pygame
#  + Mostrar cómo desplegar figuras
#  + Mostrar el uso de colisiones
#  + Mostrar cómo capturar datos de teclado y mouse con pygame
#  + Servir de base para Proyecto.
#
# *Recuerde eliminar los comentarios antes de entregar su tarea.
# *Este ejemplo tiene listas de python, que salvo las que usa pil2surface y load_gif no pueden usarse

import pygame, time, random, sys
from PIL import Image, ImageSequence
#convierte una imagen tipo PIL a surface de pygame
def pil2surface(pil_img):
    mode, size, data = pil_img.mode, pil_img.size, pil_img.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

#carga una gif animado como una lista de imagenes pygame
def load_gif(filename):
    pil_img = Image.open(filename)
    sprites = []
    if pil_img.format == 'GIF' and pil_img.is_animated:
        for sp in ImageSequence.Iterator(pil_img):
            py_img = pil2surface(sp.convert('RGBA'))
            sprites.append(py_img)
    else:
         sprites.append(pil2surface(pil_img))
    return  sprites

#dibuja en win la secuencia ani en posiciones x,y cada tf-ti tiempo usando indice f 
def draw_gif(win, ani, x, y, ti, tf, f):
    if f>=len(ani): f=0
    rect = ani[f].get_rect(center = (x, y))
    win.blit(ani[f], rect)
    if time.time() - ti > tf:
        f  += 1
        ti = time.time()
        
    return (f, ti)

#Ejemplo de que los elementos de un juego pueden ser clases o listas de clases
class Enemy:
    def __init__(self, d, i, e, x, y, st): #constructor
        self.der = load_gif(d)
        self.izq = load_gif(i)
        self.exp = load_gif(e)
        self.frm = 0
        self.x  = x
        self.y  = y
        self.st = st
        self.d  = x
        self.dis = False
        self.tim= time.time()

    def step(self, mx, my, x, y):  #por cada iteración
        if not self.dis:
            self.dis = random.randrange(0,10000) < 3

        if self.dis and self.st>0:  #si está disparando
            pygame.draw.circle(pantalla, color=color_verde, center=(self.d , self.y), radius=10)
            if self.st!=0 and self.d-20 <= mx <= self.d+20 and self.y-20 <= my <= self.y+20:
                self.dis = False
                self.d = self.x
                return True
                
            if self.st==1:
                self.d -= 0.1
            elif self.st==2:
                self.d += 0.1
            if self.d<0 or self.d>540:
                self.dis = False
                self.d = self.x
            
        
        if self.st!=0 and self.x-20 <= x <= self.x+20 and self.y-20 <= y <= self.y+20: #verifica si explora
            self.st=0
            self.frm=0
            
        if self.st==0: #explota
            self.frm, self.tim = draw_gif(pantalla, self.exp, self.x , self.y , self.tim , 0.1, self.frm)
            if self.frm==0:
                self.st=-1                          
        elif self.st==1: #mueve izquierda
            self.frm, self.tim = draw_gif(pantalla, self.izq , self.x , self.y , self.tim , 0.1, self.frm)
        elif self.st==2: #mueve derecha
            self.frm, self.tim = draw_gif(pantalla, self.der, self.x , self.y , self.tim , 0.1, self.frm)

        return False
    
#Inicializa modulo pygame
pygame.init()
pygame.display.set_caption('This the way')
texto    = pygame.font.SysFont('Arial', 25)
tamano   = ancho, alto = 540, 360
pantalla = pygame.display.set_mode(tamano)

fondo = pygame.image.load('fondo.jpg') #fonso

#carga animaciones para personaje
ani_mmander = load_gif("derecha.gif")
ani_mmanizq = load_gif("izquierda.gif")
ani_mmanexplode = load_gif("explosion.gif")
#coordenadas y datos de personajes
frm_mman = 0
x_mman = 250
y_mman = 250
st_mman = 1
tim_mman = time.time()

#crea enemigos al azar
lene = []
for i in range(0,10):
    if random.randrange(1,3)==1:
        st=1
        x=500
    else:
        st=2
        x=30
        
    y = random.randrange(30,300)
    lene.append(Enemy("marioder.gif", "marioizq.gif", "explosion.gif", x, y, st))

#sprite de la bola de fuego
ani_missil = load_gif("missil.gif")
frm_missil = 0
x_missil = 250
y_missil = 250
st_missil = 0
tim_missil = time.time()


#Tuplas con colores del juego
color_negro  = 0, 0, 0
color_blanco = 255,255,255
color_verde  = 0, 255, 0

flag_salir = False
run = True
while not flag_salir:
    #Busca entre todos los eventos del juego el cierre de ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_salir=True

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_botonpress =  (evento.type == pygame.MOUSEBUTTONDOWN)
    mouse_botonup    =  (evento.type == pygame.MOUSEBUTTONUP)
        

    keys = pygame.key.get_pressed()
    #pantalla.fill(color_negro) #fondo negro
    pantalla.blit(fondo, (0,0)) #fondo imagen

    #si no está explotando porque murió
    if run:      
        if keys[pygame.K_UP]:
            y_mman -= 0.1

        if keys[pygame.K_DOWN]:
            y_mman += 0.1

        if keys[pygame.K_LEFT]:
            st_mman = 1
            x_mman -= 0.1
            
        if keys[pygame.K_RIGHT]:
            st_mman = 2
            x_mman += 0.1

        if keys[pygame.K_SPACE] and st_missil==0:
            y_missil = y_mman
            x_missil = x_mman
            if st_mman==1:
                st_missil = -0.1
            else:
                st_missil = 0.1
                
        if st_mman == 1:
            ani_mman = ani_mmanizq
        elif st_mman == 2:
            ani_mman = ani_mmander     

        if st_missil != 0:
            x_missil += st_missil
            if x_missil<0 or x_missil>540:
                st_missil = 0
            else:
                frm_missil,tim_missil = draw_gif(pantalla, ani_missil , x_missil , y_missil , tim_missil , 0.1, frm_missil )

        #despliega todos los enemigos (internamente ellos hacen todo en step() )
        for e in lene:
            if e.step(x_mman, y_mman, x_missil, y_missil):
                run = False
                frm_mman = 1

        frm_mman,tim_mman = draw_gif(pantalla, ani_mman, x_mman, y_mman, tim_mman, 0.1, frm_mman)  
    else: #esta explotando
        frm_mman,tim_mman = draw_gif(pantalla, ani_mmanexplode, x_mman, y_mman, tim_mman, 0.1, frm_mman)
        if frm_mman==0:
            sys.exit()

    pygame.display.flip() #update para todas aquellas que no tienen

pygame.display.quit()
    



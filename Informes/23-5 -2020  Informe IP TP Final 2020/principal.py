'''
  Laura Peralta, Luana Bertani, Lopez Gonzalo
  
  Universidad Nacional General Sarmiento
  
  Mayo 2020
'''

import math, os, random, sys
import pygame

from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from extras import *


def main():
    #### CONFIGURACIONES DE PYGAME  ####
    
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")

    screen = pygame.display.set_mode((ANCHO, ALTO))
    
    
    ####   IMAGENES    ####
    fondoPresentacion = pygame.image.load("imagenes/fondo.png").convert_alpha()
    imgHoja = pygame.image.load("imagenes/Hoja.jpg").convert_alpha()
    
    
    ####  MUSICA INICIAL   ####
    pygame.mixer.music.load("sonidos/tetris.mp3")
    pygame.mixer.music.play()


    ####  CONSTANTES   ####
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    items=["colores","paises","animales", ]    
    
    colores=["rojo","azul","amarillo","negro","blanco","celeste","verde","rosa"]
    paises=["argentina","uruguay","brasil","cuba","venezuela"]
    animales=["mono","jirafa","gato","perro","jabali","elefante","pez","cocodrilo","rinoceronte","caballo"]
    
    listaDeTodo=[colores,paises,animales]

    
    ####  VAIRABLES   ####
    NIVEL = 10 
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]
    puntos = 0
    i = 0
    inicio = True
    
    
    ####  FUNCIONES PREVIAS  ####
    letraAzar = unaAlAzar(abc)
    
    
    ####  CICLO DE JUEGO  ####
    while i < len(items):  # 3
        ''' Va a jugar hasta que i = 3  '''
        
        # buscar la tecla presionada del modulo de eventos de pygame
        for evento in pygame.event.get():
            ''' evento = presionar una tecla o usar el mouse '''
            ''' evento.type = captura el boton tipeado '''
            if evento.type == QUIT:
                    pygame.quit()
                    return
                
            '''    
            if inicio == True:
                
              segundo el boton que toca
              
              cambiar la variable 
              
              NIVEL                
            '''
            if evento.type == KEYDOWN:
                    if inicio == False:
                        letra = dameLetraApretada(evento.key)
                        palabraUsuario += letra
                        if evento.key == K_BACKSPACE:
                            palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if evento.key == K_RETURN:
                        if inicio:
                            inicio = False  
                            # la funcion .fill limpia la pantalla
                            screen.fill(COLOR_FONDO)
                            pygame.mixer.music.load("sonidos/pacman.mp3")
                            pygame.mixer.music.play()
                        else:       
                            eleccionUsuario.append(palabraUsuario)
                            #chequea si es correcta y suma o resta puntos
                            sumar = esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)
                            puntos += sumar
                            palabraUsuario = ""
                            i = i+1                

        segundos = pygame.time.get_ticks() / 1000
        
        # PRESENTACION
        if inicio:
            dibujarPresentacion(screen, fondoPresentacion)
        # PARTIDA
        elif  i<len(items):            
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos, i, imgHoja)
        # RESPUESTAS
        else:        
            screen.fill(COLOR_FONDO)
            pygame.mixer.music.load("sonidos/marioMapa.mp3")
            pygame.mixer.music.play()
            
            eleccionCompu=juegaCompu(letraAzar, listaDeTodo, NIVEL)
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundos)
        pygame.display.flip()

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


# MAIN PRINCIPAL
if __name__ == "__main__":
    main()
    
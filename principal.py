#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  Laura Peralta, Luana Bertani, Lopez Gonzalo
  
  Universidad Nacional General Sarmiento
  
  Mayo 2020
'''

import math, os, random, sys
import pygame
import codecs
import math

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
    fondoPresentacion = pygame.image.load("imagenes/fondo2.png").convert_alpha()

    ##  CONSTANTES  ##
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p",
         "q","r","s","t","u","v","w","x","y","z"]    
    items=["paises", "colores", "animales"]    
    
    colores=[]
    paises=[]
    animales=[]
    
    listaDeTodo=[paises, colores, animales]
    
    #  ITEMS  #
    pais = codecs.open("items/paises.txt",  "r", "utf-8").read()
    color = codecs.open("items/colores.txt",  "r", "utf-8").read()
    animal = codecs.open("items/animales.txt",  "r", "utf-8").read()
    
    paises.append(pais)
    colores.append(color)
    animales.append(animal)
    
    listaDeTodo = cargarItems(listaDeTodo)
    print(listaDeTodo)
    
    jugar = True    
    reiniciar = True   
    
    ####  CICLO DE JUEGO  ####
    while jugar:
        if reiniciar:
            # Musica
            pygame.mixer.music.load("sonidos/tetris.mp3")
            pygame.mixer.music.play()

            # Tiempo total del juego
            gameClock = pygame.time.Clock()
            totaltime = 0
            fps = FPS_INICIAL
            
            # Controladores 
            presentacion = True
            habilitarReinicio = False
            reiniciar = False   
            ctaRegresiva = 1
            i = 0
            
            # Variables
            puntos = 0
            palabraUsuario=""
            eleccionUsuario=[]
            eleccionCompu=[]
            usuario = "..."
            aciertos = 0
            incorrectas = 0
            segundos = 0
            
            letraAzar = unaAlAzar(abc)

            
        while i < len(items):  
            # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            
            # buscar la tecla presionada del modulo de eventos de pygame
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()                
                    return
                if e.type == KEYDOWN:
                        if e.key == K_RETURN:             
                            if (len(palabraUsuario) > 0):
                                eleccionUsuario.append(palabraUsuario)
                                #chequea si es correcta y suma o resta puntos
                                sumar = esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)                                
                                puntos += sumar[0] + sumar[1]
                                
                                aciertos += sumar[0]
                                incorrectas += sumar[1]
                                
                                palabraUsuario = ""
                                i = i+1
                        if e.key == K_BACKSPACE:
                                palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                                
                        elif (e.key != K_RETURN and not presentacion):                                                
                            #letra = dameLetraApretada(e.key)                        
                            # e.unicode acepta ñ y tildes
                            letra = e.unicode                        
                            palabraUsuario += letra
                       
            '''
                Se comentó y rehizo la variable de segundos ya que no se reiniciaba entre partidas
            '''
            #segundos = pygame.time.get_ticks() / 1000
            segundos = (math.ceil((totaltime / 100)/10) - ctaRegresiva)
            
            if segundos > -1:
                presentacion = False  
    
            # limpiar pantalla anterior
            screen.fill(COLOR_FONDO)
            
            if presentacion:
                dibujarPresentacion(screen, fondoPresentacion, segundos)
            elif i<len(items):
                dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
            else:
                eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
                dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundos, usuario, aciertos, incorrectas)
                habilitarReinicio = True
            pygame.display.flip()
    
        while not reiniciar:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN:
                    if habilitarReinicio and e.key == K_RETURN: 
                            i = 0
                            reiniciar = True
    

if __name__ == "__main__":
    main()

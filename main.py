# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


ANCHO_VENTANA = 600
ALTO_VENTANA = 400

ANCHO_RAQUETA = 60
ALTO_RAQUETA = 10

ANCHO_OBJETO1 = 90
ALTO_OBJETO1 = 20

ANCHO_OBJETO2 = 90
ALTO_OBJETO2 = 20

ANCHO_OBJETO3 = 90
ALTO_OBJETO3 = 20

OBJETO1_STATE = True
OBJETO2_STATE = True
OBJETO3_STATE = True

LADO_PELOTA = 10

VELOCIDAD_RAQUETA = 5

raqueta_x = ANCHO_VENTANA/2 - ANCHO_RAQUETA/2
RAQUETA_Y = ALTO_VENTANA - ALTO_RAQUETA

OBJETO1_X = ANCHO_VENTANA/4 - ANCHO_OBJETO1/2
OBJETO1_Y = ALTO_VENTANA/4 
OBJETO2_X = ANCHO_VENTANA/2 - ANCHO_OBJETO2/2
OBJETO2_Y = ALTO_VENTANA/4 
OBJETO3_X = ANCHO_VENTANA - ANCHO_VENTANA/4 - ANCHO_OBJETO3/2 
OBJETO3_Y = ALTO_VENTANA/4 

pelota_x = ANCHO_VENTANA/2-LADO_PELOTA/2
pelota_y = ALTO_VENTANA-ALTO_RAQUETA-LADO_PELOTA

VELOCIDAD_PELOTA_X = 3
VELOCIDAD_PELOTA_Y = 3

TICS_SEGUNDO = 60

pausa_ticks = 1000 // TICS_SEGUNDO

#INICIAR PYGAME

pygame.init()

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA],0,32)
pygame.display.set_caption("Python_Arkanoid")


#BUCLE

pausa_pelota = 0

ON = True

while ON:

    tempo_0 = pygame.time.get_ticks()
    tecla_pulsada = pygame.key.get_pressed()
    #if tecla_pulsada[K_SPACE]:
    pausa_pelota = 1
    
    #PINTAR
    
    ventana.fill((0,0,0))

    imagen_raqueta = pygame.Rect(raqueta_x,RAQUETA_Y,ANCHO_RAQUETA,ALTO_RAQUETA)
    pygame.draw.rect(ventana, (255,255,255), imagen_raqueta)
    
    if  OBJETO1_STATE == True:
        imagen_objeto1 = pygame.Rect(OBJETO1_X,OBJETO1_Y,ANCHO_OBJETO1,ALTO_OBJETO1)
        pygame.draw.rect(ventana, (255,255,255), imagen_objeto1)
    
    if OBJETO2_STATE == True:
        imagen_objeto2 = pygame.Rect(OBJETO2_X,OBJETO2_Y,ANCHO_OBJETO2,ALTO_OBJETO2)
        pygame.draw.rect(ventana, (255,255,255), imagen_objeto2)
    
    if OBJETO3_STATE == True:
        imagen_objeto3 = pygame.Rect(OBJETO3_X,OBJETO3_Y,ANCHO_OBJETO3,ALTO_OBJETO3)
        pygame.draw.rect(ventana, (255,255,255), imagen_objeto3)
    
    imagen_pelota = pygame.Rect(pelota_x,pelota_y,LADO_PELOTA,LADO_PELOTA)
    pygame.draw.rect(ventana, (255,255,255), imagen_pelota)

    pygame.display.update()


    
#MOVIMIENTO RAQUETA
    
    #tecla_pulsada = pygame.key.get_pressed()
    if tecla_pulsada[K_RIGHT] and raqueta_x <= ANCHO_VENTANA - ANCHO_RAQUETA:
        raqueta_x = raqueta_x + VELOCIDAD_RAQUETA
    
    if tecla_pulsada[K_LEFT] and raqueta_x >= 0:
        raqueta_x = raqueta_x - VELOCIDAD_RAQUETA   
        
    
    #MOVIMIENTO PELOTA

    if pausa_pelota == 0:
        raqueta_x = ANCHO_VENTANA/2 - ANCHO_RAQUETA/2
        RAQUETA_Y = ALTO_VENTANA - ANCHO_RAQUETA
        pelota_x = ANCHO_VENTANA/2 - LADO_PELOTA/2
        pelota_y = ALTO_VENTANA - LADO_PELOTA*2
        OBJETO1_X = ANCHO_VENTANA/4 - ANCHO_OBJETO1/2
        OBJETO1_Y = ALTO_VENTANA/4 
        OBJETO2_X = ANCHO_VENTANA/2 - ANCHO_OBJETO2/2
        OBJETO2_Y = ALTO_VENTANA/4 
        OBJETO3_X = ANCHO_VENTANA - ANCHO_VENTANA/4 - ANCHO_OBJETO3/2 
        OBJETO3_Y = ALTO_VENTANA/4
        
    if pausa_pelota > 0:
        pelota_x += VELOCIDAD_PELOTA_X
        pelota_y -= VELOCIDAD_PELOTA_Y
    
    #COLISIONES
        # PELOTA CON LAS PAREDES
        
    if pelota_x <=0 or pelota_x >=ANCHO_VENTANA:
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X 

    if pelota_y <=0:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y

        #PELOTA CON LA RAQUETA

    if pelota_x<=raqueta_x + ANCHO_RAQUETA and pelota_x>=raqueta_x and pelota_y>=RAQUETA_Y - LADO_PELOTA and pelota_y<=RAQUETA_Y + ALTO_RAQUETA:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y        
        
        #PELOTA CON OBJETO1 POR ARRIBA
    if OBJETO1_STATE == True and pelota_x <= OBJETO1_X + ANCHO_OBJETO1 and pelota_x >= OBJETO1_X and pelota_y <= OBJETO1_Y +1 and pelota_y >= OBJETO1_Y:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y
        OBJETO1_STATE = False    
    
        #PELOTA CON OBJETO1 POR ABAJO
    if OBJETO1_STATE == True and pelota_x <= OBJETO1_X + ANCHO_OBJETO1 and pelota_x >= OBJETO1_X and pelota_y <= OBJETO1_Y + ALTO_OBJETO1 and pelota_y >= OBJETO1_Y + ALTO_OBJETO1 - ALTO_OBJETO1/15:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y
        OBJETO1_STATE = False  
        
        #PELOTA CON OBJETO1 POR DCHA
    if OBJETO1_STATE == True and pelota_x <= OBJETO1_X + ANCHO_OBJETO1 and pelota_x >= OBJETO1_X + ANCHO_OBJETO1 - ANCHO_OBJETO1/15 and pelota_y <= OBJETO1_Y + ALTO_OBJETO1 and pelota_y >= OBJETO1_Y:
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO1_STATE = False  
       
        #PELOTA CON OBJETO1 POR IZQ
    if OBJETO1_STATE == True and pelota_x <= OBJETO1_X + ANCHO_OBJETO1/15 and pelota_x >= OBJETO1_X and pelota_y <= OBJETO1_Y + ALTO_OBJETO1 and pelota_y >= OBJETO1_Y:    
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO1_STATE = False     
        
        #PELOTA CON OBJETO2 POR ARRIBA
    if OBJETO2_STATE == True and pelota_x <= OBJETO2_X + ANCHO_OBJETO2 and pelota_x >= OBJETO2_X and pelota_y <= OBJETO2_Y +1 and pelota_y >= OBJETO2_Y:    
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y
        OBJETO2_STATE = False  
        
        #PELOTA CON OBJETO2 POR ABAJO
    if OBJETO2_STATE == True and pelota_x <= OBJETO2_X + ANCHO_OBJETO2 and pelota_x >= OBJETO2_X and pelota_y <= OBJETO2_Y + ALTO_OBJETO2 and pelota_y >= OBJETO2_Y + ALTO_OBJETO2 - ALTO_OBJETO2/15:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y    
        OBJETO2_STATE = False  
        
        #PELOTA CON OBJETO2 POR DCHA
    if OBJETO2_STATE == True and pelota_x <= OBJETO2_X + ANCHO_OBJETO2 and pelota_x >= OBJETO2_X + ANCHO_OBJETO2 - ANCHO_OBJETO2/15 and pelota_y <= OBJETO2_Y + ALTO_OBJETO2 and pelota_y >= OBJETO2_Y:
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO2_STATE = False  
        
        #PELOTA CON OBJETO2 POR IZQ
    if OBJETO2_STATE == True and pelota_x <= OBJETO2_X + ANCHO_OBJETO2/15 and pelota_x >= OBJETO2_X and pelota_y <= OBJETO2_Y + ALTO_OBJETO2 and pelota_y >= OBJETO2_Y:    
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO2_STATE = False  
        
        #PELOTA CON OBJETO3 POR ARRIBA
    if OBJETO3_STATE == True and pelota_x <= OBJETO3_X + ANCHO_OBJETO3 and pelota_x >= OBJETO3_X and pelota_y <= OBJETO3_Y + 1 and pelota_y >= OBJETO3_Y:    
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y
        OBJETO3_STATE = False  
       
        #PELOTA CON OBJETO3 POR ABAJO
    if OBJETO3_STATE == True and pelota_x <= OBJETO3_X + ANCHO_OBJETO3 and pelota_x >= OBJETO3_X and pelota_y <= OBJETO3_Y + ALTO_OBJETO3 and pelota_y >= OBJETO3_Y + ALTO_OBJETO3 - ALTO_OBJETO3/15:
        VELOCIDAD_PELOTA_Y = -VELOCIDAD_PELOTA_Y    
        OBJETO3_STATE = False  
        #PELOTA CON OBJETO3 POR DCHA
    if OBJETO3_STATE == True and pelota_x <= OBJETO3_X + ANCHO_OBJETO3 and pelota_x >= OBJETO3_X + ANCHO_OBJETO3 - ANCHO_OBJETO3/15 and pelota_y <= OBJETO3_Y + ALTO_OBJETO3 and pelota_y >= OBJETO3_Y:
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO3_STATE = False  
        
        #PELOTA CON OBJETO3 POR IZQ
    if OBJETO3_STATE == True and pelota_x <= OBJETO3_X + ANCHO_OBJETO3/15 and pelota_x >= OBJETO3_X and pelota_y <= OBJETO3_Y + ALTO_OBJETO3 and pelota_y >= OBJETO3_Y:    
        VELOCIDAD_PELOTA_X = -VELOCIDAD_PELOTA_X
        OBJETO3_STATE = False  
        
        #REINICIO DEL JUEGO
    if pelota_y >= ALTO_VENTANA:
        OBJETO1_STATE = True
        OBJETO2_STATE = True
        OBJETO3_STATE = True 
        raqueta_x = ANCHO_VENTANA/2 - ANCHO_RAQUETA/2
        RAQUETA_Y = ALTO_VENTANA - ALTO_RAQUETA
        pelota_x = ANCHO_VENTANA/2-LADO_PELOTA/2
        pelota_y = ALTO_VENTANA-ALTO_RAQUETA-LADO_PELOTA -1
        
               
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.display.quit()
            ON = False
    
    tempo_frame = pygame.time.get_ticks() - tempo_0
    pygame.time.wait(max(0,pausa_ticks - tempo_frame))
    
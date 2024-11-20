
import pygame

from  random import randint

pygame.init()

#Inicializamos la ventana del Juego
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Pin Ball")

#Creamos el objeto Pelota
ball = pygame.image.load("img/Pelota.png")
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

#bucle principal del juego
jugando = True
while jugando:
    #Comprobamos los eventos

    #comprobamos si se ha pulsado el boton de cierre de ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    #muevo la pelota
    ballrect = ballrect.move(speed)

    #compruebo su la pelota toca el limite de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    #Se pinta la venta con un color

    #Esto borra los posibles elementos anteriores
    ventana.fill((255,255,255))
    ventana.blit(ball,ballrect)

    #Todos los elementos se vuelven a dibujar
    pygame.display.flip()

    #Controlamos la Frecuencia de Refresco(FPS)
    pygame.time.Clock().tick(60)
pygame.quit()
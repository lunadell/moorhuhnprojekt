import pygame
import random
import os
from factory import *
from settings import *




# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("My Game")

# create object
sprites = []
flederFactory = FlederFactory()

# pygame Clock
clock = pygame.time.Clock()

# GameLoop running?
running = True

fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn,random.randint(1000,2000))
while running:
    # Delta Time
    dt = clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == fledermaus_spawn:
            z = random.choice([1,2,3,4,5,6])
            x = random.randint(0,440)
            y = random.randint(0,340)

            #Rechtsflieger alle Größen      
            if z == 1: 
                sprites.append(flederFactory.createObjectAtPosition(x,y))
            elif z == 2:
                sprites.append(flederFactory.createObject2AtPosition(x,y)) 
            elif z == 3:
                sprites.append(flederFactory.createObject3AtPosition(x,y))

            #Linksflieger alle Größen           
            elif z == 4:
                sprites.append(flederFactory.createObject4AtPosition(x,y))     
            elif z == 5:
                sprites.append(flederFactory.createObject5AtPosition(x,y))                   
            elif z == 6:
                sprites.append(flederFactory.createObject6AtPosition(x,y))   
    # Update
    for sprite in sprites:
        sprite.update()

    # Render
    screen.fill((255, 255, 255))
    for sprite in sprites:
        screen.blit(sprite.getImage(), sprite.getRect())

    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
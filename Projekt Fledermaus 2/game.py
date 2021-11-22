import pygame
import random
import os
from factory import *
from settings import *




# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Cavebat")

clock = pygame.time.Clock()
counter  = 60
text = "60".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('freesansbold.tff', 44)




# create object
sprites = []
ballons = []
flederFactory = FlederFactory()
ballonFactory = BallonFactory()

# pygame Clock
clock = pygame.time.Clock()

# GameLoop running?
running = True

ballon_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(ballon_spawn,random.randint(1000,2000))

fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn,random.randint(1000,2000))


#Background 
size = (1700,750)  #Background size
bg_w, bg_h = size 
bg = pygame.transform.smoothscale(pygame.image.load('b.png'), (bg_w, bg_h)) 
pos_x = 0
speed = 4




while running:
    # Delta Time
    dt = clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter > 0:
              text = str(counter).rjust(3)  
            else: 
                text = ' Fertig' 
        if event.type == pygame.QUIT:
            running = False

             
        if event.type == ballon_spawn:
            x = random.randint(0, 440)
            y = 0

            ballons.append(ballonFactory.createBallonAtPosition(x,y))


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
    for ballon in ballons:
        ballon.update()

    for sprite in sprites:
        sprite.update()

    # Render
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_LEFT]:  
      pos_x += speed   
    elif  allKeys[pygame.K_RIGHT]:
      pos_x -= speed 
    else:
      pos_x += 0
      
    x_rel = pos_x % bg_w
    if x_rel > 0:
      x_part2 = x_rel - bg_w  
    else:
      x_part2 = x_rel + bg_w 
    screen.blit(bg, (x_rel,0))
    screen.blit(bg, (x_part2,0))
    
   
    for sprite in sprites:
        screen.blit(sprite.getImage(), sprite.getRect())

    for ballon in ballons:
        screen.blit(ballon.getImage(), ballon.getRect())

    screen.blit(font.render("Time: " + text, True, (255, 255, 255)), (10, 48))    
    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
clock.tick(60)

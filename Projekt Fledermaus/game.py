import pygame
import random
import os
from factory import *
from settings import *




# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Fledermaus")

#Background
size = (WIDTH,HEIGHT)  
bg_w, bg_h = size 
bg = pygame.transform.smoothscale(pygame.image.load('b.png'), (bg_w, bg_h)) 
pos_x = 0


# create object
sprites = []
ballons = []
flederFactory = FlederFactory()
ballonFactory = BallonFactory()

#Crosshair
player = Weapon1(30)

#Ammo

maxAmmo = 10
ammo = maxAmmo

# pygame Clock 
clock = pygame.time.Clock()
counter  = 10
text = "10".rjust(3)
pygame.time.set_timer(pygame.USEREVENT + 2, 1000)

# schriftart
font = pygame.font.SysFont('freesansbold.tff', 44)

munition = str(ammo).rjust(3)

# GameLoop running?
running = True

ballon_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(ballon_spawn,random.randint(10000,12000))

fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn,random.randint(1000,2000))



while running:
    # Delta Time
    dt = clock.tick(fps)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 2:
            counter -= 1
            if counter > 0:
              text = str(counter).rjust(3)  
            else: 
                text = ' Fertig'                 
        if event.type == pygame.QUIT:
            running = False

        #Spawn PowerUps
        if event.type == ballon_spawn:
            x = random.randint(0, WIDTH)
            y = 0

            ballons.append(ballonFactory.createBallonAtPosition(x,y))

        #Spawn Fledermäuse
        if event.type == fledermaus_spawn:
            z = random.choice([1,2,3,4,5,6])
            x = random.randint(0,WIDTH)
            y = random.randint(0,HEIGHT)

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



            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_click = pg.mouse.get_pressed()
                if mouse_click[0] == 1 and ammo > 0:
                    ammo -=1
                    munition = str(ammo).rjust(3)
                elif mouse_click[2] == 1:
                    ammo = maxAmmo
                    munition = str(ammo).rjust(3)
                else:
                    pass



    # Update

    for ballon in ballons:
        ballon.update()

    for sprite in sprites:
        sprite.update()

    player.update()


    # aktualisiere Anzige
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_LEFT]:  
      pos_x += KEY_SPEED  
    elif  allKeys[pygame.K_RIGHT]:
      pos_x -= KEY_SPEED  
    else:
      pos_x += 0
      
    x_rel = pos_x % bg_w
    if x_rel > 0:
      x_part2 = x_rel - bg_w  
    else:
      x_part2 = x_rel + bg_w 
    screen.blit(bg, (x_rel,0))
    screen.blit(bg, (x_part2,0))

    screen.blit(font.render("Time: " + text, True, WHITE), (10, 10))
    screen.blit(font.render("Munition: " + munition, True, WHITE), (WIDTH/2, HEIGHT/2))    

    # Double Buffering
    pygame.display.flip()
    
    player.update()
    

    # Render
    
    for sprite in sprites:
        screen.blit(sprite.getImage(), sprite.getRect())

    for ballon in ballons:
        screen.blit(ballon.getImage(), ballon.getRect())
    
    screen.blit(player.getImage(), player.getRect())

    # Double Buffering
    pygame.display.flip()

clock.tick(fps)
# Done! Time to quit.

pygame.quit()

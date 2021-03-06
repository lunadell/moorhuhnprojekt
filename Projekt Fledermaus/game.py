import pygame
import random
import os

from pygame import mouse
from factory import *
from settings import *

from Weapon import *
from collider import *




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

fledermaeuse = []
kurbese = []

flederFactory = FlederFactory()
kurbesFactory = KurbesFactory()

#Crosshair
player = Weapon1()

vier = player.getRect

# schriftart
font = pygame.font.SysFont('freesansbold.tff', 44)

#collider
collider = Collider()


#Ammo
ammo = MAXAMMO

Score = 0
score_anzeigen= font.render("Score: " + str(Score), True, WHITE)


# pygame Clock 
clock = pygame.time.Clock()
counter  = 10
text = "10".rjust(3)
pygame.time.set_timer(pygame.USEREVENT + 2, 1000)



# GameLoop running?
running = True

kurbes_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(kurbes_spawn,random.randint(10000,12000))

fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn,random.randint(1000,1500))

collider = Collider()

while running:
    # Delta Time
    dt = clock.tick(fps)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX,mouseY = event.pos
            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0] and ammo > 0:
                ammo -=1
            elif mouse_buttons[2]:
                ammo = MAXAMMO
        if ammo > 0:
            munition = font.render("Munition: "+ str(ammo),True, WHITE)
        else:
            munition = font.render("Munition: " + str(ammo), True, (238, 75, 43))

   
        if event.type == pygame.USEREVENT + 2:
            counter -= 1
            if counter > 0:
              text = str(counter).rjust(3)  
            else: 
                text = 'Fertig'                 
        if event.type == pygame.QUIT:
            running = False

        #Spawn PowerUps
        if event.type == kurbes_spawn:
            x = random.randint(0, WIDTH)
            y = 0

            kurbese.append(kurbesFactory.createKurbesAtPosition(x,y))

        #Spawn Flederm??use
        if event.type == fledermaus_spawn:
            z = random.choice([1,2,3,4,5,6])
            x = random.randint(0,WIDTH)
            y = random.randint(0,HEIGHT)


            #Rechtsflieger alle Gr????en      
            if z == 1:               
                fledermaeuse.append(flederFactory.createObjectAtPosition(x,y))
                
            elif z == 2:
                fledermaeuse.append(flederFactory.createObject2AtPosition(x,y)) 
                
            elif z == 3:
                fledermaeuse.append(flederFactory.createObject3AtPosition(x,y))
                

            #Linksflieger alle Gr????en           
            elif z == 4:
                fledermaeuse.append(flederFactory.createObject4AtPosition(x,y)) 
              
            elif z == 5:
                fledermaeuse.append(flederFactory.createObject5AtPosition(x,y))
                                   
            elif z == 6:
                fledermaeuse.append(flederFactory.createObject6AtPosition(x,y)) 
                
    

   
    for sprite in fledermaeuse:
        if collider.RectVsRect(sprite.getRect(),player.getRect()):
            print("Hit",sprite.getRect())

            fledermaeuse.remove(sprite)


   
    for sprite in fledermaeuse:
        if collider.RectVsRect(sprite.getRect(),player.getRect()):
            print("Hit",sprite.getRect())

            fledermaeuse.remove(sprite)




    # Update

    for kurbes in kurbese:
        kurbes.update()

    for sprite in fledermaeuse:
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
   
    screen.blit(munition, (WIDTH-300, HEIGHT-50))
    screen.blit(score_anzeigen, (10,100))

    # Double Buffering
    pygame.display.flip()
    
    player.update()
    

    # Render
    
    for sprite in fledermaeuse:
        screen.blit(sprite.getImage(), sprite.getRect())

    for kurbes in kurbese:
        screen.blit(kurbes.getImage(), kurbes.getRect())
    
    screen.blit(player.getImage(), player.getRect())

    # Double Buffering
    pygame.display.flip()

clock.tick(fps)

# Done! Time to quit.
pygame.quit()

import pygame
import random
import os
import time
from pygame import mouse
from factory import *
from settings import *

from weapon import *
from collider import *
from pygame import mixer


# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Fledermaus")


# Background
size = (WIDTH, HEIGHT)



# Images
bg = pygame.transform.smoothscale(Image('b.png').getImage(), (WIDTH, HEIGHT))
bg_Intro = pygame.transform.smoothscale(Image('Intro.png').getImage(), (WIDTH, HEIGHT))
bg_Intro2 = pygame.transform.smoothscale(Image('b2.png').getImage(), (WIDTH, HEIGHT))
feuer = pygame.transform.smoothscale(Image('f.png').getImage(), (WIDTH*0.9 , HEIGHT*0.4))



# Anfangposition der Sicht
pos_x = 0


# Audio
mixer.music.load("./sounds/Land-of-the-Dead.wav")
mixer.music.play(-1)

hit_sound = pg.mixer.Sound("./sounds/hit.wav")
reload_sound = pg.mixer.Sound("./sounds/reload.mp3")


time_to_blit = None
geschossen = False


# Create object
fledermaeuse = []
kurbese = []

flederFactory = FlederFactory()
kurbesFactory = KurbesFactory()

# Crosshair
player = Weapon1()


# Schriftart
font = pygame.font.SysFont('freesansbold.tff', 44)
myfont=pygame.font.SysFont("Britannic Bold", 100)
myfont1 = pygame.font.SysFont("Britannic Bold", 70)


# Collider
collider = Collider()


# Ammo
ammo = MAXAMMO
munition = font.render("Munition: "+ str(ammo),True, WHITE)


# Score
score = 0
score_anzeigen = font.render("score: " + str(score), True, WHITE)


# Pygame Clock
clock = pygame.time.Clock()
counter = SPIELLAUFZEIT
text = "-".rjust(3)
pygame.time.set_timer(pygame.USEREVENT + 2, 1000)



# Gameloop while ended
end_it = False
while (end_it == False):

    screen.blit(bg_Intro, (0, 0))
    Text1=myfont.render("welcome to the hell", 1, (RED))
    Text2 = myfont1.render("Click to start", 1, (WHITE))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            end_it = True

    screen.blit(Text1, (WIDTH * 0.16, HEIGHT * 0.25))
    screen.blit(Text2, (WIDTH * 0.2, HEIGHT - 200))
    pygame.display.flip()
    
    


# Events
kurbes_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(kurbes_spawn, random.randint(1000, 12000))

fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn, random.randint(1000, 1500))


# Gameloop
running = True
while running:

    # Mauszeiger verschwinden lassen
    pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))


    clock.tick(FPS)


    # Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            munition, ammo, geschossen = player.updateMuni(pygame.mouse.get_pressed(),ammo,font)
        
        if geschossen:
            time_to_blit = pygame.time.get_ticks() + 1
            geschossen = False

        if event.type == pygame.USEREVENT + 2:
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)
            else:
                not running

                end_it = False

                while (end_it == False):

                    screen.blit(bg_Intro2, (0, 0))
                    Text1 = myfont.render("Score: " + str(score), 1, (RED))
                    Text2 = myfont1.render("press space to restart", 1, (WHITE))
                    for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    counter = SPIELLAUFZEIT
                                    score = 0
                                    score_anzeigen = font.render("score: " + str(score), True, WHITE)
                                    screen.blit(score_anzeigen, (10, 100))
                                    end_it = True

                    screen.blit(Text1, (WIDTH * 0.5 , HEIGHT * 0.25))
                    screen.blit(Text2, (WIDTH * 0.3, HEIGHT - 200))
                    
                    pygame.display.flip()


        if event.type == pygame.QUIT:
            running = False

        # Spawn PowerUps
        if event.type == kurbes_spawn:
            x = random.randint(0, WIDTH)
            y = 0

            kurbese.append(kurbesFactory.createKurbesAtPosition(x, y))

        # Spawn Fledermäuse
        if event.type == fledermaus_spawn:
            y = random.randint(0, HEIGHT)

            # Rechtsflieger alle Größen
            fledermaeuse.append(flederFactory.createRandomObject(y))


    for sprite in fledermaeuse:
        mouse_buttons = pygame.mouse.get_pressed()
        if collider.RectVsRect(sprite.getRect(), player.getRect()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_buttons[0] and ammo > 0:
                    # print("Hit", sprite.getRect())

                    fledermaeuse.remove(sprite)
                    hit_sound.play()
                    for fledermaus in fledermaeuse:
                        fledermaus.sterben(screen)
                    score += 5
                    score_anzeigen = font.render(
                        "score: " + str(score), True, WHITE)



    for sprite in kurbese:
        mouse_buttons = pygame.mouse.get_pressed()
        if collider.RectVsRect(sprite.getRect(), player.getRect()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_buttons[0] and ammo > 0:
                    # print("Hit", sprite.getRect())
                    kurbese.remove(sprite)

                    # Alle Fledermäuse halbschnell
                    n_speed = random.choice([SLOWMOW,SPEEDUP])
                    for fledermaus in fledermaeuse:
                        fledermaus.neueSpeed(n_speed)
                        
                    # Hier die powerUps rein


    # Update

    for kurbes in kurbese:
        kurbes.update()

    for sprite in fledermaeuse:
        sprite.update()

    player.update()


    # Aktualisiere Anzige
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_LEFT]:
        pos_x += KEY_SPEED
    elif allKeys[pygame.K_RIGHT]:
        pos_x -= KEY_SPEED
    else:
        pos_x += 0

    x_rel = pos_x % WIDTH
    if x_rel > 0:
        x_part2 = x_rel - WIDTH
    else:
        x_part2 = x_rel + WIDTH

    screen.blit(bg, (x_rel, 0))
    screen.blit(bg, (x_part2, 0))




    # Render
    for sprite in fledermaeuse:

        # CK: Das ist neu
        sprite.render(screen)

    for kurbes in kurbese:
        screen.blit(kurbes.getImage(), kurbes.getRect())

    screen.blit(player.getImage(), player.getRect())




    if time_to_blit:
        screen.blit(feuer, (WIDTH * 0.2, HEIGHT * 0.8))
        if pygame.time.get_ticks() >= time_to_blit:
            time_to_blit = None

    screen.blit(font.render("Time: " + text, True, WHITE), (10, 10))

    screen.blit(munition, (WIDTH * 0.85 , HEIGHT * 0.9))
    screen.blit(score_anzeigen, (10, 100))

    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()

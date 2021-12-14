import os
import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *
import pygame
import random
import time
from pygame import mixer
pygame.init()
pygame.mixer.init()


shot_sound = pg.mixer.Sound("sounds/shot.wav")
reload_sound = pg.mixer.Sound("./sounds/reload.mp3")



class IWeapon():
    def __init__(self):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        self.image = pg.image.load(os.path.join(
                img_folder, 'crosshair1.png')).convert_alpha()

        self.rect = self.image.get_rect()
        

    def getRect(self):
        return self.rect

    def getImage(self):
        return self.image
        
    def update(self):
        self.rect.center = (pg.mouse.get_pos())
        
        
    def updateMuni(self, mouse_buttons, ammo, font):

        geschossen = False
        
        if mouse_buttons[0] and ammo > 0:
 
            ammo -=1
            shot_sound.play()
            geschossen = True

        elif mouse_buttons[2]:
                ammo = MAXAMMO
                reload_sound.play()

        if ammo > 0:
            munition = font.render("Munition: "+ str(ammo),True, WHITE)
        else:
            munition = font.render("Munition: " + str(ammo), True, RED)

        return munition, ammo, geschossen
        


class Weapon1 (IWeapon):
    
    pass
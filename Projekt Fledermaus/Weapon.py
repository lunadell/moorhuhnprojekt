import os
import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *
import random

class IWeapon():
    def __init__(self, ammo: int):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        self.image = pg.image.load(os.path.join(
                img_folder, 'crosshair1.png')).convert_alpha()

        self.rect = self.image.get_rect()

        self.maxAmmo = ammo
        self.currentAmmo = self.maxAmmo

        self.klick = pg.mouse.get_pressed()


    def getRect(self):
        return self.rect

    def getImage(self):
        return self.image
        
  
    def update(self):
    
        self.rect.center = (pg.mouse.get_pos())
        
        if self.klick[0] == 1 and self.currentAmmo > 0:
            self.currentAmmo -= 1

        elif self.klick[2]== 1:
            delay(3000)
            self.currentAmmo = self.maxAmmo

        else:
            pass
        
        

class Weapon1 (IWeapon):
    
    pass
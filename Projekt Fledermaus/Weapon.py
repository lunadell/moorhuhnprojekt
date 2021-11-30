import os
import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *
import random


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
 
        
        

class Weapon1 (IWeapon):
    
    pass
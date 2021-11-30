import os
import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *
import random
from Weapon import *


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class FliegendesObjekt(Sprite):

    def verschwinden():
        pass

    def update():
        pass


class Fledermaus(FliegendesObjekt):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['fleder1']
        self.imageIndex = 1
        print(id(self.flyweightImages))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.sx = sx
        self.sy = sy

        # Fleder Speed
        self.maxtimer = FLEDERSPEED
        self.timer = 0


    def update(self):

        self.rotate()
        self.x = self.x + self.sx

        self.y = self.y
        self.rect.center = (self.x, self.y)

        allKeys = pg.key.get_pressed()
        if allKeys[pg.K_LEFT]:  
         self.x += KEY_SPEED
        elif  allKeys[pg.K_RIGHT]:
          self.x -= KEY_SPEED
      
        self.rect.center = (self.x, self.y)
    

        # if (self.rect.bottom >= HEIGHT):
        #     self.sy = self.sy * -1

        # if (self.rect.right >= WIDTH):
        #     self.sx = self.sx * -1

        # if (self.rect.left <= 0):
        #     self.sx = self.sx * -1

        # if (self.rect.top <= 0):
        #     self.sy = self.sy * -1


    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 4):
                self.imageIndex = 1
            self.image = self.flyweightImages['fleder'+str(self.imageIndex)]

    def verschwinden(self):
        pass




class IPowerUp(FliegendesObjekt):

    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['kurbes1']
        self.imageIndex = 1
        print(id(self.flyweightImages))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.sx = sx
        self.sy = sy

        self.maxtimer = KURBESSPEED
        self.timer = 0


    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 5):
                self.imageIndex = 1
            self.image = self.flyweightImages['kurbes'+str(self.imageIndex)]


    def update(self):
        self.rotate()
        self.x = self.x
        allKeys = pg.key.get_pressed()
        if allKeys[pg.K_LEFT]:  
         self.x += KEY_SPEED
        elif  allKeys[pg.K_RIGHT]:
          self.x -= KEY_SPEED
        self.y = self.y + self.sy
        self.rect.center = (self.x, self.y)



class SlowMotion(IPowerUp):

    def update(self):
        IPowerUp.update(self)
        
    

    def verschwinden():
        pass


class UnlmtAmmo(IPowerUp):
    def update(self):
        IPowerUp.update(self)


class StrongWeapen(IPowerUp):

    def update(self):
        IPowerUp.update(self)



        







import os
import pygame as pg
from settings import *
import random

class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class FliegendesObjekt(Sprite):
    def fliegen():
        pass

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
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy

        # Fleder Speed
        self.maxtimer = COINSPEED
        self.timer = 0

    def update(self):
        self.rotate()
        self.x = self.x + self.sx
        self.y = self.y 
        self.rect.topleft = (self.x, self.y)

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

class Ballon(FliegendesObjekt):
    def __init__(self, flyweightImages: dict, x: int, y: int,sy:int,imagename: str):
        Sprite.__init__(self,x,y,imagename)
        self.sy = sy

    def update(self):
        pass
    def verschwinden(self):
        pass


class IPowerUp():
    
    def update(self):
        pass

class SlowMotion(IPowerUp):
    def update(self):
        pass

class UnlmtAmmo(IPowerUp):
    def update(self):
        pass

class StrongWoepen(IPowerUp):
    def update(self):
        pass




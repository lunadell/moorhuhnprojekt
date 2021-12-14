import os
import pygame as pg
from pygame import surface
from pygame.time import *
from flyweight import *
from settings import *
import random
from weapon import *


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

    def verschwinden(self):
        raise NotImplementedError


class Fledermaus(Sprite):
    def __init__(self, todesDict: dict, flyweightImages: dict, y: int, sx: int, groesse):
        if sx > 0:
            self.x = 0
        else:
            self.x = WIDTH
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['fleder1']
        self.todesDict = todesDict
        self.imageIndex = 1
        print(id(self.flyweightImages))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.sx = sx
        self.speed = 1
        self.todesSnap = self.todesDict['tot1']

        # Fleder Speed
        self.maxtimer = FLEDERSPEED
        self.timer = 0
        self.last_timer = pg.time.get_ticks()
        self.laengeTimer = 2000
        self.geschwindigkeit = False


        # CK: Das ist neu
        self.groesse = groesse

    def update(self):

        self.rotate()

        # Check Time
        if pg.time.get_ticks() - self.last_timer > self.laengeTimer:
            self.speed = 1
            self.geschwindigkeit = False

        if self.geschwindigkeit:
            
            if self.speed == SLOWMOW:
                #spiele guten Sound
                pass
            elif self.speed == SPEEDUP:
                #spiele "MUHAHAH"
                pass

            self.x = self.x + self.sx * self.speed
            
        else:
            self.x = self.x + self.sx


        self.y = self.y
        self.rect.center = (self.x, self.y)

        allKeys = pg.key.get_pressed()
        if allKeys[pg.K_LEFT]:
            self.x += KEY_SPEED
        elif allKeys[pg.K_RIGHT]:
            self.x -= KEY_SPEED

        self.rect.center = (self.x, self.y)

    def neueSpeed(self, n_speed):

        self.speed = n_speed
        self.geschwindigkeit = True
        self.last_timer = pg.time.get_ticks()




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

    # CK: Das ist neu
    def render(self, screen):
        blit_image = pg.transform.scale(self.image, self.groesse)
        if self.sx < 0:
            blit_image = pg.transform.flip(blit_image, True, False)
        screen.blit(blit_image, self.rect)


    def sterben(self, screen):
        blit_image = pg.transform.scale(self.todesSnap, self.groesse)
        if self.sx < 0:
            blit_image = pg.transform.flip(blit_image, True, False)
        screen.blit(blit_image, self.rect)


class IPowerUp(Sprite):

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
        elif allKeys[pg.K_RIGHT]:
            self.x -= KEY_SPEED
        self.y = self.y + self.sy
        self.rect.center = (self.x, self.y)

    def magic(self):
        pass


class NewSpeed(IPowerUp):

    def update(self):
        IPowerUp.update(self)

    def magic(self):
        pass

    def verschwinden():
        pass


class SpeedUp(IPowerUp):
    def update(self):
        IPowerUp.update(self)


class StrongWeapen(IPowerUp):

    def update(self):
        IPowerUp.update(self)




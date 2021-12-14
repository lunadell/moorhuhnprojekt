from settings import *
from sprites import *
from flyweight import *
import pygame as pg
import random
from weapon import *

pg.display.set_caption("Moorhuhn")


class FlederFactory:
    def __init__(self):
        self.imageDict = ImageFlyweight().getFlyweightImages()
        self.imageDead = ImageFlyweight().getFlyweightImagesDead()

    
    def createRandomObject(self, y):
        
        choice1 = random.choice([-1, 1])
        choice2 = random.choice([0.7, 0.3])
        groesse = random.choice([(93,54), (186, 108), (47, 27)])
        return Fledermaus(self.imageDead, self.imageDict, y, SPEED * choice1 * choice2, groesse)


    def getImageDict(self):
        print(self.imageDict)


class KurbesFactory:
    def __init__(self):
        self.image = ImageFlyweight().getFlyweightImagesKurbes()

    def createKurbesAtPosition(self, x, y):
        

        return NewSpeed(self.image, x, y, x, FLUG * 0.5)

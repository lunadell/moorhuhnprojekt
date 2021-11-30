from settings import *
from sprites import *
from flyweight import *
import pygame as pg
import random
from Weapon import *

pg.display.set_caption("Moorhuhn")

class FlederFactory:
    def __init__(self):
        self.imageDict = ImageFlyweight().getFlyweightImages()
        self.imageDict2 = ImageFlyweight().getFLyweightImages2()
        self.imageDict3 = ImageFlyweight().getFLyweightImages3()

        #Linksflieger
        self.imageDict4 = ImageFlyweight().getFLyweightImages4()
        self.imageDict5 = ImageFlyweight().getFLyweightImages5()
        self.imageDict6 = ImageFlyweight().getFLyweightImages6()



    def createObjectAtPosition(self, x, y):
                            
        object1 = Fledermaus(self.imageDict, x, y, SPEED * random.choice([0.7,  0.3]),
                   SPEED * random.choice([1,  0.5]))
        
        return object1


    def createObject2AtPosition(self, x, y):
                   
        object2 = Fledermaus(self.imageDict2, x , y, SPEED * random.choice([0.7,  0.3]),
            SPEED * random.choice([1,  0.5]))

        return object2

    def createObject3AtPosition(self, x, y):
                   
        object3 = Fledermaus(self.imageDict3, x , y, SPEED * random.choice([0.7,  0.3]),
            SPEED * random.choice([1,  0.5]))

        return object3        


    #Ab hier Linksflieger

    def createObject4AtPosition(self, x, y):
                   
        object4 = Fledermaus(self.imageDict4, x , y, SPEED * random.choice([-0.7,  -0.3]),
            SPEED * random.choice([-1,  -0.5]))

        return object4

    def createObject5AtPosition(self, x, y):
                   
        object5 = Fledermaus(self.imageDict5, x , y, SPEED * random.choice([-0.7,  -0.3]),
            SPEED * random.choice([-1,  -0.5]))

        return object5

    def createObject6AtPosition(self, x, y):
                   
        object6 = Fledermaus(self.imageDict6, x , y, SPEED * random.choice([-0.7,  -0.3]),
            SPEED * random.choice([-1,  -0.5]))

        return object6        

class KurbesFactory:
    def __init__(self):
        self.image = ImageFlyweight().getFlyweightImagesKurbes()

    def createKurbesAtPosition(self,x,y):
        
        kurbes = SlowMotion(self.image, x, y, x, FLUG * 0.5 )

        return kurbes


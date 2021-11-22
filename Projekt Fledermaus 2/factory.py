from settings import *
from sprites import *
from flyweight import *
import pygame as pg
import random
import pygame
from pygame.display import update


pygame.display.set_caption("Moorhuhn")




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
                            
        ball1 = Fledermaus(self.imageDict, x, y, SPEED * random.choice([1,  0.5]),
                   SPEED * random.choice([1,  0.7]))
        
        return ball1


    def createObject2AtPosition(self, x, y):
                   
        ball2 = Fledermaus(self.imageDict2, x , y, SPEED * random.choice([1,  0.5]),
            SPEED * random.choice([1,  0.7]))

        return ball2

    def createObject3AtPosition(self, x, y):
                   
        ball3 = Fledermaus(self.imageDict3, x , y, SPEED * random.choice([1,  0.5]),
            SPEED * random.choice([1,  0.7]))

        return ball3        


    #Ab hier Linksflieger

    def createObject4AtPosition(self, x, y):
                   
        ball4 = Fledermaus(self.imageDict4, x , y, SPEED * random.choice([-1,  -0.5]),
            SPEED * random.choice([-1,  -0.7]))

        return ball4

    def createObject5AtPosition(self, x, y):
                   
        ball5 = Fledermaus(self.imageDict5, x , y, SPEED * random.choice([-1,  -0.5]),
            SPEED * random.choice([-1,  -0.7]))

        return ball5

    def createObject6AtPosition(self, x, y):
                   
        ball6 = Fledermaus(self.imageDict6, x , y, SPEED * random.choice([-1,  -0.5]),
            SPEED * random.choice([-1,  -0.7]))

        return ball6        

class BallonFactory:
    def __init__(self):
        self.image = ImageFlyweight().getFlyweightImagesBallon()

    def createBallonAtPosition(self,x,y):
        x = random.randint(1,1500)
        ballon = SlowMotion(self.image, x, y, x, FLUG * 0.5 )
        return ballon

             

       
        
        

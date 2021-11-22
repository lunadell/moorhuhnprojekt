import os
import pygame as pg

class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageFlyweight:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # Make Dictionary of Images
        self.images = {}
        self.images2 = {}
        self.images3 = {}
        
        #Linksflieger
        self.images4 = {}
        self.images5 = {}
        self.images6 = {}

        self.imageBallon = {}

        #Kürbis
        for i in range(1, 5):
            self.imageBallon['kurbes'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'kurbes'+str(i)+'.png')).convert_alpha()


        #Rechtsflieger
        
        #klein
        for i in range(1, 4):
            self.images['fleder'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha()

        #mittel
        for i in range(1,4):
            self.images2['fleder'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha(), (54,60))
        #groß
        for i in range(1,4):
            self.images3['fleder'+str(i)] =pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha(), (81,90))                              


        #Linksflieger
        #klein
        for i in range(1,4):
            self.images4['fleder'+str(i)] =pg.transform.flip(pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha(),True, False)    

        #mittel
        for i in range(1,4):
            self.images5['fleder'+str(i)] =pg.transform.flip(pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha(), (54,60)),True, False) 

        #groß
        for i in range(1,4):
            self.images6['fleder'+str(i)] =pg.transform.flip(pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha(), (81,90)),True, False) 


    def getFlyweightImages(self):
        return self.images

    def getFLyweightImages2(self):
        return self.images2

    def getFLyweightImages3(self):
        return self.images3

    #Linkflieger
    
    def getFLyweightImages4(self):
        return self.images4

    def getFLyweightImages5(self):
        return self.images5

    def getFLyweightImages6(self):
        return self.images6


    #PowerUp
    def getFlyweightImagesBallon(self):
        return self.imageBallon
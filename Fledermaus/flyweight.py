import os
import pygame as pg
import random



class Image:
    def __init__(self, image):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        self.image = pg.image.load(os.path.join(img_folder, image)).convert_alpha()

    def getImage(self):
        return self.image


class ImageFlyweight:
    def __init__(self):
        # Initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        # Make Dictionary of Images
        self.images = {}
        self.imagesDead = {}

        # Kurbes bzw. Kürbis
        self.imageKurbes = {}

        # Kürbis
        for i in range(1, 5):
            self.imageKurbes['kurbes'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'kurbes'+str(i)+'.png')).convert_alpha()

        # Fledermäuse
        for i in range(1, 5):
            self.images['fleder'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha()

        # Tote Fledermäuse
        for i in range(1, 2):
            self.imagesDead['tot'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'tot'+str(i)+'.png')).convert_alpha()


    # Fledermaus
    def getFlyweightImages(self):
        return self.images


    # PowerUp
    def getFlyweightImagesKurbes(self):
        return self.imageKurbes

    # Tot Fledermäuse
    def getFlyweightImagesDead(self):
        return self.imagesDead

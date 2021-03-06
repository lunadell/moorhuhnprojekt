import os
import pygame as pg

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
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)
        self.sx = sx

    def update(self):
        pass

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

class StrongWeapon(IPowerUp):
    def update(self):
        pass



class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageFlyweight:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img')
        # Make Dictionary of Images
        self.images = {}
        self.images["ball"] = pg.image.load(os.path.join(
            img_folder, 'ball.png')).convert_alpha()

        for i in range(1, 9):
            self.images['coin'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'coin'+str(i)+'.png')).convert_alpha()

    def getFlyweightImages(self):
        return self.images










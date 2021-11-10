import pygame as pg
from sprites import *

class IWeapon(Sprite):

    
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int, diameter: int):
        Sprite.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)
        self.ammo = ammo
        self.diameter = diameter

    def update(self, event_list): # event list?
        # Move crosshair based on mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

        ## Kill enemy

        for event in event_list:
        # IF mouseclick, then
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                # CHECK for Ammunition
                if self.ammo > 0:
                    # Move crosshair for recoil effect
                    
                    # minus one ammo
                    pass

                    ''' Mediator ?'''  
                    #IF Crosshair overlap Enemy, then kill
                    # mind: accuracy?
                    if self.rect.collidepoint(event.pos):
                        pass
                       

                # IF Ammunition empty, no shot/kill
                if self.ammo == 0:
                    pass
                    # Minimal Movement crosshair for "stuck" recoil effect
            

        
# Default weapon / crosshair (1)
class Weapon1(IWeapon):

    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int):
        ammo = 10
        diameter = 10
        
        IWeapon.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)

        self.image = self.flyweightImages['crosshair1']
    
    
# Power-Up Only weapon / crosshair (2)
class Weapon2(IWeapon):
    
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int):
        ammo = 15
        diameter = 15

        IWeapon.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)

        self.image = self.flyweightImages['crosshair2']
    

   


            



   
class IWeapon(Sprite):

    
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int, diameter: int):
        Sprite.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)
        self.ammo = ammo
        self.diameter = diameter

    def update(self):
        # Move crosshair based on mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

        ## Kill enemy

        # IF mouseclick, then
        if event.type == pygame.MOUSEBUTTONDOWN:
           
            # CHECK for Ammunition
            if self.ammo < 0:
                # Move crosshair for recoil effect
                
                # minus one ammo
                pass

                #IF Crosshair overlap Enemy, then kill

                ''' Mediator ?'''     

            #IF Ammunition empty, no shot/kill
            # Minimal Movment crosshair for "stuck" recoil effect
            

        

class Weapon1(IWeapon):
    #crosshair1
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int):
        ammo = 10
        diameter = 10
        
        IWeapon.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)

        self.image = self.flyweightImages['crosshair1']
    
    
    
class Weapon2(IWeapon):
    #crosshair2
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, ammo: int):
        ammo = 15
        diameter = 15

        IWeapon.__init__(self, flyweightImages: dict, x: int, y: int, imagename: str)

        self.image = self.flyweightImages['crosshair2']
    

   


            



   
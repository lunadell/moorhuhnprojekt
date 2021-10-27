class IWeapon(Sprite):
    
    def update(self):
        # Move crosshair based on mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

        if self.shoot:
            # Move crosshair for recoil effect
            pass
            
            ## Kill enemy
            ''' Mediator'''
            # Check for Ammunition

            #If Ammo empty, no shot/kill
            

            #If Hair overlap Enemy, then kill
    


class Weapon1(IWeapon):
    pass
    

class Weapon2(IWeapon):
    pass


            



   
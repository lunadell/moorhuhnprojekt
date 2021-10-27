class Crosshair(pygame.sprite.Sprite):
     #  Crosshair.png as provided by : CC0 - Public Domain Donation by hackcraft.de

    def update(self):
        # Move crosshair based on mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

        if self.shoot:
            # Move crosshair for recoil effect
            pass
            
            # Kill enemy
        
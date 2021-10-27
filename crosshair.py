class crosshair(pygame.sprite.Sprite):
    
    def update(self):
        # Move crosshair based on mouse position
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shoot:
            # Move crosshair for recoil effect
            pass
            
            # Kill enemy
import pygame

#init
pygame.init()
screen_size = (1500,750)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Moorhuhn")
clock = pygame.time.Clock()

#Background 
size = (3400,750)  #Background size
bg_w, bg_h = size 
bg = pygame.transform.smoothscale(pygame.image.load('b.png'), (bg_w, bg_h)) 

#player
class spieler:
    def __init__(self, name):
        self.name = name
        self.score = 0   
        self.pos_x = 0  #position
        self.speed = 13   # wie schnell man die Kamera scrollt

    def bewegen(self):
     global bg
     allKeys = pygame.key.get_pressed()
     #nach links scrollen: (position + speed)
     if allKeys[pygame.K_LEFT]:  
          self.pos_x += self.speed
          pass 
      #nach rechts scrollen: (position - speed)   
     elif  allKeys[pygame.K_RIGHT]:
          self.pos_x -= self.speed 
          pass
      #wenn nichts gedruckt wird, bleibt die Position unverändert  
     else:
          self.pos_x += 0
          pass
      #endlose Scrolling 360 grad    
     x_rel = self.pos_x % bg_w
     if x_rel > 0:
        x_part2 = x_rel - bg_w  
     else:
        x_part2 = x_rel + bg_w
     
     #der Background wird 2 mal gezeichnet, um die Scrolling 360 grad zu ermöglichen
     screen.blit(bg, (x_part2,0))
     screen.blit(bg, (x_rel,0))   


    #Funktion Score anzeigen
    def show_score(self):
     font = pygame.font.SysFont('freesansbold.tff', 44)
     White_Color = 255,255,255
     score = font.render("Score: " + str(self.score) , True,White_Color )
     screen.blit(score,(10,10)) 

    #Erhöung der Score pro Kill
    def Score_kills (self):
        self.score += 5

#Beispiel
player = spieler("name") 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Background and side scrolling auf dem Bildschirm: 
    player.bewegen() 
   
#Score anzeigen auf dem Bildschirm    
    player.show_score()

    pygame.display.flip() 
    pygame.display.quit 


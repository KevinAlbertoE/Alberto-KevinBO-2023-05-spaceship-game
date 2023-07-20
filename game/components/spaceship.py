import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    IMAGE_WIDTH = 40
    IMAGE_HEIGTH = 60
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500
    
    def __init__(self):
        
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.IMAGE_WIDTH, self.IMAGE_HEIGTH))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player' 
        
    def update(self, game, user_input):
        self.shoot(game.bullet_manager, user_input)
        if user_input[pygame.K_LEFT]: #and self.rect.left > 0:
            self.rect.x -= 10
            if self.rect.left < 0:
                self.rect.right = SCREEN_WIDTH  
        elif user_input[pygame.K_RIGHT]:# and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
            if self.rect.right > SCREEN_WIDTH:
                self.rect.left = SCREEN_WIDTH - SCREEN_WIDTH
        elif user_input[pygame.K_UP] and self.rect.top > 200: 
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
#        elif user_input[pygame.K_q] and self.rect.y > 200:
 #           self.rect.x -= 10
  #          self.rect.y -= 10
   #         if self.rect.left < 0:
    #            self.rect.right = SCREEN_WIDTH    
     #   elif user_input[pygame.K_e] and self.rect.y > 200:
      #      self.rect.x += 10
       #     self.rect.y -= 10      
        #    if self.rect.right > SCREEN_WIDTH:
         #       self.rect.left = SCREEN_WIDTH - SCREEN_WIDTH
#        elif user_input[pygame.K_x] and self.rect.bottom < SCREEN_HEIGHT:
 #           self.rect.x += 10
  #          self.rect.y += 10
   #         if self.rect.left > SCREEN_WIDTH:
    #            self.rect.right = SCREEN_WIDTH - SCREEN_WIDTH
     #   elif user_input[pygame.K_z] and self.rect.bottom < SCREEN_HEIGHT:
      #      self.rect.x -= 10
       #     self.rect.y += 10
        #    if self.rect.right < 0:
         #       self.rect.left = SCREEN_WIDTH               
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def shoot(self, bullet_manager, user_input):
        if user_input[pygame.K_v]:
            bullet = Bullet(self) # el parametro de spaceship que se pide en la clase lo enviamos aqui
            bullet_manager.add_bullet(bullet)

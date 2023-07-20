import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT
#from game.components.enemies.enemy import Enemy
#from game.components.enemies.enemy_manager import EnemyManager

class Bullet(Sprite):
    PLAYER_IMAGE = pygame.transform.scale(BULLET, (10, 20))
    ENEMY_IMAGE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BULLET_TYPES = { 'player': PLAYER_IMAGE, 'enemy': ENEMY_IMAGE }
    SPEED = 10

    def __init__(self, spaceship):
        self.image = self.BULLET_TYPES[spaceship.type]# espaceship.type devuelve un "player" or "enemy"
        # 1 averiguar de donde le envian spaceship (spasehip le envian desde la clase spaceship or la clase enemigo)
        self.rect = self.image.get_rect(center = spaceship.rect.center)# es igual a decir que aparecera en enemy o player en el centro
        self.owner = spaceship.type# devuelve texto (enemy or player)

    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += 10
            
        else:
             self.owner == 'player'
             self.rect.y -= 10  
             #if self.rect.colliderect(Enemy.rect):
              #  EnemyManager.delete_enemy()
                   

        # aqui hay que poner una condicional para que el movimiento varie de ariba a abajo
        #self.rect.y += 10# bullets es una lista entonces en donde le pasamos la lista tenemos que añadir una condicional para ver que lista enviamos

        if self.rect.top > SCREEN_HEIGHT: #añadir condicional para eliminar si es que la bala del player es < o se elimine
            bullets.remove(self)
        elif self.rect.top < 0:
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
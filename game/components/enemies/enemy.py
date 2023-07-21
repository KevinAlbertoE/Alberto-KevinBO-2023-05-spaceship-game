import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet
#from game.components.spaceship import Spaceship


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
   # SPEED_ON_Y = 1
    #SPEED_ON_X = 10
    MOVES = { 0: 'left', 1: 'right', 2: 'down'}
    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 3000
   # ENEMY_IMG = [ENEMY_1, ENEMY_2, ENEMY_3]
    def __init__(self, image, speed_on_x, speed_on_y):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 2)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.speed_on_x = speed_on_x
        self.speed_on_y = speed_on_y
        self.type = 'enemy'
        current_time = pygame.time.get_ticks()
        self.shooting_time = random.randint(current_time + self.INITIAL_SHOOTING_TIME, current_time + self.INITIAL_SHOOTING_TIME)

    def update(self, enemies, game):
        #self.rect.y += self.SPEED_ON_
        self.shoot(game.bullet_manager)

        if self.direction == self.MOVES[0]:
            self.rect.y += self.speed_on_y
            self.rect.x -= self.speed_on_x


        elif self.direction == self.MOVES[1]:
            self.rect.x += self.speed_on_x
            self.rect.y += self.speed_on_y
        
        elif self.direction == self.MOVES[2]:
            self.rect.y += self.speed_on_y
    #    if self.image.colliderect(Bullet) and Bullet.owner ==  Spaceship.type:
     #       game.bullet_manager.remove(Bullet)


        self.handle_direction()
        if self.rect.top > SCREEN_HEIGHT: #or self.rect.bottom < 0:
            enemies.remove(self)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
            self.speed_on_y += 1
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[2]:
            self.speed_on_y += 10
            if self.rect.bottom > SCREEN_HEIGHT / 2:
                self.speed_on_y = -5
                self.direction = self.MOVES[0]                
        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()

        if self.shooting_time <= current_time:
            bullet = Bullet(self)#crear una bala para simismo
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)        
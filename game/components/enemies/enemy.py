import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, ENEMY_3, ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = 1
    SPEED_ON_X = 10
    MOVES = { 0: 'left', 1: 'right', 2: 'down'}
    ENEMY_IMG = [ENEMY_1, ENEMY_2, ENEMY_3]
    def __init__(self):
        self.image = random.choice(self.ENEMY_IMG)
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 2)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)

    def update(self, enemies):
        #self.rect.y += self.SPEED_ON_Y

        if self.direction == self.MOVES[0]:
            self.rect.y += self.SPEED_ON_Y
            self.rect.x -= self.SPEED_ON_X


        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X
            self.rect.y += self.SPEED_ON_Y
        
        elif self.direction == self.MOVES[2]:
            self.rect.y += self.SPEED_ON_Y
            

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
            self.SPEED_ON_Y += 1
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[2]:
            self.SPEED_ON_Y += 10
            if self.rect.bottom > SCREEN_HEIGHT / 2:
                self.SPEED_ON_Y = -5
                self.direction = self.MOVES[0]

                



        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0
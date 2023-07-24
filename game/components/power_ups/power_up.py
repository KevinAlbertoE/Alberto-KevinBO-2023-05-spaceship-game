import pygame
import random
from pygame.sprite import Sprite
from game.components.enemies.enemy import Enemy

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHIELD_TYPE, HEART_TYPE

class PowerUp(Sprite):
    POWER_WIDTH = 40
    POWER_HEIGHT = 50
    MOVES = { 0: 'left', 1: 'right', 2: 'down'}
    def __init__(self, image, type):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.POWER_WIDTH, self.POWER_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.randint(120, SCREEN_WIDTH - 120), 0))
        self.movement_count = 0
        self.direction = self.MOVES[random.randint(0, 2)]
        self.type = type
        self.start_time = 0
        self.moves_before_change = random.randint(20, 50)
        self.speed_on_x = random.randint(10, 20)
        self.speed_on_y = random.randint(1, 5)

    def update(self, game_speed, power_ups):

        if self.direction == self.MOVES[0]:
            self.rect.y += self.speed_on_y
            self.rect.x -= self.speed_on_x


        elif self.direction == self.MOVES[1]:
            self.rect.x += self.speed_on_x
            self.rect.y += self.speed_on_y
        
        elif self.direction == self.MOVES[2]:
            self.rect.y += self.speed_on_y
        self.handle_direction()
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)         
        
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





   
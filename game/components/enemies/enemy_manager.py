import random
import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, DEFAULT_TYPE, HEART_TYPE, OBLIQUE_TYPE

class EnemyManager:   
    def __init__(self):
        self.enemies = []
        self.enemy_images = [ENEMY_1, ENEMY_2, ENEMY_3]

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            if enemy.rect.colliderect(game.player):
                if game.player.power_up_type == DEFAULT_TYPE:
                    game.increase_death_counter()
                    game.playing = False
                    pygame.time.delay(500)
                    break
                if game.player.power_up_type == HEART_TYPE or OBLIQUE_TYPE:
                    game.player.hit += 10000
                    self.enemies.remove(enemy)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            image = random.choice(self.enemy_images)
            speed_on_x = random.randint(10, 20)
            speed_on_y = random.randint(1, 5)

            enemy = Enemy(image, speed_on_x, speed_on_y)
            self.enemies.append(enemy)
        
    def reset(self):
        self.enemies = []
          

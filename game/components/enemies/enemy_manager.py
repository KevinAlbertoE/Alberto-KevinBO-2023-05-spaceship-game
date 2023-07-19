import pygame
from game.components.enemies.enemy import Enemy
#from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class EnemyManager:   
    def __init__(self):
        self.enemies = []
        
    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            enemy = Enemy()
            if enemy not in self.enemies:
                self.enemies.append(enemy)

            else: 
                self.enemies.remove(enemy)
          

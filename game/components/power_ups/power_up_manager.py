import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart 
from game.components.power_ups.oblique_movement import ObliqueMovement
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, HEART_TYPE, SPACESHIP_HEART, OBLIQUE_TYPE, SPACESHIP_OBLIQUE

class PowerUpManager:
    def __init__(self):
        
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)



    def update(self, game):
        current_time = pygame.time.get_ticks()
        move_type = random.randint(0, 2)


        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            if move_type == 0:
                self.generate_power_up(Shield())
            elif move_type == 1:
                self.generate_power_up(Heart())
            elif move_type == 2:
                self.generate_power_up(ObliqueMovement())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
#elif len(self.power_ups) == 0 and points % 200 == 0 and move_type == 1:
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_type = power_up.type
                if power_up.type == SHIELD_TYPE:
                    game.player.power_up_time_up = power_up.start_time + self.duration * 1000
                    game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                    
                    self.power_ups.remove(power_up)
                    

                elif power_up.type == HEART_TYPE:
                    game.player.power_up_time_up = power_up.start_time 
                    game.player.set_image(SPACESHIP_HEART, (65, 75))

                    self.power_ups.remove(power_up)
                    game.player.hit = 0
                elif power_up.type == OBLIQUE_TYPE:
                    game.player.power_up_time_up = power_up.start_time 
                    game.player.set_image(SPACESHIP_OBLIQUE, (65, 75))
                    self.power_ups.remove(power_up)
                    game.player.hit = 0

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, power):
        power_up = power
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 5000, now + 10000)
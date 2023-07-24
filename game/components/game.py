import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, OBLIQUE, HEART_TYPE, SHIELD_TYPE, OBLIQUE_TYPE, HEART_RED, SHIELD
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.score import Score
from game.components.bullets.bullet_manager import BulletManager 
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = Score()
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.highest_score = Score()
        self.death_counter = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen, 'Press any button to start')
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):

        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.player.reset()
        self.score.reset()
        self.power_up_manager.reset()

        # Game loop: events - update - draw
        self.playing = True
        pygame.mixer.music.load("game/assets/Sound/theme.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)
        while self.playing:
            
            self.events()
            self.update()
            self.draw()
           
       # pygame.display.quit()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw_score(self.screen, f"Score: {self.score.score}", 60, 37, "White", 20)
        icon1 = pygame.transform.scale((HEART_RED), (30, 30))
        self.score.draw_score(self.screen, 'EXTRA LIFE', (SCREEN_WIDTH - 170), 50, "White", 15)
        self.screen.blit(icon1, ((SCREEN_WIDTH - 60), 30))
        icon2 = pygame.transform.scale((OBLIQUE), (30, 30))
        self.screen.blit(icon2, ((SCREEN_WIDTH - 60), 60))
        self.score.draw_score(self.screen, 'PRESS Z, X, Q, E TO USE', (SCREEN_WIDTH - 250), 75, "White", 15)
        icon3 = pygame.transform.scale((SHIELD), (30, 30))
        self.score.draw_score(self.screen, 'SHIELD PROTECTS', (SCREEN_WIDTH - 220), 110, "White", 15)
        self.screen.blit(icon3, ((SCREEN_WIDTH - 60), 100))
        #self.enemies.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        pygame.mixer.init()
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
         

    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.update(self)

        self.menu.reset_screen(self.screen)
    

        if self.death_counter > 0:
   
            self.menu.update_message('Game Over: press any key to restart')
            self.set_highest_score()
            self.score.draw_score(self.screen, f'YOUR SCORE: {self.score.score}', (SCREEN_WIDTH / 3 + 50), (SCREEN_HEIGHT / 2 + 30), "Black", 20)
            self.score.draw_score(self.screen, f"HIGHEST SCORE: {self.highest_score.score}", (SCREEN_WIDTH / 3 + 50), (SCREEN_HEIGHT / 2 + 60), "Black", 20)
            self.score.draw_score(self.screen, f"TOTAL DEATHS:{self.death_counter}", (SCREEN_WIDTH / 3 + 50), (SCREEN_HEIGHT / 2 + 90), "Black", 20)
            icon = pygame.transform.scale((ICON), (80, 120))
            self.screen.blit(icon, ((SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 2) - 150))

        self.menu.draw(self.screen)
        self.menu.update(self)    
    def increase_death_counter(self):
        self.death_counter += 1
    
    def set_highest_score(self):
        if self.score.score > self.highest_score.score:
            self.highest_score.set_value(self.score.score)    

    def draw_power_up_time(self):
        if self.player.has_power_up and self.player.power_up_type == SHIELD_TYPE:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show > 0:
                self.score.draw_score(self.screen, f'{self.player.power_up_type} is enabled for {time_to_show}', 60, 60, "White", 20)

            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image() 
        elif self.player.has_power_up and self.player.power_up_type == HEART_TYPE:
            time_to_show = round((self.player.power_up_time_up - self.player.hit) / 10000)

            if time_to_show > 0:
                self.score.draw_score(self.screen, f'{self.player.power_up_type} is enabled for {time_to_show}', 60, 60, "White", 20)

            elif time_to_show == 0:
                self.player.set_image() 
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()         
        elif self.player.has_power_up and self.player.power_up_type == OBLIQUE_TYPE:
            time_to_show = round((self.player.power_up_time_up - self.player.hit) / 10000)
            user_input = pygame.key.get_pressed()
            self.player.move_oblique(self, user_input)
            if time_to_show > 0:
                self.score.draw_score(self.screen, f'{self.player.power_up_type} is enabled for {time_to_show}', 60, 60, "White", 20)

            elif time_to_show == 0:

                self.player.set_image()    
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
                 
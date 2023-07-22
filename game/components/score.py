import pygame
from game.utils.constants import FONT_STYLE
class Score:
    def __init__(self):
        self.score = 0
        self.list_score = []
        self.list_highest_score = []

    def increase_score(self):
        self.score += 1 
        self.list_score.append(self.score)

       

    def draw_score(self, screen, message, pos_x, pos_y, color, size ):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(message, False, color)
        text_rect = text.get_rect(center = (pos_x, pos_y))
        screen.blit(text, text_rect)
        
#    def draw_score_menu(self, game):
 #       font = pygame.font.Font(FONT_STYLE, 20)
  #      text_your_score = font.render(f'YOUR SCORE: {self.score}', False, 'Black')
   #     text_rect_your_score = text_your_score.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30))
    #    text_highest_score = font.render(f"HIGHEST SCORE:{max(self.list_score)}", False, "Black")
     #   text_rect_highest_score = text_highest_score.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))
      #  text_death = font.render(f"TOTAL DEATHS:{game.death_counter}", False, "Black")
      #  text_rect_death = text_death.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90))

 #       game.screen.blit(text_highest_score, text_rect_highest_score)
#        game.screen.blit(text_your_score, text_rect_your_score)
  #      game.screen.blit(text_death, text_rect_death)
    def reset(self):
            self.score = 0
 

        

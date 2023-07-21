import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT
class Score:
    def __init__(self):
        self.score = 0
        self.list_score = []
        self.list_highest_score = []

    def increase_score(self):
        self.score += 1 
        self.list_score.append(self.score)

       

    def draw_score(self, game):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', False, 'White')
        text_rect = text.get_rect(topright = (SCREEN_WIDTH - 30, 30))
        game.screen.blit(text, text_rect)
        
    def draw_score_menu(self, game):
        font = pygame.font.Font(FONT_STYLE, 20)
        text_your_score = font.render(f'YOUR SCORE: {self.score}', False, 'Black')
        text_rect_your_score = text_your_score.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30))
        text_highest_score = font.render(f"HIGHEST SCORE:{max(self.list_score)}", False, "Black")
        text_rect_highest_score = text_highest_score.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))
        text_death = font.render(f"TOTAL DEATHS:{game.death_counter}", False, "Black")
        text_rect_death = text_highest_score.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90))
        game.screen.blit(text_death, text_rect_death)
        game.screen.blit(text_highest_score, text_rect_highest_score)
        game.screen.blit(text_your_score, text_rect_your_score)
    def reset(self):
            self.score = 0
 

        

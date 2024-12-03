import pygame

class Score:
    def __init__(self, font, x, y):
        self.score = 0
        self.font = font
        self.x = x
        self.y = y

    def increase(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (self.x, self.y))
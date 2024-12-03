import pygame
import sys
import time

class Life:
    def __init__(self, font, x, y):
        self.lives = 3
        self.font = font
        self.x = x
        self.y = y
        self.immune = 1.5
        self.dmg_taken = 0

    def taking_damage(self):
        current_time = time.time()
        if current_time - self.dmg_taken >= self.immune:
            self.lives -= 1
            self.dmg_taken = current_time
            if self.lives <= 0:
                print("Game over!")
                sys.exit()

    def draw(self, screen):
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        screen.blit(lives_text, (self.x, self.y))
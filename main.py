import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfiield import *
from shot import Shot
import sys 
from score import Score
from lives import Life
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    lives = Life(pygame.font.SysFont('Arial', 30), SCREEN_WIDTH - 350, 10)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = Score(pygame.font.SysFont('Arial', 30), SCREEN_WIDTH - 150, 10)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)
            
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()
                    score.increase()

        for asteroid in asteroids:
            if asteroid.collision(player):
                lives.taking_damage()
        screen.fill("black")
       
        for i in drawable:
            i.draw(screen)
        score.draw(screen)
        lives.draw(screen)
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

import pygame
from constants import *
from circleshape import CircleShape
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        left = self.velocity.rotate(random.uniform(20, 50))
        right = self.velocity.rotate(-random.uniform(20, 50))
        tleft = self.velocity.rotate(random.uniform(110, 150))
        tright = self.velocity.rotate(-random.uniform(110, 150))

        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = left * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = right * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = tleft * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = tright * 1.2
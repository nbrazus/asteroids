import pygame
import random
from constants import *
from player import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            angle = random.uniform(20, 50)
            one = self.velocity.rotate(angle)
            two = self.velocity.rotate(-angle)
            newrad = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x, self.position.y, newrad)
            new2 = Asteroid(self.position.x, self.position.y, newrad)
            new1.velocity = one * 1.2
            new2.velocity = two * 1.2

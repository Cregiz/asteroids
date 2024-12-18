import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y , radius)
        self.radius = radius

    def draw(self, screen):
        color = (255, 255, 255)
        center = (self.position.x, self.position.y)
        width = 2
        pygame.draw.circle(screen, color, center, self.radius, width)

    def update(self, dt):
        movement = self.velocity * dt
        self.position.x += movement.x
        self.position.y += movement.y

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2

        if hasattr(self, "containers"):
            for container in self.containers:
                container.add(asteroid1)
                container.add(asteroid2)


        
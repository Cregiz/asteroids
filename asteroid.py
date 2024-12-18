import pygame
from circleshape import CircleShape

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
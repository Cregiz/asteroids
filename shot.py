import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = (255, 255, 255)
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, color, center, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
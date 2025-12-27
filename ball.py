import pygame
import math
import random
from constants import BALL_LENGTH, WHITE, BALL_SPEED
from rectangleshape import RectangleShape

class Ball(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_LENGTH, BALL_LENGTH)


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position.x, self.position.y, self.width, self.height))

    def update(self, dt):
        self.position += (self.velocity * dt)

    def set_random_velocity(self):
        degrees = random.uniform(150, 210)
        radians = math.radians(degrees)
        self.velocity.x = math.cos(radians) * BALL_SPEED
        self.velocity.y = math.sin(radians) * BALL_SPEED

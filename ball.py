import pygame
import math
import random
from constants import BALL_LENGTH, WHITE, BALL_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from rectangleshape import RectangleShape

class Ball(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_LENGTH, BALL_LENGTH)


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position.x, self.position.y, self.width, self.height))

    def update(self, dt):
        if self.position.y + self.height >= SCREEN_HEIGHT or self.position.y <= 0:
            self.velocity.y = -self.velocity.y
        self.position += (self.velocity * dt)

    def set_random_velocity(self, direction):
        if direction == "left":
            degrees = random.uniform(150, 210)
        if direction == "right":
            degrees = random.uniform(-30, 30)
        radians = math.radians(degrees)
        self.velocity.x = math.cos(radians) * BALL_SPEED
        self.velocity.y = math.sin(radians) * BALL_SPEED

    def reset(self, direction):
        self.position = pygame.Vector2((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        if direction == "right":
            self.set_random_velocity("right")
        if direction == "left":
            self.set_random_velocity("left")

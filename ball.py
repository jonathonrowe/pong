import pygame
from constants import BALL_LENGTH, WHITE
from rectangleshape import RectangleShape

class Ball(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_LENGTH, BALL_LENGTH)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    
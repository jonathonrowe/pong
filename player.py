import pygame
from rectangleshape import RectangleShape
from constants import *

class Player(RectangleShape):
    def __init__(self, x, y, is_human):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.is_human = is_human

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def update(self, dt):
        keys = pygame.key.get_pressed()
    
        if self.is_human:
            if keys[pygame.K_UP]:
                self.move(-dt)
            if keys[pygame.K_DOWN]:
                self.move(dt)
        else:
            # write the code for the ai in here.
            pass

    def move(self, dt):
        self.y += dt * PLAYER_SPEED
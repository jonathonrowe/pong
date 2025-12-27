import pygame
from rectangleshape import RectangleShape
from constants import *

class Player(RectangleShape):
    def __init__(self, x, y, is_human, is_player1):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.is_human = is_human
        self.is_player1 = is_player1
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position.x, self.position.y, self.width, self.height))

    def update(self, dt):
        keys = pygame.key.get_pressed()
    
        if self.is_human and self.is_player1:
            if keys[pygame.K_UP]:
                self.move(-dt)
            if keys[pygame.K_DOWN]:
                self.move(dt)
        elif self.is_human and not self.is_player1:
            if keys[pygame.K_w]:
                self.move(-dt)
            if keys[pygame.K_s]:
                self.move(dt)
        else:
            # write player_cpu ai code here
            pass

    def move(self, dt):
        self.position.y += dt * PLAYER_SPEED
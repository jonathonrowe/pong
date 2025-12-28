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

    def update(self, dt, ball="ball"):     
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
        elif not self.is_human and not self.is_player1:
            if self.position.y > ball.position.y:
                self.move(-dt)
            if self.position.y + self.height < ball.position.y + ball.height:
                self.move(dt)

    def move(self, dt):
        self.position.y += dt * PLAYER_SPEED
        # Stop paddle at boundary.
        if self.position.y <= 0:
            self.position.y = 0
        if self.position.y + self.height >= SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - self.height
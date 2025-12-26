import sys
import pygame
from constants import *
from player import Player
from ball import Ball

def main():
    print("You are playing Pong")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong by Jon")

    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.SysFont(FONT, FONT_SIZE)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)

    player1 = Player((SCREEN_WIDTH * 0.95), (SCREEN_HEIGHT / 2), True)
    player_cpu = Player((SCREEN_WIDTH * 0.05), (SCREEN_HEIGHT /2), False)
    ball = Ball((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
     
if __name__ == "__main__":
    main()

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

    score_font = pygame.font.SysFont(FONT, SCORE_FONT_SIZE)
    font = pygame.font.SysFont(FONT, FONT_SIZE)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)

    player1 = Player((SCREEN_WIDTH * 0.95), (SCREEN_HEIGHT / 2), True, True)
    player2 = Player((SCREEN_WIDTH * 0.05), (SCREEN_HEIGHT /2), True, False)
    ball = Ball((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    ball.set_random_velocity("left")

    game_state = "start"
    running = True

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    title = "PONG by Jon"

    # Main Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_state = "paused"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = "playing"

        screen.fill("black")

        if game_state == "start":
            draw_text(title, font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .2))
        
        elif game_state == "playing":

            updatable.update(dt)

            if ball.check_collision(player1):
                ball.velocity.x = -ball.velocity.x
            if ball.check_collision(player2):
                ball.velocity.x = -ball.velocity.x

            if ball.position.x + ball.width < 0:
                player1.score += 1
                ball.reset("right")
            if ball.position.x > SCREEN_WIDTH:
                player2.score += 1
                ball.reset("left")

            for sprite in drawable:
                sprite.draw(screen)
        
        elif game_state == "paused":
            draw_text("PAUSED", font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

        player1_score_surface = score_font.render(str(player1.score), True, WHITE)
        screen.blit(player1_score_surface, ((SCREEN_WIDTH / 2) + 50, 20))
        
        player2_score_surface = score_font.render(str(player2.score), True, WHITE)
        screen.blit(player2_score_surface, ((SCREEN_WIDTH / 2) - 50, 20))

        pygame.display.flip()
        dt = clock.tick(60) / 1000
     
if __name__ == "__main__":
    main()

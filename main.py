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
    title_font = pygame.font.SysFont(FONT, TITLE_FONT_SIZE)
    press_key_font = pygame.font.SysFont(FONT, PRESS_KEY_FONT_SIZE)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)

    ball = Ball((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    ball.set_random_velocity("left", 30)

    game_state = "start"
    paused = False
    tutorial_step = 0
    player1 = None
    player2 = None
    player_cpu = None
    tutorial_player1 = None
    winner = None
    # Timer in seconds
    game_over_timer = 0
    tutorial_timer = 0
    running = True

    # Main Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_1:
                    player1 = Player((SCREEN_WIDTH * 0.95), (SCREEN_HEIGHT / 2), "Player 1", True, True)
                    player_cpu = Player((SCREEN_WIDTH * 0.05), (SCREEN_HEIGHT /2), "Computer", False, False)
                    game_state = "one"
                if event.key == pygame.K_2:
                    player1 = Player((SCREEN_WIDTH * 0.95), (SCREEN_HEIGHT / 2), "Player 1", True, True)
                    player2 = Player((SCREEN_WIDTH * 0.05), (SCREEN_HEIGHT /2), "Player 2", True, False)
                    game_state = "two"
                if event.key == pygame.K_t:
                    Player.containers = ()
                    tutorial_player1 = Player((SCREEN_WIDTH * 0.95), (SCREEN_HEIGHT / 2), "Player 1", True, True)
                    tutorial_player2 = Player((SCREEN_WIDTH * 0.05), (SCREEN_HEIGHT /2), "Player 2", True, False)
                    Player.containers = (updatable, drawable)
                    game_state = "tutorial"

        screen.fill("black")

        if game_state == "start":
            draw_text(TITLE, title_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .2))
            draw_text("Press 1 for single player mode", press_key_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .7))
            draw_text("Press 2 for two player mode", press_key_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .8))
            draw_text(PRESS_TUTORIAL, press_key_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .6))
        
        elif game_state == "tutorial":
            tutorial_player1.update(dt)
            tutorial_player1.draw(screen)
            tutorial_player2.update(dt)
            tutorial_player2.draw(screen)
            if tutorial_step == 0:
                if tutorial_timer > 0:
                    draw_text("Good Job!", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .7))
                    tutorial_timer -= dt
                    if tutorial_timer <= 0:
                        tutorial_step = 1
                else:
                    draw_text("Press UP to move up", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .5))
                    if tutorial_player1.position.y <= (SCREEN_HEIGHT * .45):
                        tutorial_timer = 2.0
            if tutorial_step == 1:
                if tutorial_timer > 0:
                    draw_text("Good Job!", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .7))
                    tutorial_timer -= dt
                    if tutorial_timer <= 0:
                        tutorial_step = 2
                else:
                    draw_text("Press DOWN to move down", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .5))
                    if tutorial_player1.position.y >= (SCREEN_HEIGHT * .55):
                        tutorial_timer = 2.0
            if tutorial_step == 2:
                if tutorial_timer > 0:
                    draw_text("Good Job!", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .7))
                    tutorial_timer -= dt
                    if tutorial_timer <= 0:
                        tutorial_step = 3
                else:
                    draw_text("For Player 2", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .3))
                    draw_text("Press W to move up", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .5))
                    if tutorial_player2.position.y <= (SCREEN_HEIGHT * .45):
                        tutorial_timer = 2.0
            if tutorial_step == 3:
                if tutorial_timer > 0:
                    draw_text("Good Job!", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .7))
                    tutorial_timer -= dt
                    if tutorial_timer <= 0:
                        tutorial_step = 0
                        tutorial_player1 = None
                        tutorial_player2 = None
                        game_state = "start"
                else:
                    draw_text("For Player 2", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .3))
                    draw_text("Press S to move down", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .5))
                    if tutorial_player2.position.y >= (SCREEN_HEIGHT * .55):
                        tutorial_timer = 2.0

        elif game_state == "one":
            
            ball.update(dt)
            player1.update(dt)
            player_cpu.update(dt, ball=ball)

            if player1.score >= 10:
                winner = player1.name
                game_over_timer = 3.0
                game_state = "game over"
            if player_cpu.score >= 10:
                game_over_timer = 3.0
                winner = player_cpu.name
                game_state = "game_over"

            if ball.check_center_collision(player1):
                ball.velocity.x = -ball.velocity.x
            if ball.check_center_collision(player_cpu):
                ball.velocity.x = -ball.velocity.x

            if ball.check_top_edge_collision(player1):
                ball.set_random_velocity("left", 45)
            if ball.check_top_edge_collision(player_cpu):
                ball.set_random_velocity("right", 45)
            if ball.check_bottom_edge_collision(player1):
                ball.set_random_velocity("left", 45)
            if ball.check_bottom_edge_collision(player_cpu):
                ball.set_random_velocity("right", 45)

            if ball.position.x + ball.width < 0:
                player1.score += 1
                ball.reset("right")
            if ball.position.x > SCREEN_WIDTH:
                player_cpu.score += 1
                ball.reset("left")
            
            for sprite in drawable:
                sprite.draw(screen)

            player1_score_surface = score_font.render(str(player1.score), True, WHITE)
            screen.blit(player1_score_surface, ((SCREEN_WIDTH / 2) + 50, 20))
        
            player_cpu_score_surface = score_font.render(str(player_cpu.score), True, WHITE)
            screen.blit(player_cpu_score_surface, ((SCREEN_WIDTH / 2) - 50, 20)) 

        elif game_state == "two":

            updatable.update(dt)

            if player1.score >= 10:
                winner = player1.name
                game_over_timer = 3.0
                game_state = "game over"
            if player2.score >= 10:
                game_over_timer = 3.0
                winner = player2.name
                game_state = "game_over"

            if ball.check_center_collision(player1):
                ball.velocity.x = -ball.velocity.x
            if ball.check_center_collision(player2):
                ball.velocity.x = -ball.velocity.x
            # Need to update these with changes in angle, too
            if ball.check_top_edge_collision(player1):
                ball.set_random_velocity("left", 45)
            if ball.check_top_edge_collision(player2):
                ball.set_random_velocity("right", 45)
            if ball.check_bottom_edge_collision(player1):
                ball.set_random_velocity("left", 45)
            if ball.check_bottom_edge_collision(player2):
                ball.set_random_velocity("right", 45)
            

            if ball.position.x + ball.width < 0:
                player1.score += 1
                ball.reset("right")
            if ball.position.x > SCREEN_WIDTH:
                player2.score += 1
                ball.reset("left")

            for sprite in drawable:
                sprite.draw(screen)
        
            player1_score_surface = score_font.render(str(player1.score), True, WHITE)
            screen.blit(player1_score_surface, ((SCREEN_WIDTH / 2) + 50, 20))
        
            player2_score_surface = score_font.render(str(player2.score), True, WHITE)
            screen.blit(player2_score_surface, ((SCREEN_WIDTH / 2) - 50, 20))

        elif paused:
            draw_text("PAUSED", title_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
            draw_text(PRESS_SPACE, press_key_font, WHITE, screen, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT * .8))

        elif game_state == "game over":
            if game_over_timer > 0:
                draw_text("Game Over", title_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .4))
                draw_text(f"{winner} Wins!", press_key_font, WHITE, screen, (SCREEN_WIDTH * .5), (SCREEN_HEIGHT * .6))
                game_over_timer -= dt
                if game_over_timer <= 0:
                    game_state = "start"


        pygame.display.flip()
        dt = clock.tick(60) / 1000
     
if __name__ == "__main__":
    main()

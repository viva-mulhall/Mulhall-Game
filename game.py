import random
import pygame
from paddle import Paddle
from ball import Ball
import sound_effect as se

pygame.init()

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game():
    # Open a new window
    size = (900, 500)
    screen = pygame.display.set_mode(size)
    bg_color = (0, 155, 100)
    pygame.display.set_caption('Multiplayer Tennis')
    player_1 = Paddle((0, 0, 255), 20, 75)
    player_1.rect.x = 20
    player_1.rect.y = 200
    player_2 = Paddle((255, 0, 0), 20, 75)
    player_2.rect.x = 870
    player_2.rect.y = 200
    paddle = [player_1, player_2]
    blue = [player_1]
    red = [player_2]
    ball = Ball((255,255,255),10,10)
    ball.rect.x = 330
    ball.rect.y = 195
    se.game_sound.play()

    all_sprites_list = pygame.sprite.Group()

    # Add the 2 paddles and the ball to the list of objects
    # Add the paddles to the list of sprites
    all_sprites_list.add(player_1)
    all_sprites_list.add(player_2)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True


    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # Initialise player scores
    score1 = 0
    score2 = 0

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop

        # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_1.moveUp(1)
        if keys[pygame.K_s]:
            player_1.moveDown(1)
        if keys[pygame.K_UP]:
            player_2.moveUp(1)
        if keys[pygame.K_DOWN]:
            player_2.moveDown(1)
        all_sprites_list.update()

        if pygame.sprite.collide_mask(ball, player_1):
            ball.bounce()
            se.ball_collide.play()
            score1 = score1 + 1
        if  pygame.sprite.collide_mask(ball, player_2):
            ball.bounce()
            se.ball_collide.play()
            score2 = score2 + 1
        if ball.rect.x >= 891:
            end_1()
        if ball.rect.x < 0:
            end_2()
        if ball.rect.y> 490:
            ball.velocity[1] = -ball.velocity[1]
            se.ball_collide.play()
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]
            se.ball_collide.play()
        if score2 == 5:
            end_2()
        if score1 == 5:
            end_1()




        screen.fill(bg_color)
        pygame.draw.rect(screen, (255, 255, 255), ball)
        pygame.draw.line(screen, (255, 255, 255), [450, 0], [450, 500], 12)
        all_sprites_list.draw(screen)


        font = pygame.font.Font(None, 65)
        text = font.render(str(f"Player 1: {score1}"), 1, (255, 255, 255))
        screen.blit(text, (150, 10))
        text = font.render(str(f"Player 2: {score2}"), 1, (255, 255, 255))
        screen.blit(text, (490, 10))

        pygame.display.flip()
    pygame.quit()

def end_2():

    size = (900, 500)
    screen = pygame.display.set_mode(size)
    bg_color = (0, 0, 0)
    pygame.display.set_caption('Multiplayer Tennis')
    screen.fill(bg_color)
    font = pygame.font.Font(None, 65)
    text = font.render(str(f"Player 2 WON!!"), 1, (255, 0, 0))
    screen.blit(text, (270, 200))
    text = font.render(str('press space to restart'), 1, (255, 255, 255))
    screen.blit(text, (230, 370))
    pygame.display.flip()
    def draw_text(text, font, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    restart = False

    run = True

    while run:
        pygame.init()
        screen.fill((0, 0, 0))

        if restart == True:
            pygame.init()
            game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart = True
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

def end_1():
    size = (900, 500)
    screen = pygame.display.set_mode(size)
    bg_color = (0, 0, 0)
    pygame.display.set_caption('Multiplayer Tennis')
    screen.fill(bg_color)
    font = pygame.font.Font(None, 65)
    text = font.render(str(f"Player 1 WON!!"), 1, (0, 0, 255))
    screen.blit(text, (290, 200))
    text = font.render(str('press space to restart'), 1, (255, 255, 255))
    screen.blit(text, (230, 370))
    pygame.display.flip()
    def draw_text(text, font, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    again = False

    go = True

    while go:
        pygame.init()
        screen.fill((0, 0, 0))

        if again == True:
            pygame.init()
            game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    again = True
                if event.type == pygame.QUIT:
                    go = False
    pygame.quit()




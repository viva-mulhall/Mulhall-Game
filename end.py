import pygame
from game import *

def end():

    size = (900, 500)
    screen = pygame.display.set_mode(size)
    bg_color = (0, 0, 0)
    pygame.display.set_caption('Multiplayer Tennis')
    screen.fill(bg_color)
    font = pygame.font.Font(None, 65)
    text = font.render(str(f"Player 2 WON!!"), 1, (255, 0, 0))
    screen.blit(text, (350, 200))
    text = font.render(str('press space to restart'), 1, (255, 255, 255))
    screen.blit(text, (490, 10))
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
        else:
            draw_text('Press space to restart', font, (255,255,255), 220, 370)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart = True
            if event.type == pygame.QUIT:
                run = False


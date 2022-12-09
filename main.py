from game import *
import sound_effect as se
pygame.init()

screen_width = 900
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Main Menu')

#game variables
main_menu =  False

font = pygame.font.SysFont('arialblack', 40)
white = (255,255,255)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

run = True

while run:
    pygame.init()
    screen.fill((0,0,0))

    if main_menu == True:
        #makes entire game run
        game()
    else:
        draw_text('Press space to restart', font, (255, 255, 255), 220, 370)
        se.main_menu.play()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_menu = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()



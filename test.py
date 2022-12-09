import pygame
import random
import time

# initialize pygame
pygame.init()

# color globals
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
violet = (127, 0, 255)
brown = (102, 51, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# screen globals
screen_width = 600
screen_height = 400
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(“PyTennis by HiTech360”)
font = pygame.font.SysFont(“monospace”, 75)

# ball globals
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
ball_xv = 3
ball_yv = 3
ball_r = 20

# draw paddle 1
paddle1_x = 10
paddle1_y = 10
paddle1_w = 25
paddle1_h = 100

# draw paddle 2
paddle2_x = screen_width – 35
paddle2_y = 10
paddle2_w = 25
paddle2_h = 100

# initialize score
player1_score = 0
player2_score = 0

# game loop
pygame.mouse.set_visible(0) # makes mouse invisible in game screen
do_main = True
while do_main:
pressed = pygame.key.get_pressed()
pygame.key.set_repeat()
for event in pygame.event.get():
if event.type == pygame.QUIT:
do_main = False

if pressed[pygame.K_ESCAPE]:
do_main = False

if pressed[pygame.K_w]:
paddle1_y -= 5
elif pressed[pygame.K_s]:
paddle1_y += 5

if pressed[pygame.K_UP]:
paddle2_y -= 5
elif pressed[pygame.K_DOWN]:
paddle2_y += 5

# location of ball is updated
ball_x += ball_xv
ball_y += ball_yv

# collision of ball with top/bottom of screen
if ball_y – ball_r <= 0 or ball_y + ball_r >= screen_height:
ball_yv *= -1

# collision of paddle with top/bottom of screen
if paddle1_y < 0:
paddle1_y = 0
elif paddle1_y + paddle1_h > screen_height:
paddle1_y = screen_height – paddle1_h

if paddle2_y < 0:
paddle2_y = 0
elif paddle2_y + paddle2_h > screen_height:
paddle2_y = screen_height – paddle2_h

# collision of ball and paddles
# left paddle
if ball_x < paddle1_x + paddle1_w and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle1_h:
ball_xv *= -1
# right paddle
if ball_x > paddle2_x and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle2_h:
ball_xv *= -1

# player score
if ball_x <= 0:
player2_score += 1
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
elif ball_x >= screen_width:
player1_score += 1
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)

game_screen.fill(black)
paddle_1 = pygame.draw.rect(game_screen, red, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
paddle_2 = pygame.draw.rect(game_screen, blue, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
net = pygame.draw.line(game_screen, orange, (300,5), (300,400))
ball = pygame.draw.circle(game_screen, yellow, (ball_x, ball_y), ball_r, 0)

score_text = font.render(str(player1_score) + ” ” + str(player2_score), 1, white)
game_screen.blit(score_text, (screen_width / 2 – score_text.get_width() / 2, 10))

pygame.display.update()

time.sleep(0.016666667)

pygame.quit()
# game end
import pygame

pygame.mixer.init()

main_menu = pygame.mixer.Sound('Menu_Sound.wav')
game_sound = pygame.mixer.Sound('game_sound.wav')
ball_collide = pygame.mixer.Sound('ball_hit.wav')
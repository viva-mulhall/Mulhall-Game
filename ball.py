import random
from random import randint
import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, color, [0,0, width, height])

        #self.velocity_x = 1
        #self.velocity_y = 0
        #self.rect = self.image.get_rect()

        self.velocity = [1, 1]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-1, 1)

    #def move_ip(self, velocity_x, velocity_y):
     #   pass

    #def collidelist(self, object):
     #   pass


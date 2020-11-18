import pygame
from pygame.locals import *

class PipeGap(pygame.sprite.Sprite):

    def __init__(self, xpos, ysize, screen_height):
        self.VELOCIDADE = 5
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/point_area.png')
        self.image = pygame.transform.scale(self.image, (1, screen_height))

        self.rect = pygame.Rect(0, 0, 10, screen_height)

        self.rect[0] = xpos+30
        self.rect[1] = 0 

        

    def update(self):
        self.rect[0] -= self.VELOCIDADE
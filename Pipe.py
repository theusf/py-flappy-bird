import pygame
from pygame.locals import *

class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted,xpos, ysize, screen_height):
        self.VELOCIDADE = 5
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/pipe-red.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 500))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = screen_height - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= self.VELOCIDADE
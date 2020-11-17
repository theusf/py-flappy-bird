import pygame
from pygame.locals import *

class Ground(pygame.sprite.Sprite):

        def __init__(self, width, height, xpos):
            pygame.sprite.Sprite.__init__(self)

            self.image = pygame.image.load('assets/base.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (width, height))

            self.mask = pygame.mask.from_surface(self.image)

            self.rect = self.image.get_rect()
            self.rect[0] = xpos
            self.rect[1] = pygame.display.get_surface().get_height() - height


        def update(self):
            self.rect[0] -= 5


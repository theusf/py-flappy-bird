import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        """ Construtor da classe pai """
        pygame.sprite.Sprite.__init__(self)

        self.sprites = [
            pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
        ]

        self.sprite_atual = 0

        """ Convert alpha para deixar o transparente """
        self.image = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()

        """ Criando o rect com base no tamanho da imagem"""
        self.rect = self.image.get_rect()

        """ Pegar altura e largura da tela """
        w, h = pygame.display.get_surface().get_size()

        """ Colocar o passaro no meio """
        self.rect[0] = w/2
        self.rect[1] = h/2

    def update(self):        
        """ Modulo 3 faz voltar pro 0 quando chega no 3 """
        self.sprite_atual = (self.sprite_atual + 1) % 3

        self.image = self.sprites[self.sprite_atual]

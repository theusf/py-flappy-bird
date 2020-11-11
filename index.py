import pygame
from pygame.locals import *
from Bird import Bird
from Ground import Ground

# EM CAPS PORQUE SAO CONSTANTES 
TELA_LARGURA = 400
TELA_ALTURA = 800

pygame.init()
screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

FUNDO = pygame.image.load('assets/background-day.png')
# Escalonar o fundo para que fique do tamanho da minha tela 
FUNDO = pygame.transform.scale(FUNDO, (TELA_LARGURA, TELA_ALTURA))

passaro_grupo = pygame.sprite.Group()
passaro = Bird()
passaro_grupo.add(passaro)

chao_grupo = pygame.sprite.Group()
chao = Ground(TELA_LARGURA, 100)
chao_grupo.add(chao)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                passaro.pulo()

    screen.blit(FUNDO, (0, 0))

    #  Atualiza os componentes
    passaro_grupo.update()

    chao_grupo.update()

    #  Desenha todo mundo do grupo
    passaro_grupo.draw(screen)

    #  Desenha todo mundo do grupo
    chao_grupo.draw(screen)

    pygame.display.update()

    clock.tick(30)
    


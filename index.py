import pygame
from pygame.locals import *
from Bird import Bird
from Ground import Ground
from Pipe import Pipe
import random

# EM CAPS PORQUE SAO CONSTANTES 
TELA_LARGURA = 400
TELA_ALTURA = 600

CHAO_LARGURA = TELA_LARGURA * 2
CHAO_ALTURA = 100

CANO_ALTURA = 500
CANO_LARGURA = 120

ESPACO_GAP = 200

pygame.init()
screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

FUNDO = pygame.image.load('assets/background-day.png')
# Escalonar o fundo para que fique do tamanho da minha tela 
FUNDO = pygame.transform.scale(FUNDO, (TELA_LARGURA, TELA_ALTURA))


passaro_grupo = pygame.sprite.Group()
passaro = Bird()
passaro_grupo.add(passaro)

chao_grupo = pygame.sprite.Group()

pipe_grupo = pygame.sprite.Group()

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size, TELA_ALTURA)
    pipe_inverted = Pipe(True, xpos, TELA_ALTURA - size - ESPACO_GAP,TELA_ALTURA)
    return (pipe, pipe_inverted)


for i in range(2):
    chao = Ground(2 * TELA_LARGURA, 100, CHAO_LARGURA * i) 
    chao_grupo.add(chao)
    #Chão "colado" um no outro

pipe_grupo = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(TELA_LARGURA * i + 700)
    pipe_grupo.add(pipes[0])
    pipe_grupo.add(pipes[1])


clock = pygame.time.Clock()

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2]) #sprite.rect[2] = posição em largura 
    #rect[0] = #


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                passaro.pulo()

    screen.blit(FUNDO, (0, 0))

    if is_off_screen(chao_grupo.sprites()[0]):
        chao_grupo.remove(chao_grupo.sprites()[0])

        novo_chao = Ground(CHAO_LARGURA, 100, CHAO_LARGURA - 30)
        chao_grupo.add(novo_chao)

    if is_off_screen(pipe_grupo.sprites()[0]):
        pipe_grupo.remove(pipe_grupo.sprites()[0])
        pipe_grupo.remove(pipe_grupo.sprites()[0])

        pipes = get_random_pipes(TELA_LARGURA * 2)

        pipe_grupo.add(pipes[0])
        pipe_grupo.add(pipes[1])
        

    #  Atualiza os componentes
    passaro_grupo.update()
    chao_grupo.update()
    pipe_grupo.update()

    #  Desenha todo mundo do grupo
    passaro_grupo.draw(screen)

    #  Desenha todo mundo do grupo
    chao_grupo.draw(screen)

    pipe_grupo.draw(screen)
    #Verifica Colisão
    
    if (pygame.sprite.groupcollide(passaro_grupo, chao_grupo, False, False) or
        pygame.sprite.groupcollide(passaro_grupo, pipe_grupo, False, False)):
        #Game Over
        pygame.display.update()
        break

    pygame.display.update()

    clock.tick(30)

    

    


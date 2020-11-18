import pygame
from pygame.locals import *
from Bird import Bird
from Ground import Ground
from Pipe import Pipe
from PipeGap import PipeGap
import random

# EM CAPS PORQUE SAO CONSTANTES
TELA_LARGURA = 400
TELA_ALTURA = 700
CHAO_LARGURA = TELA_LARGURA * 2
CHAO_ALTURA = 100
CANO_ALTURA = 500
CANO_LARGURA = 120
ESPACO_GAP = 200
EM_JOGO = False
PONTOS = 0
NO_MENU = True
GAME_OVER = False

pygame.init()
screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

# Fundo
FUNDO = pygame.image.load('assets/background-day.png')

# Escalonar o fundo para que fique do tamanho da minha tela
FUNDO = pygame.transform.scale(FUNDO, (TELA_LARGURA, TELA_ALTURA))

# Logo
LOGO = pygame.image.load('assets/logo.png')
# Sobre
SOBRE = pygame.image.load('assets/home-desc.png')
# Sobre
GAMEOVER_IMG = pygame.image.load('assets/game_over.png')

# Som do ponto
pygame.mixer.music.load('assets/point.mp3')
# pygame.mixer.music.set_volume(0.05)

# Fonte
FONT = pygame.font.Font('assets/8-bit-hud.ttf', 50)


clock = pygame.time.Clock()

pygame.display.set_caption('py flappy bird ')

passaro_grupo = pygame.sprite.Group()

passaro = Bird()

passaro_grupo.add(passaro)

chao_grupo = pygame.sprite.Group()

pipe_grupo = pygame.sprite.Group()

pipe_gap_group = pygame.sprite.Group()


def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size, TELA_ALTURA)
    pipe_inverted = Pipe(True, xpos, TELA_ALTURA -
                         size - ESPACO_GAP, TELA_ALTURA)
    pipe_gap = PipeGap(xpos, TELA_ALTURA, TELA_ALTURA)
    return (pipe, pipe_inverted, pipe_gap)


for i in range(2):
    chao = Ground(2 * TELA_LARGURA, 100, CHAO_LARGURA * i)
    chao_grupo.add(chao)
    # Chão "colado" um no outro

for i in range(2):
    pipes = get_random_pipes(TELA_LARGURA * i + 700)
    pipe_grupo.add(pipes[0])
    pipe_grupo.add(pipes[1])
    pipe_gap_group.add(pipes[2])


def is_off_screen(sprite):
    # sprite.rect[2] = posição em largura
    return sprite.rect[0] < - (sprite.rect[2])
    #rect[0] = #


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                passaro.pulo()

            if NO_MENU == True:
                
                EM_JOGO = True
                NO_MENU = False

            if GAME_OVER == True:
                pygame.quit()


    pygame.display.update()

    clock.tick(30)

    # Desneha o fundo
    screen.blit(FUNDO, (0, 0))

    #  Desenha todo mundo do grupo do passaro
    passaro_grupo.draw(screen)

    if EM_JOGO:

        #  Desenha todo mundo do grupo do chao
        chao_grupo.draw(screen)

        #  Desenha todo mundo do grupo dos canos
        pipe_grupo.draw(screen)

        #  Desenha todo mundo do grupo do pipe gap
        pipe_gap_group.draw(screen)

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
            pipe_gap_group.add(pipes[2])

        if is_off_screen(pipe_gap_group.sprites()[0]):
            pipe_gap_group.remove(pipe_gap_group.sprites()[0])

        #  Atualiza os componentes
        passaro_grupo.update()
        chao_grupo.update()
        pipe_grupo.update()
        pipe_gap_group.update()

        # Verifica Colisão
        if (pygame.sprite.groupcollide(passaro_grupo, chao_grupo, False, False) or
                pygame.sprite.groupcollide(passaro_grupo, pipe_grupo, False, False)):
            pygame.mixer.music.load('assets/hit.mp3')
            pygame.mixer.music.play(0)

            # Game Over
            EM_JOGO = False
            GAME_OVER = True
            

        if pygame.sprite.groupcollide(passaro_grupo, pipe_gap_group, False, True):
            PONTOS += 1
            pygame.mixer.music.load('assets/point.mp3')
            pygame.mixer.music.play(0)

        # Ponto
        TEXTO_SCORE = FONT.render(str(PONTOS), True, (255, 255, 255))

        TEXTORECT = TEXTO_SCORE.get_rect().center = (170, 100)

        screen.blit(TEXTO_SCORE, TEXTORECT)

    if NO_MENU:

        screen.blit(LOGO, (45, 75))
        screen.blit(SOBRE, (50, 550))

        # Limpa o grupo de passaro
        passaro_grupo.empty()
        
        # Adiciona o passaro de novo
        passaro = Bird()
        passaro_grupo.add(passaro)

    if GAME_OVER:

        screen.blit(GAMEOVER_IMG, (125, 300))
        pygame.display.update()



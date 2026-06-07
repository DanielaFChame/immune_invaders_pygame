# ===========================================================
# VERSÃO MÍNIMA (primeira entrega):
#   - mover a célula para a esquerda/direita
#   - disparar tiros
# ===========================================================

import pygame

# ---------- Configurações (tela, fps) ----------
LARGURA = 800        # largura da janela
ALTURA = 600         # altura da janela
FPS = 60             # quadros por segundo

# Cores (tuplas R, G, B)
FUNDO = (15, 20, 35)
AZUL = (90, 160, 230)
BRANCO = (255, 255, 255)
AMARELO = (240, 220, 80)

VEL_JOGADOR = 6      # quantos pixels a célula anda por quadro
VEL_TIRO = 9         # quantos pixels o tiro sobe por quadro
COOLDOWN = 300       # tempo mínimo (em milissegundos) entre dois tiros

# ---------- Inicialização ----------
pygame.init() # inicializa todos os módulos internos do Pygame
tela = pygame.display.set_mode((LARGURA, ALTURA)) # cria a janela do jogo
pygame.display.set_caption("Immuno Invaders") # define o titulo 
relogio = pygame.time.Clock() # cria o objeto de relógio para gerenciar a velocidade do jogo

# O jogador é um dicionário
jogador = {
    "x": LARGURA // 2 - 25,   # Ajuste para começar no meio da tela
    "y": ALTURA - 50,         # quase no rodapé
    "largura": 50,
    "altura": 30,
}

# Lista que vai guardar todos os tiros na tela
tiros = []

# Guarda o momento do último tiro, para controlar o cooldown
ultimo_tiro = 0

# ---------- Loop principal ----------
rodando = True
while rodando:
    relogio.tick(FPS)                 # velocidade do jogo = 60 frames por seg
    agora = pygame.time.get_ticks()   # Retorna o tempo decorrido em milissegundos

    # ----- 1) EVENTOS (fechar a janela, ESC para sair) -----
    for evento in pygame.event.get(): # pega todos os eventos (cliques, teclas pressionadas, movimento mouse...)
        if evento.type == pygame.QUIT: # fechar janela no x
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE: # fechar janela com esc
            rodando = False

    # ----- 2) ATUALIZAÇÃO -----
    teclas = pygame.key.get_pressed()  # quais teclas estão sendo pressionadas agora

    # Movimento da célula
    if teclas[pygame.K_LEFT]:
        jogador["x"] -= VEL_JOGADOR
    if teclas[pygame.K_RIGHT]:
        jogador["x"] += VEL_JOGADOR

    # Trava para a célula não sair pelas laterais
    if jogador["x"] < 0:
        jogador["x"] = 0
    if jogador["x"] > LARGURA - jogador["largura"]:
        jogador["x"] = LARGURA - jogador["largura"]

    # Disparo com a barra de espaço (respeitando o cooldown)
    if teclas[pygame.K_SPACE] and agora - ultimo_tiro >= COOLDOWN:
        tiro = {
            "x": jogador["x"] + jogador["largura"] // 2 - 3,  # ajuste para sair do meio da célula
            "y": jogador["y"],
            "largura": 6,
            "altura": 16,
        }
        tiros.append(tiro)      # adiciona o novo tiro na lista
        ultimo_tiro = agora     # marca o horário deste tiro

    # Move todos os tiros para cima (y diminui = sobe)
    for tiro in tiros:
        tiro["y"] -= VEL_TIRO 

    # Remove os tiros que já saíram pela parte de cima da tela.
    # Lista nova só com os que ainda estão visíveis.
    tiros_na_tela = []
    for tiro in tiros:
        if tiro["y"] + tiro["altura"] > 0: # o limite superior de "y" é zero
            tiros_na_tela.append(tiro)
    tiros = tiros_na_tela

    # ----- 3) DESENHO -----
    tela.fill(FUNDO)   # cor do fundo da tela

    # Desenha cada tiro
    #pygame.draw.rec(tela, cor, (x, y, largura, altura)) desenha um retagulo na tela
    for tiro in tiros:
        pygame.draw.rect(tela, AMARELO,
                         (tiro["x"], tiro["y"], tiro["largura"], tiro["altura"]))

    # Desenha a célula (corpo azul + núcleo branco)
    pygame.draw.ellipse(tela, AZUL,
                        (jogador["x"], jogador["y"], jogador["largura"], jogador["altura"]))
    # desenha o núcleo: pygame.draw.circle(tela, cor, (x, y), raio)
    pygame.draw.circle(tela, BRANCO,
                       (jogador["x"] + jogador["largura"] // 2,
                        jogador["y"] + jogador["altura"] // 2), 6)

    pygame.display.flip()   # Atualiza a tela inteira

pygame.quit() # encerra todos os módulos da biblioteca que foram ativados pelo pygame.init()

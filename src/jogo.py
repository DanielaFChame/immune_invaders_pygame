
import os
import math
import pygame

import config
import entidades
import funcoes
import dados


# Caminho do arquivo de recorde (dentro da pasta data/, na raiz do projeto).
# Subimos uma pasta a partir de src/ para chegar na raiz do projeto.
PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_RECORDE = os.path.join(PASTA_RAIZ, "data", config.ARQUIVO_RECORDE)

# Garante que a pasta data/ exista (cria automaticamente se não existir).
# exist_ok=True significa: se a pasta já existir, não dá erro.
os.makedirs(os.path.join(PASTA_RAIZ, "data"), exist_ok=True)



# ------------------------------------------------------------
# FUNÇÕES DE DESENHO (só desenham, não mudam a lógica)
# ------------------------------------------------------------
def desenhar_jogador(tela, jogador, img_jogador=None):
    """Desenha a célula de defesa. Usa imagem se houver; senão, formas geométricas."""
    if img_jogador is not None:
        tela.blit(img_jogador, (jogador["x"], jogador["y"]))
        return

    # --- desenho geométrico original (reserva) ---
    corpo = pygame.Rect(jogador["x"], jogador["y"], jogador["largura"], jogador["altura"])
    pygame.draw.ellipse(tela, config.AZUL, corpo)
    centro_x = jogador["x"] + jogador["largura"] // 2
    centro_y = jogador["y"] + jogador["altura"] // 2
    pygame.draw.circle(tela, config.BRANCO, (centro_x, centro_y), 6)


def desenhar_virus(tela, lista_virus, img_virus=None):
    """Desenha cada vírus vivo. Usa imagem se houver; senão, formas geométricas."""
    for virus in lista_virus:
        if not virus["vivo"]:
            continue

        # Se a imagem foi carregada, usa ela:
        if img_virus is not None:
            tela.blit(img_virus, (virus["x"], virus["y"]))
            continue  # já desenhou, pula o desenho geométrico

        # --- desenho geométrico original (vale como reserva) ---
        centro_x = virus["x"] + virus["largura"] // 2
        centro_y = virus["y"] + virus["altura"] // 2
        raio = virus["largura"] // 2
        for angulo in range(0, 360, 45):
            fim_x = centro_x + int((raio + 5) * math.cos(math.radians(angulo)))
            fim_y = centro_y + int((raio + 5) * math.sin(math.radians(angulo)))
            pygame.draw.line(tela, config.VERMELHO, (centro_x, centro_y), (fim_x, fim_y), 2)
        pygame.draw.circle(tela, config.VERMELHO, (centro_x, centro_y), raio)
        pygame.draw.circle(tela, config.PRETO, (centro_x, centro_y), 4)


def desenhar_anticorpos(tela, anticorpos):
    """Desenha cada disparo ativo como um anticorpo em Y:
    uma haste vertical e, na ponta de cima, uma bifurcação (dois braços)."""
    for anticorpo in anticorpos:
        if not anticorpo["ativo"]:
            continue

        x = anticorpo["x"]
        y = anticorpo["y"]
        larg = anticorpo["largura"]
        alt = anticorpo["altura"]

        cx = x + larg // 2     # centro horizontal
        topo = y               # ponta de cima (sobe, então a bifurcação fica aqui)
        base = y + alt         # parte de baixo da haste
        meio = y + alt // 2    # ponto onde a haste se divide em dois braços

        cor = config.TIRO
        espessura = max(2, larg // 3)   # acompanha a largura do tiro

        # Haste (parte reta, de baixo até o meio)
        pygame.draw.line(tela, cor, (cx, base), (cx, meio), espessura)
        # Bifurcação: dois braços abrindo até os cantos de cima
        pygame.draw.line(tela, cor, (cx, meio), (x, topo), espessura)
        pygame.draw.line(tela, cor, (cx, meio), (x + larg, topo), espessura)

        # Pontinhas nas extremidades (os "sítios de ligação" do anticorpo)
        pygame.draw.circle(tela, cor, (x, topo), espessura)
        pygame.draw.circle(tela, cor, (x + larg, topo), espessura)


def desenhar_hud(tela, fonte, jogador, recorde, virus_vivos):
    """Desenha o HUD (informações no topo): pontuação, vidas e recorde."""
    texto_pontos = fonte.render("Pontos: " + str(jogador["pontuacao"]), True, config.TEXTO)
    texto_vidas = fonte.render("Vidas: " + str(jogador["vidas"]), True, config.TEXTO)
    texto_recorde = fonte.render("Recorde: " + str(recorde), True, config.TEXTO_DESTAQUE)
    texto_virus = fonte.render("Virus: " + str(virus_vivos), True, config.COR_VITORIA)

    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_vidas, (200, 10))
    tela.blit(texto_recorde, (350, 10))
    tela.blit(texto_virus, (560, 10))

    pygame.draw.line(tela, config.CINZA,
                     (0, config.LINHA_DEFESA_Y),
                     (config.LARGURA_TELA, config.LINHA_DEFESA_Y), 1)


def desenhar_texto_centralizado(tela, texto, fonte, cor, deslocamento_y=0):
    """Função auxiliar: escreve um texto no centro da tela."""
    render = fonte.render(texto, True, cor)
    x = config.LARGURA_TELA // 2 - render.get_width() // 2
    y = config.ALTURA_TELA // 2 - render.get_height() // 2 + deslocamento_y
    tela.blit(render, (x, y))


# ------------------------------------------------------------
# FUNÇÃO QUE (RE)INICIA UMA PARTIDA
# ------------------------------------------------------------
def iniciar_partida():
    """Cria/zera todos os elementos para uma nova partida.

    Devolve uma tupla com tudo que o loop precisa:
      jogador, lista_virus, anticorpos, direcao_virus
    """
    jogador = entidades.criar_jogador()
    lista_virus = funcoes.criar_virus(config.VIRUS_LINHAS, config.VIRUS_COLUNAS)
    anticorpos = []          # começa sem nenhum disparo na tela
    direcao_virus = 1        # 1 = começa indo para a direita
    return jogador, lista_virus, anticorpos, direcao_virus


# ------------------------------------------------------------
# FUNÇÃO PRINCIPAL: monta a janela e roda o loop do jogo
# ------------------------------------------------------------
def executar():
    pygame.init()

    # Tenta ligar o áudio. Se a máquina não tiver som, o jogo continua.
    try:
        pygame.mixer.init()
    except pygame.error:
        pass

    # ---------- SONS ----------
    PASTA_SONS = os.path.join(PASTA_RAIZ, "assets", "sons")

    def carregar_som(nome):
        """Carrega um som; se faltar, devolve None e o jogo continua sem ele."""
        try:
            return pygame.mixer.Sound(os.path.join(PASTA_SONS, nome))
        except Exception as e:
            print("Nao carregou o som", nome, "->", e)
            return None

    som_tiro = carregar_som("tiro.wav")
    som_explosao = carregar_som("explosao.wav")
    som_fim = carregar_som("fim.wav")

    # ---------- JANELA ----------
    tela = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
    pygame.display.set_caption(config.TITULO)
    relogio = pygame.time.Clock()

    # ---------- IMAGENS ----------
    CAMINHO_IMG_VIRUS = os.path.join(PASTA_RAIZ, "assets", "imagens", "virus.png")
    try:
        img_virus = pygame.image.load(CAMINHO_IMG_VIRUS).convert_alpha()
        img_virus = pygame.transform.scale(img_virus, (config.VIRUS_LARGURA, config.VIRUS_ALTURA))
    except Exception as e:
        img_virus = None
        print("FALHOU ao carregar a imagem do virus. Motivo:", e)

    CAMINHO_IMG_JOGADOR = os.path.join(PASTA_RAIZ, "assets", "imagens", "celula.png")
    try:
        img_jogador = pygame.image.load(CAMINHO_IMG_JOGADOR).convert_alpha()
        img_jogador = pygame.transform.scale(img_jogador, (config.JOGADOR_LARGURA, config.JOGADOR_ALTURA))
    except Exception as e:
        img_jogador = None
        print("FALHOU ao carregar a celula. Motivo:", e)

    # ---------- FONTES ----------
    fonte = pygame.font.SysFont("chalkboardse", 22)
    fonte_grande = pygame.font.SysFont("Marker Felt", 50)

    # Lê o recorde salvo em arquivo 
    recorde = dados.ler_recorde(CAMINHO_RECORDE)

    # Estado inicial e elementos da partida
    estado = "inicio"
    jogador, lista_virus, anticorpos, direcao_virus = iniciar_partida()

    # Controle do tempo entre disparos (cooldown)
    ultimo_tiro = 0

    rodando = True
    while rodando:
        relogio.tick(config.FPS) # O loop roda a 60 FPS
        agora = pygame.time.get_ticks()  # tempo atual em milissegundos

        # ---------- 1) EVENTOS (fechar janela, teclas pressionadas) ----------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:      # clicou no X da janela
                rodando = False

            if evento.type == pygame.KEYDOWN:
                # ESC: encerra o jogo (Regra/Controle da proposta)
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                # Na tela inicial: ESPAÇO começa o jogo
                if estado == "inicio" and evento.key == pygame.K_SPACE:
                    jogador, lista_virus, anticorpos, direcao_virus = iniciar_partida()
                    estado = "jogando"

                # Nas telas de fim: R reinicia
                if estado in ("vitoria", "derrota") and evento.key == pygame.K_r:
                    jogador, lista_virus, anticorpos, direcao_virus = iniciar_partida()
                    estado = "jogando" 

        # ---------- 2) ATUALIZAÇÃO (só quando está jogando) ----------
        if estado == "jogando":
            teclas = pygame.key.get_pressed()

            # Movimento da célula (esquerda/direita)
            direcao = 0
            if teclas[pygame.K_LEFT]:
                direcao = -1
            elif teclas[pygame.K_RIGHT]:
                direcao = 1
            entidades.mover_jogador(jogador, direcao)

            # Disparo com a barra de espaço (respeitando o cooldown)
            if teclas[pygame.K_SPACE]:
                if agora - ultimo_tiro >= config.ANTICORPO_COOLDOWN:
                    anticorpos.append(entidades.criar_anticorpo(jogador))
                    ultimo_tiro = agora
                    # ---- TOCAR SOM (tiro): som_tiro.play() ----
                    if som_tiro is not None:
                        som_tiro.play()

            # Move disparos e vírus
            entidades.mover_anticorpos(anticorpos, config.ANTICORPO_VELOCIDADE)
            direcao_virus = entidades.mover_virus(
                lista_virus, direcao_virus,
                config.VIRUS_VELOCIDADE_X, config.VIRUS_DESCIDA,
                config.LARGURA_TELA
            )

            # Verifica acertos (anticorpo x vírus) e soma pontos
            pontos = entidades.verificar_acertos(anticorpos, lista_virus)
            if pontos > 0:
                jogador["pontuacao"] += pontos
                # ---- TOCAR SOM (explosão): som_explosao.play() ----
                if som_explosao is not None:
                    som_explosao.play()

            # Limpa disparos que já saíram ou já acertaram
            anticorpos = entidades.remover_inativos(anticorpos)

            # Algum vírus chegou na base ou na célula? -> perde 1 vida
            if entidades.algum_virus_alcancou_a_base(lista_virus, jogador, config.LINHA_DEFESA_Y):
                jogador["vidas"] -= 1
                # Reposiciona a "onda" de vírus no topo para continuar a partida
                lista_virus = funcoes.criar_virus(config.VIRUS_LINHAS, config.VIRUS_COLUNAS)
                direcao_virus = 1
                anticorpos = []

            # Condições de fim de partida
            if funcoes.venceu(lista_virus):
                recorde = dados.atualizar_recorde(CAMINHO_RECORDE, jogador["pontuacao"])
                estado = "vitoria"
                # ---- TOCAR SOM (fim/vitória): som_fim.play() ----
                if som_fim is not None:
                    som_fim.play()

            elif funcoes.perdeu(jogador):
                recorde = dados.atualizar_recorde(CAMINHO_RECORDE, jogador["pontuacao"])
                estado = "derrota"
                # ---- TOCAR SOM (fim/derrota): som_fim.play() ----
                if som_fim is not None:
                    som_fim.play()

        # ---------- 3) DESENHO ----------
        tela.fill(config.FUNDO)  # limpa a tela com a cor de fundo

        if estado == "inicio":
            desenhar_texto_centralizado(tela, config.TITULO, fonte_grande, config.COR_VITORIA, -60)
            desenhar_texto_centralizado(tela, "Defenda o organismo dos virus!", fonte, config.TEXTO, -10)
            desenhar_texto_centralizado(tela, "Setas: mover   |   Espaco: atirar   |   ESC: sair", fonte, config.TEXTO, 30)
            desenhar_texto_centralizado(tela, "Aperte ESPACO para comecar", fonte, config.TEXTO_DESTAQUE, 80)

        elif estado == "jogando":
            desenhar_virus(tela, lista_virus, img_virus)
            desenhar_anticorpos(tela, anticorpos)
            desenhar_jogador(tela, jogador, img_jogador)
            desenhar_hud(tela, fonte, jogador, recorde, funcoes.contar_virus_vivos(lista_virus))

        elif estado == "vitoria":
            desenhar_texto_centralizado(tela, "VITORIA!", fonte_grande, config.COR_VITORIA, -40)
            desenhar_texto_centralizado(tela, "Pontuacao: " + str(jogador["pontuacao"]), fonte, config.TEXTO, 10)
            desenhar_texto_centralizado(tela, "Recorde: " + str(recorde), fonte, config.TEXTO_DESTAQUE, 40)
            desenhar_texto_centralizado(tela, "R: jogar de novo   |   ESC: sair", fonte, config.TEXTO, 90)

        elif estado == "derrota":
            desenhar_texto_centralizado(tela, "FIM DO JOGO", fonte_grande, config.COR_DERROTA, -40)
            desenhar_texto_centralizado(tela, "Pontuacao: " + str(jogador["pontuacao"]), fonte, config.TEXTO, 10)
            desenhar_texto_centralizado(tela, "Recorde: " + str(recorde), fonte, config.TEXTO_DESTAQUE, 40)
            desenhar_texto_centralizado(tela, "R: jogar de novo   |   ESC: sair", fonte, config.TEXTO, 90)

        pygame.display.flip()  # mostra na tela tudo que foi desenhado

    pygame.quit()

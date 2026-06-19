# ============================================================
# entidades.py
# ------------------------------------------------------------
# Funções que CRIAM e MOVIMENTAM os elementos do jogo, além das
# funções de COLISÃO:
#   - jogador (célula de defesa)
#   - anticorpos (disparos)
#   - vírus (movimento em grupo)
#   - colisões (anticorpo x vírus, vírus chegando na base)
#
# Importante: aqui também NÃO usamos pygame. Cada elemento é só
# um DICIONÁRIO com posição e tamanho. O desenho na tela fica
# por conta do arquivo jogo.py. Isso deixa a lógica testável.
# ============================================================

import config


# ------------------------------------------------------------
# JOGADOR (a célula de defesa)
# ------------------------------------------------------------
def criar_jogador():
    """Cria o jogador como um dicionário com todas as suas informações.

    A proposta pede um dicionário com posição, velocidade, vidas e
    pontuação -> é exatamente o que montamos aqui.
    """
    jogador = {
        "x": config.LARGURA_TELA // 2 - config.JOGADOR_LARGURA // 2,  # centralizado
        "y": config.ALTURA_TELA - config.JOGADOR_ALTURA - 12,          # quase no rodapé
        "largura": config.JOGADOR_LARGURA,
        "altura": config.JOGADOR_ALTURA,
        "velocidade": config.JOGADOR_VELOCIDADE,
        "vidas": config.VIDAS_INICIAIS,
        "pontuacao": 0,
    }
    return jogador


def mover_jogador(jogador, direcao):
    """Move o jogador na horizontal.

    direcao = -1  -> esquerda
    direcao = +1  -> direita
    direcao =  0  -> parado

    Também impede que a célula saia pelas laterais da tela
    (isso é testado em tests/, item 6 da proposta).
    """
    jogador["x"] += direcao * jogador["velocidade"]

    # Trava no limite esquerdo
    if jogador["x"] < 0:
        jogador["x"] = 0
    # Trava no limite direito
    limite_direito = config.LARGURA_TELA - jogador["largura"]
    if jogador["x"] > limite_direito:
        jogador["x"] = limite_direito


# ------------------------------------------------------------
# ANTICORPOS (os disparos do jogador)
# ------------------------------------------------------------
def criar_anticorpo(jogador):
    """Cria um disparo saindo do topo, no centro da célula."""
    anticorpo = {
        "x": jogador["x"] + jogador["largura"] // 2 - config.ANTICORPO_LARGURA // 2,
        "y": jogador["y"],
        "largura": config.ANTICORPO_LARGURA,
        "altura": config.ANTICORPO_ALTURA,
        "ativo": True,   # vira False quando sai da tela ou acerta um vírus
    }
    return anticorpo


def mover_anticorpos(anticorpos, velocidade):
    """Move todos os disparos ATIVOS para cima.

    Quando um disparo sai pela parte de cima da tela, marcamos
    como inativo (ativo = False).
    """
    for anticorpo in anticorpos:
        if anticorpo["ativo"]:
            anticorpo["y"] -= velocidade
            if anticorpo["y"] + anticorpo["altura"] < 0:
                anticorpo["ativo"] = False


def remover_inativos(anticorpos):
    """Devolve uma nova lista só com os disparos ainda ativos.

    Fazemos isso para a lista não crescer para sempre (cada tiro
    que some é descartado).
    """
    ativos = []
    for anticorpo in anticorpos:
        if anticorpo["ativo"]:
            ativos.append(anticorpo)
    return ativos


# ------------------------------------------------------------
# VÍRUS (movimento do grupo, estilo Space Invaders)
# ------------------------------------------------------------
def mover_virus(lista_virus, direcao, velocidade_x, descida, largura_tela):
    """Move o GRUPO de vírus de lado e faz descer quando bate na borda.

    Como funciona:
      1. Descobrimos a borda esquerda (menor x) e a borda direita
         (maior x + largura) considerando só os vírus vivos.
      2. Se o próximo passo encostaria na lateral da tela, então
         o grupo TODO desce um pouco e inverte a direção.
      3. Senão, o grupo anda normalmente para os lados.

    Devolve a nova 'direcao' (pode ter invertido), para o jogo.py
    guardar e usar no próximo quadro.
    """
    tem_vivo = False
    min_x = largura_tela
    max_x = 0

    # Acha as bordas do grupo de vírus vivos
    for virus in lista_virus:
        if virus["vivo"]:
            tem_vivo = True
            if virus["x"] < min_x:
                min_x = virus["x"]
            if virus["x"] + virus["largura"] > max_x:
                max_x = virus["x"] + virus["largura"]

    if not tem_vivo:
        return direcao  # não há ninguém para mover

    # Indo para a direita e quase saindo pela direita -> desce e inverte
    if direcao > 0 and max_x + velocidade_x >= largura_tela:
        direcao = -1
        for virus in lista_virus:
            if virus["vivo"]:
                virus["y"] += descida
    # Indo para a esquerda e quase saindo pela esquerda -> desce e inverte
    elif direcao < 0 and min_x - velocidade_x <= 0:
        direcao = 1
        for virus in lista_virus:
            if virus["vivo"]:
                virus["y"] += descida
    # Caminho normal: anda de lado
    else:
        for virus in lista_virus:
            if virus["vivo"]:
                virus["x"] += direcao * velocidade_x

    return direcao


# ------------------------------------------------------------
# COLISÕES
# ------------------------------------------------------------
def colidiu(a, b):
    """Verifica se dois retângulos (a e b) estão se encostando.

    'a' e 'b' são dicionários que têm: x, y, largura, altura.
    Esta é a clássica colisão de retângulos (AABB). Devolve
    True se há sobreposição e False caso contrário.

    Esta função é testada em tests/ (item 2 da lista de testes).
    """
    return (
        a["x"] < b["x"] + b["largura"] and
        a["x"] + a["largura"] > b["x"] and
        a["y"] < b["y"] + b["altura"] and
        a["y"] + a["altura"] > b["y"]
    )


def verificar_acertos(anticorpos, lista_virus):
    """Confere se algum anticorpo acertou algum vírus.

    Se o tiro estiver tocando mais de um vírus ao mesmo tempo,
    acerta o que está MAIS À FRENTE (mais perto do jogador, ou seja,
    o de maior y) — que é o que faz sentido visualmente.
    """
    pontos_ganhos = 0
    for anticorpo in anticorpos:
        if not anticorpo["ativo"]:
            continue

        # Procura, entre os vírus tocados, o mais à frente (maior y)
        alvo = None
        for virus in lista_virus:
            if virus["vivo"] and colidiu(anticorpo, virus):
                if alvo is None or virus["y"] > alvo["y"]:
                    alvo = virus

        # Mata só esse e consome o tiro
        if alvo is not None:
            alvo["vivo"] = False
            anticorpo["ativo"] = False
            pontos_ganhos += alvo["pontos"]

    return pontos_ganhos


def algum_virus_alcancou_a_base(lista_virus, jogador, linha_defesa_y):
    """Verifica se algum vírus chegou na zona de defesa.

    Conta como "chegou" se:
      - o vírus passou da linha de defesa (perto da base), OU
      - o vírus colidiu diretamente com a célula do jogador.

    Devolve True/False. Quem trata a perda de vida é o jogo.py.
    """
    for virus in lista_virus:
        if not virus["vivo"]:
            continue
        # Passou da linha de defesa
        if virus["y"] + virus["altura"] >= linha_defesa_y:
            return True
        # Bateu na própria célula
        if colidiu(virus, jogador):
            return True
    return False

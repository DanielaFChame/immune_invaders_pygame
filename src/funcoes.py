# ============================================================
# funcoes.py
# ------------------------------------------------------------
# Funções AUXILIARES de LÓGICA do jogo:
#   - criar os vírus (a "matriz" de inimigos)
#   - contar quantos vírus ainda estão vivos
#   - verificar condição de vitória
#   - verificar condição de derrota
# ============================================================

import config


def criar_virus(linhas, colunas):
    """Cria e devolve uma LISTA DE DICIONÁRIOS, um por vírus.

    Os vírus são posicionados como uma matriz (linhas x colunas),
    parecido com o Space Invaders. Usamos dois 'for' encaixados
    (um para as linhas e outro para as colunas).

    Cada vírus é um dicionário com:
      x, y           - posição na tela
      largura,altura - tamanho (usado no desenho e na colisão)
      vivo           - True enquanto não foi atingido
      pontos         - quanto vale ao ser destruído
    """
    lista_virus = []
    for linha in range(linhas):
        for coluna in range(colunas):
            # Calcula a posição de cada vírus a partir da linha/coluna
            x = config.VIRUS_MARGEM_ESQUERDA + coluna * (config.VIRUS_LARGURA + config.VIRUS_ESPACO_X)
            y = config.VIRUS_MARGEM_TOPO + linha * (config.VIRUS_ALTURA + config.VIRUS_ESPACO_Y)

            virus = {
                "x": x,
                "y": y,
                "largura": config.VIRUS_LARGURA,
                "altura": config.VIRUS_ALTURA,
                "vivo": True,
                "pontos": config.VIRUS_PONTOS,
            }
            lista_virus.append(virus)

            # ----------------------------------------------------------
            # MELHORIA (opcional): tipos diferentes de vírus.
            # criar um campo virus["tipo"] = "comum" / "forte" e usar
            # cores/velocidades diferentes no desenho.
            # ----------------------------------------------------------
    return lista_virus


def contar_virus_vivos(lista_virus):
    """Conta quantos vírus ainda estão vivos na lista."""
    quantidade = 0
    for virus in lista_virus:
        if virus["vivo"]:
            quantidade += 1
    return quantidade


def venceu(lista_virus):
    """Condição de VITÓRIA: True quando não sobrou nenhum vírus vivo."""
    return contar_virus_vivos(lista_virus) == 0


def perdeu(jogador):
    """Condição de DERROTA: True quando as vidas chegam a zero (ou menos)."""
    return jogador["vidas"] <= 0

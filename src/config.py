# ============================================================
# config.py
# ------------------------------------------------------------
# Arquivo com as configurações gerais do jogo.
# Neste arquivo são realizadas quaisquer mudanças de 
# cor, o tamanho da tela, a velocidade dos vírus, a quantidade
# de vidas, etc.
# ============================================================

# ---------- TELA ----------
LARGURA_TELA = 800      # largura da janela em pixels
ALTURA_TELA = 600       # altura da janela em pixels
FPS = 60                # quadros por segundo (velocidade do jogo)
TITULO = "Immuno Invaders"

# ---------- CORES (tuplas R, G, B) ----------
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (220, 60, 60)
VERDE = (80, 200, 120)
AZUL = (90, 160, 230)
AMARELO = (240, 220, 80)
ROXO = (170, 90, 200)
CINZA = (120, 120, 120)
FUNDO = (15, 20, 35)        

# ---------- JOGADOR (célula de defesa) ----------
JOGADOR_LARGURA = 54
JOGADOR_ALTURA = 30
JOGADOR_VELOCIDADE = 6      # quantos pixels a célula anda por quadro
VIDAS_INICIAIS = 3          # Regra 1 da proposta: começa com 3 vidas

# ---------- ANTICORPO (o disparo do jogador) ----------
ANTICORPO_LARGURA = 6
ANTICORPO_ALTURA = 16
ANTICORPO_VELOCIDADE = 9    # sobe rápido pela tela
ANTICORPO_COOLDOWN = 300    # tempo mínimo (em milissegundos) entre um tiro e outro

# ---------- VÍRUS (inimigos) ----------
VIRUS_LARGURA = 38
VIRUS_ALTURA = 30
VIRUS_VELOCIDADE_X = 1      # velocidade lateral do grupo de vírus
VIRUS_DESCIDA = 18          # quanto os vírus descem quando batem na borda
VIRUS_LINHAS = 4            # nº de fileiras de vírus (a "matriz" de inimigos)
VIRUS_COLUNAS = 8           # nº de colunas de vírus
VIRUS_ESPACO_X = 22         # espaço horizontal entre os vírus
VIRUS_ESPACO_Y = 18         # espaço vertical entre os vírus
VIRUS_MARGEM_TOPO = 60      # distância do topo da tela até a 1ª fileira
VIRUS_MARGEM_ESQUERDA = 60  # distância da esquerda até a 1ª coluna
VIRUS_PONTOS = 10           # cada vírus eliminado vale 10 pontos 

# Linha imaginária perto da base: se um vírus passar dela, o jogador perde vida
LINHA_DEFESA_Y = ALTURA_TELA - 70

# ---------- ARQUIVO DE RECORDE ----------
ARQUIVO_RECORDE = "recorde.txt"   # nome do arquivo que guarda o recorde

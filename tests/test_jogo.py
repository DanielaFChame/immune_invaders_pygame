# ============================================================
# test_jogo.py
# ------------------------------------------------------------
# Testes simples das funções de LÓGICA do jogo (item 18 da proposta).
#
# Estes testes NÃO abrem a janela do jogo e NÃO usam pygame.
# Por isso eles rodam rápido e em qualquer computador.
#
# Como rodar (na pasta principal do projeto):
#   - Forma simples:   python tests/test_jogo.py
#   - Com pytest:      pytest
# ============================================================

import os
import sys

# Avisa ao Python onde está a pasta src/ (para conseguir importar os módulos)
PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(PASTA_RAIZ, "src"))

import config
import funcoes
import entidades
import dados


# 1) A pontuação deve aumentar quando um vírus é eliminado.
def test_pontuacao_aumenta_ao_eliminar_virus():
    # Um vírus e um anticorpo exatamente em cima dele
    virus = {"x": 100, "y": 100, "largura": 38, "altura": 30, "vivo": True, "pontos": 10}
    anticorpo = {"x": 110, "y": 105, "largura": 6, "altura": 16, "ativo": True}

    pontos = entidades.verificar_acertos([anticorpo], [virus])

    assert pontos == 10            # ganhou 10 pontos
    assert virus["vivo"] is False  # o vírus morreu
    assert anticorpo["ativo"] is False  # o disparo foi consumido


# 2) A função de colisão deve detectar quando dois objetos se encostam.
def test_colisao_detecta_sobreposicao():
    a = {"x": 0, "y": 0, "largura": 10, "altura": 10}
    b_encostando = {"x": 5, "y": 5, "largura": 10, "altura": 10}
    b_longe = {"x": 100, "y": 100, "largura": 10, "altura": 10}

    assert entidades.colidiu(a, b_encostando) is True
    assert entidades.colidiu(a, b_longe) is False


# 3) A vitória deve ser True quando não há mais vírus vivos.
def test_vitoria_quando_lista_sem_virus_vivos():
    sem_virus = []
    todos_mortos = [{"vivo": False}, {"vivo": False}]
    ainda_tem = [{"vivo": False}, {"vivo": True}]

    assert funcoes.venceu(sem_virus) is True
    assert funcoes.venceu(todos_mortos) is True
    assert funcoes.venceu(ainda_tem) is False


# 4) A derrota deve ser True quando as vidas chegam a zero.
def test_derrota_quando_vidas_zeram():
    jogador_vivo = {"vidas": 1}
    jogador_morto = {"vidas": 0}

    assert funcoes.perdeu(jogador_vivo) is False
    assert funcoes.perdeu(jogador_morto) is True


# 5) O recorde deve ser atualizado SÓ quando a pontuação atual é maior.
def test_recorde_atualiza_apenas_se_maior():
    caminho = os.path.join(PASTA_RAIZ, "tests", "_recorde_teste.txt")

    # Garante começo limpo
    dados.salvar_recorde(caminho, 50)

    # Pontuação menor: NÃO muda o recorde
    resultado = dados.atualizar_recorde(caminho, 30)
    assert resultado == 50
    assert dados.ler_recorde(caminho) == 50

    # Pontuação maior: muda o recorde
    resultado = dados.atualizar_recorde(caminho, 80)
    assert resultado == 80
    assert dados.ler_recorde(caminho) == 80

    # Limpa o arquivo de teste
    if os.path.exists(caminho):
        os.remove(caminho)


# 6) O jogador não pode ultrapassar os limites laterais da tela.
def test_jogador_nao_passa_dos_limites():
    jogador = entidades.criar_jogador()

    # Empurra muito para a esquerda
    for _ in range(1000):
        entidades.mover_jogador(jogador, -1)
    assert jogador["x"] >= 0

    # Empurra muito para a direita
    for _ in range(1000):
        entidades.mover_jogador(jogador, 1)
    assert jogador["x"] <= config.LARGURA_TELA - jogador["largura"]


# 7) Quando o tiro toca dois vírus empilhados, deve matar o da frente (maior y)
def test_tiro_acerta_o_virus_da_frente():
    virus_tras   = {"x": 100, "y": 100, "largura": 36, "altura": 36, "vivo": True, "pontos": 10}
    virus_frente = {"x": 100, "y": 130, "largura": 36, "altura": 36, "vivo": True, "pontos": 10}
    tiro = {"x": 115, "y": 128, "largura": 6, "altura": 16, "ativo": True}

    entidades.verificar_acertos([tiro], [virus_tras, virus_frente])

    assert virus_frente["vivo"] is False   # o da frente morreu
    assert virus_tras["vivo"] is True       # o de trás continua vivo


# ------------------------------------------------------------
# Permite rodar "python tests/test_jogo.py" sem instalar pytest.
# ------------------------------------------------------------
if __name__ == "__main__":
    testes = [
        test_pontuacao_aumenta_ao_eliminar_virus,
        test_colisao_detecta_sobreposicao,
        test_vitoria_quando_lista_sem_virus_vivos,
        test_derrota_quando_vidas_zeram,
        test_recorde_atualiza_apenas_se_maior,
        test_jogador_nao_passa_dos_limites,
    ]
    passou = 0
    for teste in testes:
        teste()                       # se algum assert falhar, o programa para e mostra o erro
        print("OK:", teste.__name__)
        passou += 1
    print("\nTodos os", passou, "testes passaram!")

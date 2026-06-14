# ============================================================
# dados.py
# ------------------------------------------------------------
# Arquivo responsável por LER e ESCREVER em arquivo.
# Aqui guardamos o RECORDE (a maior pontuação já feita).
#
# Fluxo previsto na proposta:
#   - Ao iniciar o jogo: ler o recorde do arquivo.
#   - Ao terminar a partida: se a pontuação atual for maior
#     que o recorde, atualizar o arquivo.
# ============================================================


def ler_recorde(caminho):
    """Lê o recorde salvo no arquivo e devolve um número inteiro.

    Se o arquivo não existir (primeira vez que o jogo roda) ou
    estiver vazio/estragado, devolvemos 0 em vez de quebrar o jogo.
    """
    try:
        # 'with' fecha o arquivo sozinho no final, mesmo se der erro
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()  # tira espaços e quebras de linha
            if conteudo == "":
                return 0
            return int(conteudo)   # transforma o texto lido em número
    except FileNotFoundError:
        # O arquivo ainda não foi criado -> não há recorde -> 0
        return 0
    except ValueError:
        # O arquivo tinha algo que não é número -> ignora e usa 0
        return 0


def salvar_recorde(caminho, pontuacao):
    """Escreve a pontuação no arquivo (sobrescreve o que estava lá)."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))   # número precisa virar texto para gravar


def atualizar_recorde(caminho, pontuacao_atual):
    """Compara a pontuação atual com o recorde salvo.

    - Se a pontuação atual for MAIOR, salva o novo recorde e o devolve.
    - Se não for, mantém o recorde antigo e o devolve.

    Devolver o recorde "vigente" facilita mostrar o valor certo na tela.
    """
    recorde = ler_recorde(caminho)
    if pontuacao_atual > recorde:
        salvar_recorde(caminho, pontuacao_atual)
        return pontuacao_atual
    return recorde

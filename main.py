# ============================================================
# main.py
# ------------------------------------------------------------
# Arquivo PRINCIPAL. É ele que você roda no terminal:
#       python main.py
#
# Tarefa dele:
#   1. Avisar ao Python onde estão os arquivos da pasta src/
#      (assim o jogo consegue achar config.py, jogo.py, etc.)
#   2. Chamar a função que executa o jogo.
# ============================================================

import os
import sys

# Adiciona a pasta "src" à lista de lugares onde o Python procura
# arquivos para importar. Sem isso, "import jogo" não funcionaria.
PASTA_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.append(PASTA_SRC)

import jogo  # noqa: E402  (importado depois de ajustar o caminho, de propósito)


if __name__ == "__main__":
    # Só roda o jogo se este arquivo for executado diretamente.
    jogo.executar()

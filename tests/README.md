# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_jogo.py`: testa funções de lógica do jogo nos módulos `entidades`, `funcoes` e `dados` (colisão, pontuação, vitória, derrota, recorde e limites do jogador).

## Como executar

```bash
python -m pytest
```

## Boas praticas

- Crie testes para toda regra de pontuacao, vidas e condicoes de fim de jogo.
- Prefira funcoes pequenas e testaveis no modulo `src/funcoes.py`.

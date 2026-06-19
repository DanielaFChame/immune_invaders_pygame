# Immuno Invaders

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Jogo de tiro e sobrevivência inspirado em *Space Invaders*. O jogador controla uma **célula de defesa** do sistema imunológico e precisa eliminar os **vírus invasores** com disparos de **anticorpos** antes que eles cheguem à base da tela.

## Integrantes do grupo

- Daniela Ferreira Chame

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
  - `config.py/`: configurações gerais (tela, FPS, cores, velocidades, vidas).
  - `jogo.py/`: loop principal, estados da partida e desenho na tela.
  - `entidades.py/`: jogador, vírus, anticorpos e colisões.
  - `funcoes.py/`: criação dos vírus, contagem e condições de vitória/derrota.
- `data/`: arquivos persistentes. Contém recorde.txt, com o maior recorde (lido ao iniciar e atualizado ao fim da partida). A pasta é criada automaticamente pelo jogo, caso não exista.
- `tests/`: testes das funções de lógica.
- `docs/`: documentação do projeto, incluindo proposta inicial.
- `assets/`: pasta opcional para imagens e sons (usada apenas nas melhorias; por padrão o jogo desenha com formas geométricas e não depende dela).

## Descrição do jogo

O jogo se passa, de forma simplificada, dentro de um organismo. O jogador controla uma célula de defesa do sistema imunológico, posicionada na parte inferior da tela, enquanto vírus invasores surgem no topo, organizados em fileiras, e descem aos poucos em direção à base. A célula dispara anticorpos para cima para destruir os vírus. Cada vírus eliminado aumenta a pontuação. A partida termina em vitória quando todos os vírus são eliminados e em derrota quando o jogador perde todas as vidas. O maior recorde é salvo em arquivo e exibido na tela.

## Objetivo do jogador

Defender o organismo eliminando todos os vírus invasores com os disparos de anticorpos, sem deixar que eles alcancem a base da tela ou colidam com a célula, e sem perder todas as vidas. Vence quem limpa a tela de vírus; o desafio extra é fazer a maior pontuação possível e superar o recorde salvo.

## Regras do jogo

- A célula de defesa se movimenta na horizontal usando as setas esquerda e direita.
- A barra de espaço dispara anticorpos para cima (com um pequeno intervalo entre tiros).
- Cada vírus eliminado vale 10 pontos.
- O jogador começa com 3 vidas.
- O jogador perde 1 vida quando um vírus alcança a base (linha de defesa) ou colide com a célula; nesse caso a onda de vírus reaparece no topo.
- A partida termina em vitória ao eliminar todos os vírus.
- A partida termina em derrota ao perder todas as vidas.
- A maior pontuação é salva em arquivo e mostrada como recorde.
  
## Controles

- Seta para esquerda: mover a célula para a esquerda
- Seta para direita: mover a célula para a direita
- Espaço: disparar anticorpo (e iniciar a partida na tela inicial)
- R: jogar de novo (nas telas de vitória ou derrota)
- ESC: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/DanielaFChame/immune_invaders_pygame.git
cd immune_invaders_pygame
pip install pygame
python main.py
```

## Como executar os testes

```bash
python -m pytest
```
## Assets Externos
- Virus: <a href="https://www.flaticon.com/free-icons/virus" title="virus icons">Virus icons created by Good Ware - Flaticon</a>
- Célula: <a href="https://www.flaticon.com/free-icons/white-blood-cell" title="white blood cell icons">White blood cell icons created by Freepik - Flaticon</a>
- Sons: Gerados usando jsfxr.me 

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.

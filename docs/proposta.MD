# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Immuno Invaders

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome: Daniela Ferreira Chame

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Jogo de tiro e sobrevivência simples inspirado em Space Invaders, no qual o jogador controla uma célula de defesa do sistema imunológico que precisa eliminar vírus invasores antes que eles atinjam a parte inferior da tela.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

O jogo será ambientado de forma simplificada dentro de um organismo. Na tela principal, o jogador controlará uma célula de defesa, representando uma célula do sistema imunológico, posicionada na parte inferior da tela. Na parte superior, aparecerão vírus invasores organizados em fileiras ou surgindo em ondas.

O jogador deverá mover a célula para a esquerda e para a direita, disparando anticorpos ou projéteis imunológicos para destruir os vírus. Os inimigos avançarão gradualmente em direção à parte inferior da tela. A dificuldade poderá aumentar conforme o jogador elimina vírus ou avança de fase.

Os principais desafios serão acertar os vírus, evitar que eles cheguem à região de defesa do organismo e administrar as vidas disponíveis.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Objetivo:

O objetivo principal do jogador é defender o organismo, acertando alvos, os quais são os vírus invasores, antes que eles alcancem a parte inferior da tela ou antes que o jogador perca todas as vidas.

## 6. Regras principais

Liste as principais regras do jogo.

- Regra 1: O jogador começa a partida com 3 vidas.
- Regra 2: O jogador controla uma célula de defesa que pode se mover horizontalmente na parte inferior da tela.
- Regra 3: O jogador pode disparar anticorpos para atingir e eliminar vírus.
- Regra 4: Cada vírus eliminado aumenta a pontuação do jogador.
- Regra 5: O jogador perde uma vida se um vírus atingir a área inferior da tela ou colidir com a célula de defesa.
- Regra 6: A partida termina em vitória se o jogador eliminar todos os vírus da fase.
- Regra 7: A partida termina em derrota se o jogador perder todas as vidas.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

O jogador vence a partida quando consegue eliminar todos os vírus da fase antes de perder todas as vidas ou sobreviver até o tempo acabar. 

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

O jogador perde quando suas vidas chegam a zero. Isso pode acontecer quando vírus atingem a parte inferior da tela ou quando colidem com a célula de defesa. A partida também poderá ser encerrada pelo jogador ao pressionar a tecla ESC ou fechar a janela do jogo.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

O jogador controlará uma célula de defesa do sistema imunológico, posicionada na parte inferior da tela. Essa célula poderá será controlada pelas setas do teclado e poderá se mover para a esquerda e para a direita e disparar anticorpos contra os vírus.

## Obstáculos, inimigos ou desafios

Descrição:

Os inimigos serão vírus invasores que aparecerão na parte superior da tela. Eles poderão estar organizados em linhas e colunas, movendo-se lateralmente e descendo aos poucos, de maneira semelhante à lógica de Space Invaders. O principal desafio será impedir que eles cheguem à parte inferior da tela.

## Itens, alvos ou objetos de interação

Descrição:

Os principais alvos serão os vírus. O jogador interage com eles por meio dos disparos de anticorpos. Caso haja tempo, poderão ser adicionados itens especiais, como uma molécula de energia que recupera uma vida ou aumenta temporariamente a velocidade dos disparos.

## Pontuação, vidas, tempo ou progresso

Descrição:

O jogador começará com 3 vidas. Cada vírus eliminado concederá 10 pontos. A pontuação será exibida na tela junto com a quantidade de vidas restantes. O progresso da fase será representado pela quantidade de vírus ainda vivos.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

- Tecla/comando: Seta para a esquerda — mover a célula para a esquerda.
- Tecla/comando: Seta para a direita — mover a célula para a direita.
- Tecla/comando: Barra de espaço — disparar anticorpo.
- Tecla/comando: ESC — sair da partida ou encerrar o jogo.

## 11. Organização inicial do código

Organização planejada:

- `main.py`: arquivo principal, responsável por iniciar o jogo.
- `src/config.py`: arquivo com configurações gerais, como tamanho da tela, FPS, cores, velocidade inicial e quantidade de vidas.
- `src/jogo.py`: arquivo com o loop principal do jogo, atualização dos elementos e controle dos estados da partida.
- `src/entidades.py`: arquivo com funções relacionadas ao jogador, vírus, disparos e colisões.
- `src/funcoes.py`: arquivo com funções auxiliares, como criação de inimigos, atualização da pontuação e verificação de vitória ou derrota.
- `src/dados.py`: contém funções de leitura e escrita de arquivos.


## 12. Recursos externos previstos


Inicialmente, serão usadas formas geométricas simples desenhadas com o próprio Pygame, como retângulos, círculos ou sprites básicos. Isso reduz a dependência de recursos externos e facilita a entrega da versão mínima.

Caso haja tempo, poderão ser usados sons gratuitos e imagens simples de domínio livre ou com licença gratuita, o uso e a fonte destes elementos serão indicadas no arquivo README.md.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementar corretamente a colisão entre os anticorpos disparados pelo jogador e os vírus.
- Dificuldade 2: Controlar o movimento dos vírus em grupo, especialmente a mudança de direção e a descida gradual.
- Dificuldade 3: Organizar o código em funções e arquivos separados sem deixar o programa confuso.
- Dificuldade 4: Criar testes simples para funções de lógica, principalmente pontuação, colisão e condição de vitória ou derrota.
- Dificuldade 5: Fazer a leitura e escrita de arquivo para salvar o recorde do jogador.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

A versão mínima do jogo terá uma tela principal de jogo, uma célula de defesa controlada pelo teclado, vírus inimigos na parte superior da tela, disparos de anticorpos, colisão entre disparos e vírus, sistema de pontuação, sistema de vidas, condição de vitória ao eliminar todos os vírus e condição de derrota ao perder todas as vidas.

Também serão incluídos um arquivo README.md com documentação básica, a proposta preenchida no arquivo docs/proposta.md, uso de pelo menos uma estrutura de dados para armazenar os vírus e os disparos, escrita ou leitura de arquivo para salvar o recorde e testes simples para funções de lógica do jogo.

## 15. Possíveis melhorias, caso haja tempo


- Melhoria 1: Criar aumento progressivo de dificuldade, com vírus se movendo mais rápido a cada fase.
- Melhoria 2: Adicionar diferentes tipos de vírus, com pontuações ou velocidades diferentes.
- Melhoria 3: Adicionar item especial de recuperação de vida ou disparo mais rápido.
- Melhoria 4: Adicionar efeitos sonoros para disparo, colisão e fim de jogo.
- Melhoria 5: Criar ranking simples com os melhores recordes salvos em arquivo.

## 16. Estrutura de Dados que poderão ser utilizadas:

O jogo poderá utilizar as seguintes estruturas de dados:

- Lista para armazenar os vírus ativos na tela.
- Lista para armazenar os disparos do jogador.
- Dicionário para armazenar informações do jogador, como posição, velocidade, vidas e pontuação.
- Tuplas para representar posições, tamanhos ou cores.
- Lista de dicionários para representar diferentes tipos de vírus, com atributos como posição, velocidade, pontuação e estado.

## 17. Uso previsto de arquivos: 

O jogo utilizará arquivo para salvar o recorde do jogador. Ao iniciar o jogo, o programa poderá ler o arquivo de recorde. Ao final da partida, se a pontuação atual for maior que o recorde salvo, o arquivo será atualizado.

Arquivo previsto: recorde.txt

Uso previsto:

- Ler o maior recorde ao iniciar o jogo.
- Exibir o recorde na tela.
- Atualizar o recorde ao final da partida, se necessário.

Caso haja tempo, também poderá ser criado um arquivo para ranking com mais de uma pontuação.

## 18. Testes Planejados: 

- Testar se a pontuação aumenta corretamente quando um vírus é eliminado.
- Testar se a função de colisão identifica corretamente quando dois objetos se encostam.
- Testar se a condição de vitória retorna verdadeiro quando não há mais vírus na lista.
- Testar se a condição de derrota retorna verdadeiro quando as vidas chegam a zero.
- Testar se o recorde é atualizado apenas quando a pontuação atual é maior que o recorde anterior.
- Testar se o jogador não ultrapassa os limites laterais da tela.



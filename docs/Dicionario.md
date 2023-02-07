# Dicionário de Dados

## Área
#### Local onde se encontra o personagem.

| Atributo  | Classe       | Tipo    | Tamanho | Descrição                                         | Exemplo    |
| --------- | ------------ | ------- | ------- | ------------------------------------------------- | ---------- |
| idArea    | Determinante | int     | 1       | Identificação da área                             | 1          |
| descrição | Simples      | varchar | 50      | Detalhamento das características da área          | Zona norte |


## Arma
#### Item que possui efeito nos NPCs

| Atributo  | Classe       | Tipo    | Tamanho | Descrição                                | Exemplo                      |
| --------- | ------------ | ------- | ------- | ---------------------------------------- | ---------------------------- |
| idItem    | Determinante | int     | 1       | Identificação do item                    | 1                            |
| preço     | Simples      | int     | 3       | Valor da arma                            | 10                           |
| tipo      | Simples      | varchar | 20      | Qual o modelo da arma utilizada          | AK-47                        |
| descricao | Simples      | varchar | 50      | Detalhamento das características da arma | arma de disparos automáticos |
| qtdDano   | Determinante | int     | 3       | Quantidade de dano que a Arma causa      | 70                           |
| qtdBalas  | Simples      | int     | 3       | Capacidade de armazenamento da arma      | 35                           |


## Comida 
#### Item consumível que cura o personagem.

| Atributo          | Classe       | Tipo    | Tamanho | Descrição                                     | Exemplo    |
| ----------------- | ------------ | ------- | ------- | --------------------------------------------- | ---------- |
| idItem            | Determinante | int     | 1       | Identificação do item                         | 1          |
| tipo              | Simples      | varchar | 20      | Qual o tipo de comida a ser utilizada         | Feijuca    |
| Nome              | Simples      | varchar | 20      | Qual o tipo de comida a ser utilizada         | Feijuca    |
| Preço             | Simples      | int     | 3       | Qual o valor da comida                        | 2          |
| descricao         | Simples      | varchar | 50      | Detalhamento das características da comida    | Consumível |
| txRecuperaçãoVida | Simples      | int     | 2       | Quantidade de pontos de vida a ser recuperado | 35         |


## Droga 
#### Item consumível que afeta o personagem positiva e negativamente.

|Atributo| Classe| Tipo | Tamanho | Descrição| Exemplo |
| ---- | ---- | ---- | ---- | ---- | ---- | 
| idItem | Determinante | int | 1 | Identificação do item | 1 |
| tipo | Simples | varchar | 20 | Qual o tipo de droga a ser utilizada | analgésico |
| descricao | Simples | varchar | 50 | Detalhamento das características da droga | Cura um pouco de vida, mas pode causar desmaios |
| vantagem | Simples   | varchar | 30 | Adiciona uma vantagem ao Jogador | recupera 5HP |
| desvantagem | Simples   | varchar | 30 | Adiciona uma desvantagem ao Jogador | 5% de chance de desmaios |


## Inventario
#### Onde os items do Jogador se encontram.

| Atributo     | Classe       | Tipo | Tamanho | Descrição                          | Exemplo |
| ------------ | ------------ | ---- | ------- | ---------------------------------- | ------- |
| idInventário | Determinante | int  | 1       | Identificação do inventário        | 1       |
| idJogador    | Determinante | int  | 1       | Identificação do Jogador           | 1       |

## Jogador
#### Personagem criado pelo usuário.

| Atributo  | Classe       | Tipo    | Tamanho | Descrição                        | Exemplo |
| --------- | ------------ | ------- | ------- | -------------------------------- | ------- |
| idJogador | Determinante | int     | 1       | Identificação do Jogador         | 1       |
| nome      | Simples      | varchar | 30      | Nome do Jogador                  | Jack    |
| vida      | Simples      | int     | 3       | Pontos de vida do Jogador        | 100     |
| xp        | Simples      | int     | 3       | Pontos de experiência do Jogador | 100     |
| dinheiro        | Simples      | int     | 3       | Pontos de experiência do Jogador | 100     |
| nivel procurado        | Simples      | int     | 3       | Pontos de experiência do Jogador | 100     |
| idVeiculo         | Determinante | int     | 1                        | Identificação do Veiculo             | 1         |
| idNPC    | Determinante | int  | 3       | Identificação do NPC                | 100     |
| idArea    | Determinante | int     | 1       | Identificação da área                             | 1          |
| xp        | Simples      | int     | 3       | Pontos de experiência do Jogador | 100     |

## Loja
#### Local onde o personagem pode comprar itens.

| Atributo  | Classe       | Tipo    | Tamanho | Descrição                        | Exemplo |
| --------- | ------------ | ------- | ------- | -------------------------------- | ---- |
| nomeLoja  | Determinante | varchar | 20      | Nome atribuído a Loja            | Happy and Guns |
| idArea    | Determinante | int     | 1       | Chave estrangeira para a área    | 1 |
| idItem    | Determinante | int     | 1       | Chave estrangeira para o item    | 1 |
| descrição | Simples      | varchar | 50      | Descreve o propósito da loja     | loja de armas |
| estoque   | Simples      | varchar | 20      | Lista de Items que a loja possui | 'AK-47', 'AM-1','P90','P40','ROCKET' |


## Mapa
#### Espaço jogável contendo Áreas
| Atributo  | Classe       | Tipo    | Tamanho | Descrição                                | Exemplo          |
| --------- | ------------ | ------- | ------- | ---------------------------------------- | ---------------- |
| idMapa    | Determinante | int     | 1       | Identificação do mapa                    | 1                |
| descrição | Simples      | varchar | 50      | Detalhamento das características do mapa | centro da cidade |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue aliada.

| Atributo   | Classe       | Tipo | Tamanho | Descrição                                  | Exemplo |
| ---------- | ------------ | ---- | ------- | ------------------------------------------ | ------- |
| idNPC      | Determinante | int  | 3       | Chave estrangeira para o NPC               | 100     |
| tipoAliado | Simples      | int  | 3       | Identificação como membro de gangue aliada | 100     |
| vida     | Simples      | int  | 3       | Quantidade de vida que o NPC possui | 100     |

## Membro de gangue inimiga
#### Personagens não jogável que faz parte de uma gangue inimiga.

| Atributo    | Classe       | Tipo | Tamanho | Descrição                                   | Exemplo |
| ----------- | ------------ | ---- | ------- | ------------------------------------------- | ------- |
| idNPC       | Determinante | int  | 3       | Chave estrangeira para o NPC                | 200     |
| tipoInimigo | Simples      | int  | 3       | Identificação como membro de gangue inimiga | 200     |
| vida     | Simples      | int  | 3       | Quantidade de vida que o NPC possui | 100     |


## Policial
#### Personagens não jogável que interage com Jogador e com Membro de gangue.

| Atributo | Classe  | Tipo    | Tamanho | Descrição                        | Exemplo |
| -------- | ------- | ------- | ------- | -------------------------------- | ------- |
| idNPC    | simples | int     | 3       | Chave estrangeira para o NPC     | 300     |
| tipoPolicial     | simples | varchar | 1       | nível de dificuldade do policial | 1       |
| vida     | Simples      | int  | 3       | Quantidade de vida que o NPC possui | 100     |
| DanoPolicial     | Simples      | int  | 3       | Quantidade de dano do policial | 100     |


## NPC
#### Personagens não jogáveis.

| Atributo | Classe       | Tipo | Tamanho | Descrição                           | Exemplo |
| -------- | ------------ | ---- | ------- | ----------------------------------- | ------- |
| idNPC    | Determinante | int  | 3       | Identificação do NPC                | 100     |
| vida     | Simples      | int  | 3       | Quantidade de vida que o NPC possui | 100     |
| tipo    | simples | varchar | 30       | Tipo de pessoa | policial       |
| vida     | Simples      | int  | 3       | Quantidade de vida que o NPC possui | 100     |



## Tarefa
#### Favores que o Jogador pode realizar para se relacionar com uma Gangue.

| Atributo    | Classe       | Tipo    | Tamanho | Descrição                                   | Exemplo               |
| ----------- | ------------ | ------- | ------- | ------------------------------------------- | --------------------- |
| idTarefa    | Determinante | int     | 1       | Identificação da área                             | 1          |
| nomeTarefa  | Determinante | varchar | 20      | Identificação da Tarefa                     | primeiras passos      |
| xp          | Simples      | int     | 3       | Pontos de experiência da tarefa | 100     |
| idNPC       | Determinante | int     | 3       | Identificação do NPC que delegou a tarefa   | 100                   |
| objetivo    | Simples      | varchar | 50      | Descreve a tarefa                           | consiga uma bicicleta |
| dificuldade | Simples      | int     | 1       | nível de dificuldade                        | 1                     |


## Veiculo
#### Objeto que o Jogador interage para se locomover rapidamente.

| Atributo          | Classe       | Tipo    | Tamanho                  | Descrição                            | Exemplo   |
| ----------------- | ------------ | ------- | ------------------------ | ------------------------------------ | --------- |
| idVeiculo         | Determinante | int     | 1                        | Identificação do Veiculo             | 1         |
| tipo              | Simples      | varchar | 20                       | Tipo do Veiculo                      | bicicleta |
| idarea            | Simples      | int     | 1                         |Área do veículo                      | 1         |
| velocidadeMax     | Simples      | int     | 10                       | Rapidez em que o Veiculo se locomove | 4         |

## Item
#### Um item utilizável pelo usuário
| Atributo     | Classe       | Tipo    | Tamanho | Descrição                           | Exemplo                   |
| ------------ | ------------ | ------- | ------- | ----------------------------------- | ------------------------- |
| idItem       | Determinante | int     | 1       | Identificação do item               | 1                         |
| usado        | Simples      | boolean | 1       | Indica se o item está usado ou não  | 1                         |
| tipo         | Simples      | varchar | 10      | Tipo do item, ex: arma, comida, etc | Bebida ForLife            |
| descricao    | Simples      | varchar | 30      | Descreve o item                     | aumenta a vida do jogador |


## Jogador_has_Tarefas
#### Qual tarefa o jogador tem
| Atributo     | Classe       | Tipo    | Tamanho | Descrição                           | Exemplo                   |
| ------------ | ------------ | ------- | ------- | ----------------------------------- | ------------------------- |
| idJogador | Determinante | int     | 1       | Identificação do Jogador         | 1       |
| nomeTarefa  | Determinante | varchar | 20      | Identificação da Tarefa                     | primeiras passos      |
| idNPC    | Determinante | int  | 3       | Identificação do NPC                | 100     |


## AreaCArea
#### Qual área conecta em qual área
| ida1    | Determinante | int     | 1       | Identificação da área principal                             | 1          |
| ia2    | Determinante | int     | 1       | Identificação da área conectada à area principal                            | 1          |


## LojaPossuiItem
#### Qual item é vendido por qual loja
| idItem       | Determinante | int     | 1       | Identificação do item               | 1                         |
| NomeLoja       | Determinante | varchar     | 50       | Identificação da loja que vende o item             | 1                         |


## Histórico de versões
|    Data    | Versão |                  Descrição                  | Autor(es) |
| :--------: | :----: | :-----------------------------------------: | :-------: |
| 27/11/2022 |  1.0   |       Criação do esqueleto do arquivo       |   Todos   |
| 27/11/2022 |  1.1   |                  Correções                  |  Letícia  |
| 27/11/2022 |  1.2   |                  Correções                  |   Todos   |
| 28/11/2022 |  1.3   |                  Correções                  |   Todos   |
| 28/11/2022 |  1.4   |                  Correções                  |   Todos   |
| 14/12/2022 |  1.5   |         Atualização para o novo DER         | Vinícius  |
| 23/12/2022 |  1.5   |      Atualização para o novo DER e MER      | Vinícius  |
| 28/12/2022 |  1.6   |        Atualização para o novo MREL         | Vinícius  |
| 15/01/2023 |  2.0   | Correções conforme observações do professor |  Letícia  |
| 16/01/2023 |  2.1   |             Ajuste das tabelas              |   Davi    |
| 16/01/2023 |  2.2   |             Correção das tabelas            |   Letícia |
| 05/02/2023 |  2.2   |             Correção das tabelas            |  Todos    |


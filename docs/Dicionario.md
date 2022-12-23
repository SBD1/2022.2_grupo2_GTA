# Dicionário de Dados

## Área
#### Local onde se encontra o personagem.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idArea | Determinante  | int | 3 | Identificação da área. |
| descrição | Simples  | varchar | 50 | Detalhamento das características da área. |


## Arma
#### Item que possui efeito nos NPCs

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipo | Simples   | varchar | 20 | Qual o modelo da arma utilizada. |
| descricao | Simples   | varchar | 50 | Detalhamento das características da arma. |
| qtdDano | Simples   | int | 10 | Quantidade de dano que a Arma causa. |
| qtdBalas | Simples   | int | 30 | Capacidade de armazenamento da arma. |


## Comida 
#### Item consumível que cura o personagem.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipo | Simples | varchar | 20 | Qual o tipo de comida a ser utilizada. |
| descricao | Simples | varchar | 50 | Detalhamento das características da comida. |
| txRecuperaçãoVida | Simples | int | 10 | Quantidade de pontos de vida a ser recuperado. |


## Droga 
#### Item consumível que afeta o personagem positiva e negativamente.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipo | Simples | varchar | 20 | Qual o tipo de droga a ser utilizada. |
| descricao | Simples | varchar | 50 | Detalhamento das características da droga. |
| vantagem | Simples   | varchar | 30 | Adiciona uma vantagem ao Jogador. |
| desvantagem | Simples   | varchar | 30 | Adiciona uma desvantagem ao Jogador. |


## Inventario
#### Onde os items do Jogador se encontram.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idPersonagem | Determinante | int | 3 | Identificação do Personagem dono do inventário. |
| capacidade | Simples | varchar | 5 | Quantidade de Items que podem ocupar o inventario. |
| dinheiro | Simples | int | 100 | valor que pode ser usado nas lojas. |


## Item
#### Objetos com que o personagem pode interagir.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idItem | Determinante | int | 3 | Identificador do Item. |
| descrição | Simples  | varchar | 20 | Descreve o item. |
| usado | Simples | int | 100 |  |
| tipo | Simples | varchar | 20 | Qual especificação do Item. |


## Jogador
#### Personagem criado pelo usuário.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idPersonagem | Determinante | int | 3 | Identificação do Jogador. |
| nome | Simples | varchar | 30 |  Nome do Jogador. |
| pontosVida | Simples | int | 10 | Pontos de vida do Jogador. |


## Loja
#### Local onde o personagem pode comprar itens.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| nome | Determinante   | varchar | 20 | Nome atribuído a Loja. |
| descrição | Simples | varchar | 20 | Descreve o propósito da loja. |
| estoque | Simples | varchar | 20 | Lista de Items que a loja possui. |


## Mapa
#### Espaço jogável contendo Áreas
|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMapa | Determinante  | int | 3 | Identificação do mapa. |
| descrição | Simples  | varchar | 50 | Detalhamento das características do mapa. |


## Membro de gangue
#### Personagens não jogável que faz parte de uma gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangue | Determinante  | int | 3 | Identificação do Membro de gangue. |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue aliada.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipoAliado | Determinante  | int | 3 | Identificação do Membro de gangue aliada. |


## Membro de gangue inimiga
#### Personagens não jogável que faz parte de uma gangue inimiga.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipoInimigo | Determinante  | int | 3 | Identificação do Membro de gangue inimiga. |


## Policial
#### Personagens não jogável que interage com Jogador e com Membro de gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idPolicial | simples  | varchar | 20 |Categoriza arma. |


## NPC
#### Personagens não jogáveis.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |   
| idNPC | Determinante  | int | 3 | Identificação do NPC.  |
| vida | Simples | int | 10 | Quantidade de vida que o NPC possui. |


## Tarefas
#### Favores que o Jogador pode realizar para se relacionar com uma Gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| nome | Determinante  | int | 3 | Identificação da Tarefa. |
| objetivo | Simples | varchar | 50 | Descreve a tarefa. |
| dificuldade | Simples | int | 5 | nível de dificuldade. |


## Veiculo
#### Objeto que o Jogador interage para se locomover rapidamente.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idVeiculo | Determinante  | int | 3 | Identificação do Veiculo. |
| tipo | Simples  | varchar | 20 | Tipo do Veiculo. |
| integridadeFísica | Simples  | int | 10 | Estado em que o carro se encontra. |
| velocidadeMax | Simples  | int | 10 | Rapidez em que o Veiculo se locomove. |


## Instância de item
#### Uma unidade de um item
|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInstaciaItem | Determinante  | int | 3 | Identificação da instância do item. |


## Instância de veículo
#### Uma unidade de um veículo
|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInstaciaVeiculo | Determinante  | int | 3 | Identificação da instância do veículo. |
| idVeiculo | Determinante  | int | 3 | Identificação do veículo. |


## Histórico de versões
|    Data    | Versão |                                       Descrição                                       |                 Autor(es)                           |  
| :--------: | :----: | :-----------------------------------------------------------------------------------: | :-------------------------------------------------: | 
| 27/11/2022 |  1.0   |                            Criação do esqueleto do arquivo                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 27/11/2022 |  1.1   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 27/11/2022 |  1.2   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 28/11/2022 |  1.3   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 28/11/2022 |  1.4   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 14/12/2022 |  1.5   |                            Atualização para o novo DER                            |  Vinícius  |
| 23/12/2022 |  1.5   |                            Atualização para o novo DER e MER                            |  Vinícius  |

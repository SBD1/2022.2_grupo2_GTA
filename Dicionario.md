# Dicionário de Dados

## Área
#### Local onde se encontra o personagem.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idArea | Determinante  | int | 3 | Identificação da Area. |
| nome | Simples  | varchar | 30 | Nome atribuído a Área. |
| descricaoArea | Simples  | varchar | 50 | Detalhamento das características da Area. |


## Jogador
#### Personagem criado pelo usuário.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idPersonagem | Determinante | int | 3 | Identificação do Jogador. |
| nome | Simples | varchar | 30 |  Nome do Jogador. |
| vida | Simples | int | 10 | Pontos de vida do Jogador. |
| dinheiro | Simples | int | 100 | valor do Jogador usado na loja. |


## Quadrado
#### Local onde se encontra o local, espaço físico onde o jogador pode se locomover.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| cordenadas | Determinante | varchar | 10 | Localização do quadrado. |
| descrição | Simples | varchar | 50 | Detalhamento das características do Quadrado. |
| clima | Simples  | varchar | 10 | Breve descrição de como se encontra o tempo. |

## Loja
#### Local onde o personagem pode comprar itens.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| nome | Determinante   | varchar | 20 | Nome atribuído a Loja. |
| estoque | Simples | varchar | 20 | Quantidade de Items que a loja possui. |
| descrição | Simples | varchar | 20 | Quais Items a Loja possui. |


## Item
#### Objetos com que o personagem pode interagir.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idItem | Determinante | int | 3 | Identificador do Item. |
| nome | Simples  | varchar | 20 | Nome atribuído ao Item. |
| tipo | Simples | varchar | 20 | Qual especificação do Item. |
| preço | Simples | int | 100 | Valor do item. |
| quantidade | Simples | int | 10 | Quantidade de Itens agrupados. |

## Arma
#### Item que possui efeito nos NPCs

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| qtdDano | Simples   | int | 10 | Quantidade de dano que a Arma causa. |
| qtdBalas | Simples   | int | 30 | Capacidade de armazenamento da arma. |
| txDisparo | Simples   | int | 10 | Cadencia ou frequência de dano causado. |
| categoria | Simples   | varchar | 10 | Tipo da Arma. |

## Utilitários
#### Items que o Jogador pode consumir.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idUtilitário | Determinante | int | 3 | Identificador do Utilitários. |
| descrição | Simples  | varchar | 50 | Descreve a função do utilitário. |

## Droga 
#### Item consumível.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| vantagem | Simples   | varchar | 30 | Adiciona uma vantagem ao Jogador. |
| desvantagem | Simples   | varchar | 30 | Adiciona uma desvantagem ao Jogador. |

## Comida 
#### Item consumível.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| txRecuperaçãoVida | Simples | int | 10 | Quantidade de pontos de vida a ser recuperado. |


## Inventario
#### Onde os items do Jogador se encontram.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInventario | Determinante | int | 3 | Identificação do Inventario. |
| capacidade | Simples | varchar | 5 | Quantidade de Items que podem ocupar o inventario. |


## Tarefas
#### Favores que o Jogador pode realizar para se relacionar com uma Gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| nome | Determinante  | int | 3 | Identificação da Tarefa. |
| objetivo | Simples | varchar | 50 | Descreve a tarefa. |
| dificuldade | Simples | int | 5 | nível de dificuldade. |
| XP | Simples | int | 10 | quantidade de pontos de experiência. |


## NPC
#### Personagens não jogáveis.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |   
| idNPC | Determinante  | int | 3 | Identificação do NPC.  |
| vida | Simples | varchar | 10 | Quantidade de vida que o NPC possui. |


## Membro de gangue
#### Personagens não jogável que faz parte de uma gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangue | Determinante  | int | 3 | Identificação do Membro de gangue. |

## Veiculo
#### Objeto que o Jogador interage para se locomover rapidamente.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idVeiculo | Determinante  | int | 3 | Identificação do Veiculo. |
| tipo | Simples  | varchar | 20 | Tipo do Veiculo. |
| integridadeFísica | Simples  | int | 10 | Estado em que o carro se encontra. |
| velocidadeMax | Simples  | int | 10 | Rapidez em que o Veiculo se locomove. |


## Policial
#### Personagens não jogável que interage com Jogador e com Membro de gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| tipoArmaEquipada | simples  | varchar | 20 |Categoriza arma. |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue aliada.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueAliada | Determinante  | int | 3 | Identificação do Membro de gangue aliada. |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue inimiga.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueInimiga | Determinante  | int | 3 | Identificação do Membro de gangue inimiga. |

## Instancia de gangue aliada 
#### Instancia uma gangue aliada 

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInstanciaAliado | Determinante  | int | 3 | Identificação da instancia de gangue aliada. |

## Instancia de gangue inimiga 
#### Instancia uma gangue inimiga 

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInstanciaInimigo | Determinante  | int | 3 | Identificação da Instancia de gangue inimiga. |


## Grupamento de Gangue Aliada
#### Conjunto de gangue aliada 
|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idnomegangue | Determinante  | varchar | 50 | Identificação da gangue aliada. |
| NroMembros | simples  | int | 3 | quantidade de integrantes da gangue aliada |


## Grupamento de Gangue Inimiga
#### Conjunto de gangue inimiga 
|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idnomegangue | Determinante  | varchar | 50 | Identificação da gangue inimiga. |
| NroMembros | simples  | int | 3 | quantidade de integrantes da gangue inimiga |

## Histórico de versões
|    Data    | Versão |                                       Descrição                                       |                 Autor(es)                           |  
| :--------: | :----: | :-----------------------------------------------------------------------------------: | :-------------------------------------------------: | 
| 27/11/2022 |  1.0   |                            Criação do esqueleto do arquivo                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 27/11/2022 |  1.1   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 27/11/2022 |  1.2   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
| 28/11/2022 |  1.3   |                            Correções                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |

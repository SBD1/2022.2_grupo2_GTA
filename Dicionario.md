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
| idJogador | Determinante | int | 3 | Identificação do Jogador. |
| nome | Simples | varchar | 30 |  Nome do Jogador. |
| vida | Simples | int | 10 | Pontos de vida do Jogador. |
| dinheiro | Simples | int | 100 | Nickname do Jogador. |


## Quadrado
#### Local onde se encontra o local, espaço físico onde o jogador pode se locomover.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idQuadrado | Determinante | int | 3 | Identificação da quadrado. |
| cordeladas | Simples | varchar | 10 | localização do quadrado. |
| descrição | Simples | varchar | 50 | Detalhamento das características do Quadrado. |
| clima | Simples  | varchar | 10 | Breve descrição de como se encontrar o tempo. |

## Loja
#### Local onde o personagem pode comprar itens.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- | 
| idLoja | Determinante | int | 3 | Identificação da Loja. |
| nome | Simples   | varchar | 20 | Nome atribuído a Loja. |
| estoque | Simples | varchar | 20 | Quantidade de Items que a loja possui. |
| descrição | Simples | varchar | 20 | Quais Items a Loja possui. |


## Itens
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
| idArma | Determinante | int | 3 | Identificador da habilidade da Arma. |
| qtdDano | Simples   | int | 10 | Quantidade de dano que a Arma causa. |
| qtdBalas | Simples   | int | 30 | Capacidade de armazenamento da arma. |
| txDisparo | Simples   | int | 10 | Cadencia ou frequência de dano causado. |
| categoria | Simples   | varchar | 10 | Tipo da Arma. |

## Utilitários
#### Items que o Jogador pode consumir.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idUtilitário | Determinante | int | 3 | Identificador do Utilitários. |
| descrição | Simples  | varchar | 50 | Tipo da Arma. |

## Droga 
#### Item consumível.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idDroga | Determinante | int | 3 | Identificador da Droga. |
| vantagem | Simples   | varchar | 30 | Adiciona uma vantagem ao Jogador. |
| desvantagem | Simples   | varchar | 30 | Adiciona uma desvantagem ao Jogador. |

## Comida 
#### Item consumível.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idComida | Determinante | int | 3 | Identificador da Droga. |
| txRecuperaçãoVida | Simples | int | 10 | Quantidade de pontos de vida a ser recuperado. |


## Inventario
#### Onde os items do Jogador se encontram.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idInventario | Determinante | int | 3 | Identificação do Inventario. |
| capacidade | Simples | varchar | 5 | Quantidade de Items que o inventario pode ocupar. |


## Tarefas
#### Favores que o Jogador pode realizar para se relacionar com uma Gangue.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idTarefa | Determinante  | int | 3 | Identificação da Tarefa. |
| descriçãoTarefa | Simples | varchar | 50 | Qual a tarefa que o Jogador tera que fazer. |


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
| idPolicial | Simples  | int | 3 | Identificação do Policial. |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue aliada.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueAliada | Simples  | int | 3 | Identificação do Membro de gangue aliada. |


## Membro de gangue aliada 
#### Personagens não jogável que faz parte de uma gangue inimiga.

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueInimiga | Simples  | int | 3 | Identificação do Membro de gangue inimiga. |

## Instancia de gangue aliada 
####

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueInimiga | Simples  | int | 3 | Identificação do Membro de gangue inimiga. |

## Instancia de gangue inimiga 
#### 

|Atributo| Classe| Tipo | Tamanho | Descrição|
| ---- | ---- | ---- | ---- | ---- |  
| idMembroDeGangueInimiga | Simples  | int | 3 | Identificação do Membro de gangue inimiga. |






## Histórico de versões
|    Data    | Versão |                                       Descrição                                       |                 Autor(es)                           |  
| :--------: | :----: | :-----------------------------------------------------------------------------------: | :-------------------------------------------------: | 
| 27/11/2022 |  1.0   |                            Criação do esqueleto do arquivo                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |
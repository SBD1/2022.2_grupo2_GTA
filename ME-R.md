# Modelo Entidade-Relacionamento(ME-R)

## Entidades
* Local
    * Área
    * Quadrado
* Instancia gangue inimiga
* Instancia gangue aliada
* Personagem 
    * NPC 
        * Policial 
        * Membro de gangue
            * Membro de gangue aliada
            * Membro de gangue inimiga 
    * Soldado 
* Veiculo
* Inventario    
* Itens
    * Arma
    * Utilitário
        * Comida 
        * Roupa     
        * Droga 



## Atributos
* Itens (<ins>idItens</ins>, nome, tipo, preço, quantidade);
* Inventario (<ins>idInventario</ins>, capacidade);
* Jogador(<ins>idPersonagem</ins>, nome, vida, dinheiro);
* Arma (<ins>idArma</ins>,qtdDano,qtdBalas, txDisparo, tipo);
* Utilitário (<ins>id</ins>, descrição);
* Comida (<ins>id</ins>, txRecuperacaoVida);
* Droga (<ins>id</ins>,vantagem ,desvantagem);
* Área (nome, descrição, tamanho);
* Quadrado(coordenadas, descrição, clima);
* Veiculo((<ins>idVeiculo</ins>, tipo, integridadeFísica, velocidadeMax);
* Instancia gangue aliada(<ins>idInstanciaAliado</ins>);
* Instancia gangue inimiga(<ins>idInstanciaInimiga</ins>);

## Relacionamentos
**Jogador *Possui* Inventario**
- O jogador pode possuir somente um inventario (1,1). Um inventario pode ser possuído por somente um jogador (1,1).

**Inventario *Armazena* Item**
- O inventario pode armazenar um ou vários itens (0,n). Um ou vários itens podem ser armazenados em um ou nenhum inventario (n,0).

**Jogador *Equipa* Item**
- O jogador pode equipar vários ou nem um item (0,n). Um ou vários itens podem ser equipados em um ou nenhum jogador (n,0).

**Tarefa *Gera* Membro de gangue aliada**
- A tarefa pode gerar um ou vários Membro de gangue aliada (1,n).  Um ou vários Membro de gangue aliada pode gerar um ou várias tarefas (1,n).

**Policial *Prende* Membro de gangue**
- O policial pode prender nenhum ou vários Membro de gangue (0,n). Nenhum ou vários Membro de gangue podem ser presos pelo policial (0,n).

**Instancia de gangue inimiga *Brigam* Instancia de gangue aliada**
- A Instancia de gangue inimiga pode brigar com nenhuma ou varis Instancia de gangue aliada (0,n). Nenhum ou várias Instancia de gangue aliada podem brigar com nenhuma ou varias Instancia de gangue inimiga (0,n).

**Gangue inimiga *Declara* Instancia de gangue inimiga**
- A Gangue inimiga pode Declarar uma ou varias Instancia de gangue inimiga (1,n). Nenhuma ou varias Instancia de gangue inimiga podem ser declaradas por Gangue inimiga (0,n).

**Gangue aliada *Declara* Instancia de gangue aliada**
- A Gangue aliada pode Declarar uma ou varias Instancia de gangue aliada (1,n). Nenhuma ou varias Instancia de gangue aliada podem ser declaradas por Gangue aliada (0,n).

**Jogador *Dirige* Veiculo**
- O jogador pode Dirigir nenhum ou um veiculo (0,1). Um ou nenhum jogador pode ser dirigido por nenhum ou um jogador (0,1).

**Jogador *Realiza* Tarefa**
- O jogador pode realizar nenhuma ou varias tarefas (0,n). Nenhuma ou varias tarefas podem ser realizadas por um ou nenhum jogador (0,n).

**Loja *Possui* Itens**
- A loja pode possuir um ou vários itens (1,n). Um ou Vários itens podem ser possuídos por uma loja (1,n).

**Loja *Se Localiza Em* Área** 
- A loja pode se localizar em uma area (1,1). Uma loja pode ser localizada em uma ou area (1,1).

**Área *Possui* Quadrado** 
-A Área possui um quadrado (1,1). Um quadrado possui uma area (1,1).

**Quadrado *Posiciona* Jogador**
- O quadrado posiciona nenhum ou vários jogadores (0,n). O jogador se posiciona em um quadrado(1,1).

**Área *Possui* NPC**
- área pode possuir nenhum ou vários NPCs (0,n). Um NPC pode ser possuído por uma área(1,1).




## Histórico de versões
|    Data    | Versão |                                       Descrição                                       |                 Autor(es)                           |  
| :--------: | :----: | :-----------------------------------------------------------------------------------: | :-------------------------------------------------: | 
| 20/11/2022 |  1.0   |                            Criação do esqueleto do arquivo                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |

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
* Instancia gangue aliada(<ins>idInstanciaAaliado</ins>);
* Instancia gangue inimiga(<ins>idInstanciaInimiga</ins>);

## Relacionamentos
**Jogador *Possui* Inventario**
- O jogador pode possuir somente um inventario (1,1). Um inventario pode ser possuído por somente um jogador(1,1).

**Inventario *Armazena* Item**
- O inventario pode armazenar um ou vários itens(1,n). Vários itens podem ser armazenados em um inventario(n,1).

**Jogador *Equipa* Item**
- 

**Tarefa *Gera* Membro de gangue aliada**

**Policial *Prende* Membro de gangue**

**Instancia de gangue inimiga *Brigam* Instancia de gangue aliada**

**Gangue inimiga *Declara* Instancia de gangue inimiga**

**Gangue aliada *Declara* Instancia de gangue aliada**

**Jogador *Dirige* Veiculo**

**Jogador *Realiza* Tarefa**

**Loja *Possui* Itens**

**Loja *Se Localiza Em* Área** 

**Área *Possui* Quadrado** 

**Quadrado *Posiciona* Jogador**




## Histórico de versões
|    Data    | Versão |                                       Descrição                                       |                 Autor(es)                           |  
| :--------: | :----: | :-----------------------------------------------------------------------------------: | :-------------------------------------------------: | 
| 20/11/2022 |  1.0   |                            Criação do esqueleto do arquivo                            |  Thiago, Lorenzo, Vinícius, Letícia, Lorenzo, Davi  |

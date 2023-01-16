|Data|Versão|Alteração|Autor| 
|----|------|---------|-----|
19/12/2022|0.1|Primeira versão do MER |Letícia|
15/01/2023|0.2| Alterações parciais segundo observações do professor | Letícia |
# Modelo Entidade-Relacionamento

## Entidades
* LOJA;
* JOGADOR;
* TAREFA
* NPC
    * MEMBRO DE GANGUE;
        * MEMBRO DE GANGUE ALIADA
        * MEMBRO DE GANGUE INIMIGA
    * POLICIAL;
* INVENTARIO;
* INSTANCIA DE ITEM;
* ITEM;
    * ARMA;
    * COMIDA;
    * DROGA;
* MAPA;
* AREA;
* INSTANCIA DE VEICULO;
* VEICULO;

## Atributos
* Loja(<ins>nome</ins>, descricaoLoja, estoque);
* Jogador(<ins>idPersonagem</ins>, nome, pontosVida);
* Tarefa(<ins>nome</ins>, dificuldade, objetivo);
* NPC(<ins>idNPC</ins>, vida);
    * Policial(</ins>idPolicial</ins>);
    * Membro de Gangue Aliada(tipo aliado);
    * Membro de Gangue Aliada(tipo inimigo);
* Inventario(<ins>idPersonagem</ins>, capacidade, dinheiro); 
* InstanciaItem(<ins>idInstanciaItem</ins>);
* Item(<ins>idItem</ins>, descricao, usado, tipo); 
    * Arma(qtDano, qtBalas).
    * Comida(txRecuperacaoVida).
    * Droga(vantagem, desvantagem).
* Mapa(<ins>idMapa</ins>, descricao);
* Area(<ins>idArea</ins>, descricao); 

## Relacionamentos
* Loja - *vende* - Item:
    * Uma Loja *vende* um ou varios Item(s) e um Item, *é vendido* por uma Loja;
    * Cardinalidade: 1 : N
* Jogador -  *dirige* -  Veículo:
    * Um Jogador *dirige* um Veículo e um Veículo *é dirigido* por um Jogador; 
    * Cardinalidade: 1 : 1.
* Jogador -  *executa* -  Tarefa:
    * Um jogador *executa* várias Tarefa(s) e uma Tarefa *é executada* por um Jogador. 
    * Cardinalidade: 0 : N.
* Jogador - *mata* - NPC:
    * Um Jogador *mata* um ou vários NPC(s) e um NPC *mata* um Jogador;
    * Cardinalidade: 1 : N.
* Jogador - *recebe* - Tarefa:
    * Um Jogador *recebe* uma Tarefa e um Tarefa *é entregada* a um Jogador;
    * Cardinalidade: N : N.  
* Membro de Gangue Aliada - *entrega* - Tarefa:
    *  Um Membro de Gangue Aliada *entrega* uma Tarefa e uma Tarefa é *entregada* por um Jogador.
* Jogador - *possui* - Inventario:
    * Um Jogador *possui* um Inventario e um Inventario *é possuido* por um Jogador;
    * Cardinalidade: 1 : 1.    
* Inventario - *possui* - Instancia de Item:
    * Um Inventario *possui* nenhuma ou várias Instancia de Item e um Inventario *é possuido* por uma Instancia de Item;
    * Cardinalidade: 1 : 1. 
* Mapa - *contem* - Area:
    * Um Mapa *tem* uma ou várias Area(s) e uma ou várias Area(s) *é constituído* por um ou vários Mapa(s);
    * Cardinalidade: N : N.
* Area - *conecta* - Area:
    * Uma Area *conecta* uma Area e uma Area *é conectada* por outra Area;
    * Cardinalidade: N : N
* Area - *contem* - NPC:
    * Uma Area *contem* zero ou vário(s) NPC(s) e um ou mais NPCs *estão ou não* em uma Area;
    * Cardinalidade: 0 : N.
* Area - *contem* - Loja:
    * Uma Area *contem* uma Loja e uma Loja *está contida* em uma Area;
    * Cardinalidade: 1 : 1.
* Area - *contem* - Veiculo:
    * Uma Area *contem* uma ou várias Instâncias de Veículo e uma Instância de Veículo *está contida* em uma Area;
    * Cardinalidade: 1 : N.
* Item - *gera* - InstanciaItem:
    * Um Item *gera* uma ou várias InstanciaItem e uma InstanciaItem *é gerada* por um Item;
    * Cardinalidade: N : 1.
* Policial - *prende* - Membro de Gangue:
    * Um ou vários policial(is) *prende* um ou vários Membro(s) de Gangue e um ou vários Membro(s) de Gangue são presos por um ou vários Policial(is).
* Membro de Gangue Inimiga - *briga* - Membro de Gangue Aliada 
    * Zero ou vários Membro(s) de Gangue Inimiga *brigam* com um ou mais Membro(s) de Gangue Aliada e zero ou vários Membro(s) de Gangue Aliada *brigam* com zero ou vários Membros de Gangue Inimiga.
    * 

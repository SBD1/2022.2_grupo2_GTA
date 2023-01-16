|Data|Versão|Alteração|Autor| 
|----|------|---------|-----|
19/12/2022|0.1|Primeira versão do MER |Letícia|
15/01/2023|0.2| Alterações segundo observações do professor | Letícia |
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
    * Um Jogador *mata* nenhum ou vários NPC(s) e um NPC *mata* nenhum ou vários Jogador(es);
    * Cardinalidade: 0 : N.
* Jogador - *recebe* - Tarefa:
    * Um Jogador *recebe* uma ou várias Tarefa(s) e um Tarefa *é entregada* a um ou vários Jogador(es);
    * Cardinalidade: N : N.  
* Membro de Gangue Aliada - *entrega* - Tarefa:
    *  Um Membro de Gangue Aliada *entrega* uma ou nehuma Tarefa e uma Tarefa é *entregada* por um Membro de Gangue Aliada.
    *  Cardinalidade: 1 : N.
* Jogador - *possui* - Inventario:
    * Um Jogador *possui* um Inventario e um Inventario *é possuido* por um Jogador;
    * Cardinalidade: 1 : 1.    
* Mapa - *contem* - Area:
    * Um Mapa *contem* uma ou várias Area(s) e uma ou várias Area(s) *é constituído* por um ou vários Mapa(s);
    * Cardinalidade: N : N.
* Area - *conecta* - Area:
    * Uma Area *conecta* uma Area e uma Area *é conectada* por outra Area;
    * Cardinalidade: N : N
* Area - *contem* - NPC:
    * Uma Area *contem* nenhum ou vário(s) NPC(s) (0,n) e um NPC *está contido* em somente uma Area (1 : 1);
    * Cardinalidade: (0 : N) e (1 : 1).
* Area - *contem* - Loja:
    * Uma Area *contem* uma Loja e uma Loja *está contida* em uma Area;
    * Cardinalidade: 1 : 1.
* Area - *contem* - Veiculo:
    * Uma Area *contem* nenhuma ou vários Veículos (o : N) e um Veículo *está contido* em uma Area (1 : 1);
    * Cardinalidade: (0 : N) e (1 : 1).
* Policial - *prende* - Membro de Gangue:
    * Um policial *prende* nenhum ou vários Membro(s) de Gangue e um Membro de Gangue é preso por nenhum ou um Polcial.
    * Cardinalidade: (0:N) e (1 : 1).
* Membro de Gangue Inimiga - *briga* - Membro de Gangue Aliada 
    * Um Membro de Gangue Inimiga *briga* com um ou vários Membro(s) de Gangue Aliada e um Membro de Gangue Aliada *briga* com um ou vários Membro(s) de Gangue Inimiga. 
    * Cardinalidade: 1 : N.

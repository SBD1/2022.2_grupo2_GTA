SELECT descricao FROM Mapa;
--> Buscar descrição do mapa

SELECT descricao FROM Area;
--> Buscar descrição do mapa

SELECT * FROM Mapa;
--> Tudo que tem na tabela mapa

SELECT * from Mapa where idMapa = 1;
--> Marca o span inicial

SELECT VIDA FROM Membro de gangue inimiga;
--> Buscar vida do  Membro de gangue inimiga;

SELECT VIDA FROM jogador;
--> Buscar vida do jogador;

SELECT xp FROM jogador;
--> Buscar XP dos jogadores;

SELECT nome FROM jogador;
--> Buscar nome do jogador;

SELECT * FROM jogador;
--> Buscar todos os atributos dos jogadores;

SELECT * FROM Tarefa;
--> Buscar todos os atributos da tarefa;

SELECT dificuldade FROM Tarefa;
--> Buscar a dificuldade da tarefa;

SELECT objetivo FROM Tarefa;
--> Buscar a objetivo da tarefa;

SELECT xp FROM Tarefa;
--> Buscar quantidade de xp que a tarefa entrega;

SELECT * FROM Loja;
--> Buscar todos os atributos da loja;

SELECT descricao FROM Loja;
--> Buscar a descricao da Loja;

SELECT estoque FROM Loja;
--> Buscar os items que a Loja possuem;

SELECT descricao FROM Loja;
--> Buscar a descricao da Loja;

SELECT * FROM Item;
--> Buscar todos os atributos do Item;

SELECT tipo FROM Item;
--> Buscar qual tipo do item;

SELECT descricao FROM Item;
--> Buscar a descricao do Item;

SELECT usado FROM Item;
--> Buscar se o item ja foi usado ou não;

-- Comida

SELECT idItem, tipo, descricao, preco, txRecuperacaoVida FROM item where nome = 'suco';
SELECT idItem, tipo, descricao, preco, txRecuperacaoVida FROM item where nome = 'tacos';
SELECT idItem,tipo,  descricao, preco, txRecuperacaoVida FROM item where nome = 'burritos';

-- Arma

SELECT idItem, tipo, descricao, preco, qtdDano, qtdBalas FROM item where nome = 'pistola AP';
SELECT idItem, tipo, descricao, preco, qtdDano, qtdBalas FROM item where nome = 'sniper heavy mk';

-- Droga

SELECT idItem, tipo, descricao, preco, vantagem, desvantagem FROM item where nome = 'droga 1';
SELECT idItem, tipo, descricao, preco, vantagem, desvantagem FROM item where nome = 'droga 2';

-- Inventario

SELECT inventario.idJogador, item.nome, item.descricao, item.preco, item.qtd_vida, item.qtd_dano
from inventario 
INNER JOIN item on inventario.id_item = item.id_item
JOIN jogador on inventario.idJogador = jogador.idJogador;

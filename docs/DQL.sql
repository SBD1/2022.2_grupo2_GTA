-- Comida

SELECT * FROM item WHERE is_equipavel= 'TRUE';
SELECT * FROM item where is_equipavel = 'FALSE';

SELECT idItem, tipo, descricao, preco, txRecuperacaoVida FROM item where nome = 'suco';
SELECT idItem, tipo, descricao, preco, txRecuperacaoVida FROM item where nome = 'tacos';
SELECT idItem,tipo,  descricao, preco, txRecuperacaoVida FROM item where nome = 'burritos';

-- Arma

SELECT * FROM item WHERE is_equipavel= 'TRUE';
SELECT * FROM item where is_equipavel = 'FALSE';

SELECT idItem, tipo, descricao, preco, qtdDano, qtdBalas FROM item where nome = 'pistola AP';
SELECT idItem, tipo, descricao, preco, qtdDano, qtdBalas FROM item where nome = 'sniper heavy mk';

-- Droga

SELECT * FROM item WHERE is_equipavel= 'TRUE';
SELECT * FROM item where is_equipavel = 'FALSE';

SELECT idItem, tipo, descricao, preco, vantagem, desvantagem FROM item where nome = 'droga 1';
SELECT idItem, tipo, descricao, preco, vantagem, desvantagem FROM item where nome = 'droga 2';

-- Inventario

SELECT inventario.idJogador, item.nome, item.descricao, item.preco, item.qtd_vida, item.qtd_dano
from inventario 
INNER JOIN item on inventario.id_item = item.id_item
JOIN jogador on inventario.idJogador = jogador.idJogador;

-- Policial

-- Membro de Gangue Aliada

-- Membro de Gangue Inimiga

-- Jogador

-- Area

-- Mapa

-- Loja

-- Tarefa

-- Veiculo

/* linguagem de manipulação de dados */

INSERT INTO area (idArea, descricao)
VALUES
(1, 'Centro da cidade'),
(2, 'Rua da sua casa'),
(3, 'Região do morro mal assombrado'),
(4, 'Base militar'),
(5, 'Hospital da cidade'),
(6, 'Aeroporto'),
(7, 'Zona comercial'),
(8, 'Morro da favela'),
(9, 'Praia');

INSERT INTO item (idItem, descricao, usado, tipo)
VALUES
(10, 'heroína -> + dano causado, - vida', 0,  'droga'),
(11, 'morfina -> + vida máxima, - dano causado', 0, 'droga'),
(12, 'maconha -> + vida máxima, ilusões', 0, 'droga'),
(13, 'ritalina -> + velocidade, - dano causado', 0, 'droga'),
(14, 'craque -> + dano causado, - vida', 0, 'droga'),
(20, 'Suco Dolly -> recupera pouca vida', 0,  'Comida'),
(21, 'Hamburguer -> recupera qtd media de vida', 0, 'Comida'),
(22, 'Frango -> recupera muita vida', 0, 'Comida'),
(23, 'fritas -> recupera muito pouca vida', 0, 'Comida'),
(24, 'pizza -> cura toda vida', 0, 'Comida'),
(30, 'AK-47 -> rifle automático', 0, 'arma'),
(31, 'P90 -> submetralhadora', 0, 'arma'),
(32, 'Bazuca -> bazuca com dano explosivo', 0, 'arma'),
(33, 'Espingarda -> arma de curto alcance e alto dano', 0, 'arma'),
(34, 'Desert Eagle -> arma pequena com alto dano', 0, 'arma'),
(35, 'Glock -> arma de pequeno porte', 0, 'arma');

INSERT INTO droga(idItem, descricao,tipo, vantagem, desvantagem)
VALUES
(10, 'heroína -> + dano causado, - vida','droga', '+25% dano', '-25HP'),
(11, 'morfina -> + vida máxima, - dano causado','droga', '+50HP maximo', '-25% dano'),
(12, 'maconha -> + vida máxima, ilusões', 'droga','+30 HP', 'Ilusões'),
(13, 'ritalina -> + velocidade, - dano causado', 'droga','+15% speed', '-15% dano'),
(14, 'craque -> + dano causado, - vida', 'droga','+25% dano', '-25HP');

INSERT INTO comida(idItem, descricao, tipo, txRecuperacaoVida)
VALUES
(20, 'Suco Dolly -> recupera pouca vida', 'Comida', 25),
(21, 'Hamburguer -> recupera qtd media de vida', 'Comida', 50),
(22, 'Frango -> recupera muita vida', 'Comida', 80),
(23, 'fritas -> recupera muito pouca vida', 'Comida', 10),
(24, 'pizza -> cura toda vida', 'Comida', 100);

INSERT INTO arma(idItem, descricao, tipo, qtdDano, qtdBalas)
VALUES
(30, 'AK-47 ', 'arma', 70, 35),
(31, 'P90 ', 'arma', 65, 50),
(32, 'Bazuca', 'arma', 95, 3),
(33, 'Espingarda ', 'arma', 75, 7),
(34, 'Desert Eagle ', 'arma', 65, 8),
(35, 'Glock', 'arma', 40, 10);


INSERT INTO npc(idNPC, vida, tipo, idArea)
VALUES
(100, 100, 'membro de gangue aliada','8'),
(101, 100, 'membro de gangue aliada','8'),
(102, 100, 'membro de gangue aliada','8'),
(200, 100, 'membro de gangue inimiga','3'),
(201, 100, 'membro de gangue inimiga','3'),
(202, 100, 'membro de gangue inimiga','3'),
(300, 100, 'policial','1'),
(301, 100, 'policial','1'),
(302, 100, 'policial','1');

INSERT INTO MembroDeGangue(idNPC, tipo)
VALUES
(100,'aliado'),
(101,'aliado'),
(102,'aliado'),
(200,'inimigo'),
(201,'inimigo'),
(202,'inimigo');

INSERT INTO MembroDeGangueAliada(idNPC, tipoAliado,vida)
VALUES
(100, 1,100),
(101, 2,100),
(102, 3,100);

INSERT INTO MembroDeGangueInimiga(idNPC, tipoInimigo,vida)
VALUES
(200, 1,100),
(201, 2,100),
(202, 3,100);

INSERT INTO policial(idNPC, vida, tipoPolicial)
VALUES
(300, 100,'basico'),
(301, 100,'choque'),
(302, 100,'elite');

INSERT INTO tarefas(nomeTarefa,dificuldade, objetivo, xp, idNPC, NumTarefa)
VALUES
('primeiros passos', 1, 'consiga uma bicicleta', 100,100,1),
('perigo à sociedade', 2, 'adquira uma arma de fogo', 200,101,2),
('limpando o caixa', 3, 'roube a loja Chill and Buy', 300, 102,3);

INSERT INTO veiculo(idVeiculo, tipo, velocidadeMax, idArea)
VALUES
(1, 'bicicleta', 4, 1),
(2, 'moto', 10, 2),
(3, 'carro', 8, 3),
(4, 'helicoptero', 9, 4),
(5, 'blindado', 5, 5),
(6, 'blindado', 5, 6),
(7, 'blindado', 5, 7);

INSERT INTO jogador(idJogador, nome, vida, xp,idVeiculo,idNPC, idArea, idtarefa)
VALUES
(1, 'Jack', 100, 0, 1, 100,1,0),
(2, 'Bob', 100, 0, 2, 100,1,0),
(3, 'Samanta', 100, 0, 3, 100,1,0),
(4, 'Spencer', 100, 0, 4, 100,1,0),
(5, 'Will', 100, 0, 5, 100,1,0),
(6, 'Drake', 100, 0, 6, 100,1,0),
(7, 'Ashley', 100, 0, 7, 100,1,0);

INSERT INTO inventario(idInventario, idJogador, dinheiro)
VALUES
(1, 1, 10),
(2, 2, 20),
(3, 3, 30),
(4, 4, 40),
(5, 5, 50),
(6, 6, 60),
(7, 7, 70);



INSERT INTO loja(nomeLoja, descricao, estoque, idItem, idArea) /* Editar */
VALUES
('Happy and Guns', 'loja de armas','AK-47', 30, 6),
('Chill and Buy', 'loja de consumíveis', 'suco Dollyy', 20, 1);

INSERT INTO mapa(idMapa, descricao)
VALUES
(1, 'Zona Norte'),
(2, 'Zona Sul'),
(3, 'Zona Leste'),
(4, 'Zona Oeste');

INSERT INTO AreaCArea(idA1, idA2)
VALUES
(1,2),
(1,4),
(2,1),
(2,5),
(2,3),
(3,2),
(3,6),
(4,1),
(4,5),
(4,7),
(5,4),
(5,6),
(5,2),
(5,8),
(6,3),
(6,5),
(6,9),
(7,4),
(7,8),
(8,4),
(8,7),
(8,9),
(9,6),
(9,8);

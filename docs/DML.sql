/* linguagem de manipulação de dados */

INSERT INTO item (idItem, nome, descricao)
VALUES
(10, 'heroína', 'Aumenta o dano causado, a troco de vida reduzida'),
(11, 'morfina', 'Aumenta a vida máxima, mas reduz o dano causado'),
(20, 'Suco Dolly', 'recupera pouca vida'),
(21, 'Hamburguer', 'recupera qtd media de vida'),
(22, 'Frango', 'recupera muita vida'),
(30, 'AK-47', 'rifle automático'),
(31, 'P90', 'submetralhadora'),
(32, 'Bazuca','bazuca com dano explosivo'),
(33, 'Espingarda', 'arma de curto alcance e alto dano'),
(34, 'Desert Eagle', 'arma de pequeno porte com alto dano'),
(35, 'Glock', 'arma de pequeno porte');

INSERT INTO droga(idItem, nome, vantagem, desvantagem)
VALUES
(10, 'heroína', '+25% dano', '-25HP'),
(11, 'morfina', '+50HP maximo', '-25% dano'),

INSERT INTO comida(idItem, nome, txRecuperacaoVida)
VALUES
(20, 'Suco Dolly', 25),
(21, 'Hamburguer', 50),
(22, 'Frango', 80);

INSERT INTO arma(idItem, nome, qtdDano, qtdBalas)
VALUES
(30, 'AK-47', 70, 35),
(31, 'P90', 65, 50),
(32, 'Bazuca', 95, 3),
(33, 'Espingarda', 75, 7),
(34, 'Desert Eagle', 65, 8),
(35, 'Glock', 40, 10);

INSERT INTO npc(idNPC, vida, tipo)
VALUES
(100, 100, 'membro de gangue aliada'),
(101, 100, 'membro de gangue aliada'),
(102, 100, 'membro de gangue aliada'),
(200, 100, 'membro de gangue inimiga'),
(201, 100, 'membro de gangue inimiga'),
(202, 100, 'membro de gangue inimiga'),
(300, 100, 'policial'),
(301, 100, 'policial'),
(302, 100, 'policial');

INSERT INTO membro_de_gangue_aliada(idNPC, tipoAliado)
VALUES
(100, 'iniciante'),
(101, 'soldado'),
(102, 'chefe');

INSERT INTO membro_de_gangue_inimiga(idNPC, tipoInimigo)
VALUES
(200, 'fraco'),
(201, 'rival'),
(202, 'comandante');

INSERT INTO policial(idNPC, tipoPolicial)
VALUES
(300, 'basico'),
(301, 'tropa de choque'),
(302, 'elite');

INSERT INTO tarefa(nome, idNPC, objetivo, dificuldade)
VALUES
('primeiros passos', 100, 'consiga uma bicicleta', 1),
('perigo à sociedade', 101, 'adquira uma arma de fogo', 2),
('limpando o caixa', 102, 'roube a loja Chill and Buy', 3);

INSERT INTO veiculo(idVeiculo, tipo, velocidadeMax)
VALUES
(1, 'bicicleta', 4),
(2, 'moto', 10),
(3, 'carro', 8),
(4, 'helicoptero', 9),
(5, 'blindado', 5);

INSERT INTO jogador(idJogador, idVeiculo, nomeTarefa, nome, vida, experiencia, idArea)
VALUES
(1, 1, 'primeiros passos', 'Jack', 100, 100, 1),
(2, 2, 'primeiros passos', 'Bob', 100, 100, 2),
(3, 3, 'primeiros passos', 'Samanta', 100, 100, 3),
(4, 4, 'primeiros passos', 'Spencer', 100, 100, 4),
(5, 5, 'primeiros passos', 'Will', 100, 100, 5),
(6, 6, 'primeiros passos', 'Drake', 100, 100, 6),
(7, 7, 'primeiros passos', 'Ashley', 100, 100, 7);

INSERT INTO inventario(idInventario, idJogador, dinheiro)
VALUES
(1, 1, 10),
(2, 2, 20),
(3, 3, 30),
(4, 4, 40),
(5, 5, 50),
(6, 6, 60),
(7, 7, 70);

INSERT INTO área (idArea, descrição) /* Editar */
VALUES
(1, 1, 'Centro da cidade'),
(2, 2, 'Rua da sua casa'),
(3, 3, 'Região do morro mal assombrado'),
(4, 4, 'Base militar'),
(5, 5, 'Hospital da cidade'),
(6, 6, 'Aeroporto'),
(7, 7, 'Zona comercial'),
(8, 8, 'Morro da favela'),
(9, 9, 'Praia');

INSERT INTO loja(nome, idArea, idItem, descricao, estoque) /* Editar */
VALUES
('Happy and Guns', 6, 1, 'loja de armas','AK-47', 'AM-1','P90','P40','ROCKET'),
('Chill and Buy', 1, 2, 'loja de consumíveis', 'suco Dollyy(cura)', 'Tang (aumenta o dano)');

INSERT INTO mapa(idMapa, descricao) /* Editar */
VALUES
(1, 'Zona Norte'),
(2, 'Zona Sul'),
(3, 'Zona Leste'),
(4, 'Zona Oeste');

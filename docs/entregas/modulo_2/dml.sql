/* linguagem de manipulação de dados */

INSERT INTO item (idItem, descricao, usado, tipo)
VALUES
(1,'Bebida ForLife',100,'aumenta a vida do jogador'),
(2,'Drink and Kill',100,'aumenta o dano da arma do jogador'),
(3,'Bebida Feliz para sempre',100,'aumenta a vida do jogador');

INSERT INTO jogador(idPersonagem, nome, pontosVida, experiencia)
VALUES
(1,'Jack', 100,100),
(2, 'Bob', 100,100),
(3, 'Samanta', 100,100),
(4, 'Spencer', 100,100),
(5, 'Will', 100,100),
(6, 'Drake', 100,100),
(7, 'Ashley', 100,100);

INSERT INTO loja(nome, descricao, estoque)
VALUES
('Happy and Guns','loja de armas','AK-47', 'AM-1','P90','P40','ROCKET'),
('Chill and Buy','loja de consumíveis', 'suco Dollyy(cura)','Tang (aumenta o dano)');


INSERT INTO área (idArea, descrição)
VALORES
( 1 , ' Zona Norte ' ),
( 2 , ' Zona Sul ' ),
( 3 , ' Zona Leste ' ),
( 4 , ' Zona Oeste ' );

INSERT INTO arma(tipo,descricao,qtdDano,qtdBalas)
VALORES
( ' AK-47 ' , ' arma de disparos automáticos ' , 70 , 35 ) ,
( ' AM-1 ' , ' arma de disparos automáticos ' , 65 , 35 ) ,
( ' P90 ' , ' arma de disparos automáticos ' , 65 , 30 ) ,
( ' ROCKET ' , ' basuca com dano explosivo ' , 95 , 3 ),
( ' espingarda ' , ' arma de únicos porém com dano acentuado ' , 75 , 7 ),
( ' desert Eagle ' , ' arma de pequeno porte e fácil de usar ' , 65 , 8 )
( ' pistola básica ' , ' arma de pequeno porte e fácil de usar ' , 40 , 10 );


INSERT INTO área (idArea, descricao)
VALUES
(1,'Zona Norte'),
(2,'Zona Sul'),
(3,'Zona Leste'),
(4,'Zona Oeste');

INSERT INTO arma(tipo,descricao,qtdDano,qtdBalas)
VALUES
('AK-47','arma de disparos automáticos',70,35),
('AM-1','arma de disparos automáticos',65,35),
('P90','arma de disparos automáticos',65,30),
('ROCKET','basuca com dano explosivo',95,3),
('espingarda','arma de únicos porém com dano acentuado',75,7),
('desert Eagle','arma de pequeno porte e fácil de usar',65,8),
('pistola básica','arma de pequeno porte e fácil de usar',40,10);

INSERT INTO comida(tipo, descricao, txRecuperacaoVida)
VALUES
('Suco Dolly','consumível feito de Dolly',35),
('Suco Tang','consumível a base de Tang',25),
('Pratao de frango','consumível',55),
('Feijuca','consumível',65),
('Refresco','consumível feito de suco de cor',20);

INSERT INTO droga(tipo, descricao, vantagem, desvantagem)
VALUES
('analgésico','Cura um pouco de vida, mas pode causar desmaios', 'recupera 5HP','5% de chance de desmaios'),
('heroína','Ganha muita energia, mas pode causar overdose', 'Corre mais rápido','-30HP'),
('morfina','Alivia dor e te deixa com visão turva', 'recupera 20HP','Te deixa confuso'),
('maconha','Extrato de planta que te faz ter uma brisa maneira', 'recupera 15HP','Te deixa confuso'),
('ritalina','Droga que aumenta concentração (supostamente)', 'Aumenta concentração','-25HP');

INSERT INTO inventario(idPersonagem,dinheiro)
VALUES
(1,'10'),
(2,'20'),
(3,'30'),
(4,'40'),
(5,'50'),
(6,'60'),
(7,'70');

INSERT INTO mapa(idMapa, descricao)
VALUES
(1,'centro da cidade'),
(2,'rua da sua casa'),
(3,'região do morro mal assombrado'),
(4,'base militar'),
(5,'Hospital da cidade');

INSERT INTO veiculo(idVeiculo, tipo, integridadeFisica, velocidadeMax)
VALUES
(1,'bicicleta',20,4),
(2,'moto',40,10),
(3,'carro',60,8),
(4,'helicoptero',70,9),
(5,'blindado',100,5);


INSERT INTO membro_de_gangue_aliada(tipoAliado)
VALUES
(100),
(101),
(102);

INSERT INTO membro_de_gangue_inimiga(tipoInimigo)
VALUES
(200),
(201),
(202);

INSERT INTO policial(idPolicial)
VALUES
(300),
(301),
(302);

INSERT INTO npc(idNPC, vida)
VALUES
(100, 100),
(101, 100),
(102, 100),
(200, 100),
(201, 100),
(202, 100),
(300, 100),
(301, 100),
(302, 100);

INSERT INTO tarefa(nome,idJogador,idNPC,objetivo,dificuldade)
VALUES
('primeiros passos',1,100,'consiga uma bicicleta',1),
('perigo à sociedade',2,101,'adquira uma arma de fogo',2),
('limpando o caixa',3,102,'roube a loja Chill and Buy',3),
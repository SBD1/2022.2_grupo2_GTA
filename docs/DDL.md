```
-- Table Veiculo

CREATE TABLE IF NOT EXISTS Veiculo (
    idVeiculo INT NOT NULL,
    tipo VARCHAR(20) NULL,
    velocidadeMax INT NULL,
  
  PRIMARY KEY (idVeiculo));
  
  
-- Table NPC

CREATE TABLE IF NOT EXISTS NPC (
  idNPC INT NOT NULL,
  vida INT NULL,
  tipo VARCHAR(30) NULL,
  
  PRIMARY KEY (idNPC));




-- Table Jogador

CREATE TABLE IF NOT EXISTS Jogador (
  idJogador INT NOT NULL,
  nome VARCHAR(30) NULL,
  vida INT NULL,
  xp INT NULL,
  idVeiculo INT NOT NULL,
  idNPC INT NOT NULL,
  
  PRIMARY KEY (idJogador),
  CONSTRAINT fk_Jogador_Veiculo1
    FOREIGN KEY (idVeiculo)
    REFERENCES Veiculo (idVeiculo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Jogador_NPC1
    FOREIGN KEY (idNPC)
    REFERENCES NPC (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Item

CREATE TABLE IF NOT EXISTS Item (
  idItem INT NOT NULL,
  descricao VARCHAR(50) NULL,
  usado INT NULL,
  tipo VARCHAR(20) NULL,
  
  PRIMARY KEY (idItem));




-- Table Loja

CREATE TABLE IF NOT EXISTS Loja (
  nomeLoja VARCHAR(20) NOT NULL,
  descricao VARCHAR(50) NULL,
  estoque VARCHAR(20) NULL,
  idItem INT NOT NULL,
  
  PRIMARY KEY (nomeLoja),
  CONSTRAINT fk_Loja_Item1
    FOREIGN KEY (idItem)
    REFERENCES Item (idItem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Arma

CREATE TABLE IF NOT EXISTS Arma (
  idItem INT NOT NULL,
  descricao VARCHAR(20) NULL,
  tipo VARCHAR(20) NULL,
  qtdDano INT NULL,
  qtdBalas INT NULL,
  
  PRIMARY KEY (idItem),
  CONSTRAINT fk_Arma_Item1
    FOREIGN KEY (idItem)
    REFERENCES Item (idItem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Comida

CREATE TABLE IF NOT EXISTS Comida (
  idItem INT NOT NULL,
  descricao VARCHAR(50) NULL,
  tipo VARCHAR(20) NULL,
  txRecuperacaoVida INT NULL,
  
  PRIMARY KEY (idItem),
  CONSTRAINT fk_Comida_Item1
    FOREIGN KEY (idItem)
    REFERENCES Item (idItem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);  



-- Table Droga

CREATE TABLE IF NOT EXISTS Droga (
  idItem INT NOT NULL,
  descricao VARCHAR(50) NULL,
  tipo VARCHAR(20) NULL,
  vantagem VARCHAR(30) NULL,
  desvantegem VARCHAR(30) NULL,
  
 PRIMARY KEY (idItem),
 CONSTRAINT fk_Droga_Item1
    FOREIGN KEY (idItem)
    REFERENCES Item (idItem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Area

CREATE TABLE IF NOT EXISTS Area (
  idArea INT NOT NULL,
  descricao VARCHAR(50) NULL,
  nomeLoja VARCHAR(20) NOT NULL,
  idVeiculo INT NOT NULL,
  idNPC INT NOT NULL,
  Area_idArea INT NOT NULL,
  Area_nomeLoja VARCHAR(20) NOT NULL,
  Area_idVeiculo INT NOT NULL,
  Area_idNPC INT NOT NULL,
  
  PRIMARY KEY (idArea, nomeLoja, idVeiculo, idNPC),
  CONSTRAINT fk_Area_Loja1
    FOREIGN KEY (nomeLoja)
    REFERENCES Loja (nomeLoja)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Area_Veiculo1
    FOREIGN KEY (idVeiculo)
    REFERENCES Veiculo (idVeiculo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Area_NPC1
    FOREIGN KEY (idNPC)
    REFERENCES NPC (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Area_Area1
    FOREIGN KEY (Area_idArea , Area_nomeLoja , Area_idVeiculo , Area_idNPC)
    REFERENCES Area (idArea , nomeLoja , idVeiculo , idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);



-- Table Inventario

CREATE TABLE IF NOT EXISTS Inventario (
  idInventario INT NOT NULL,
  dinheiro INT NULL,
  idJogador INT NOT NULL,
  
 PRIMARY KEY (idInventario, idJogador),
 CONSTRAINT fk_Inventario_Jogador
    FOREIGN KEY (idJogador)
    REFERENCES Jogador (idJogador)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Membro de gangue

CREATE TABLE IF NOT EXISTS MembroDeGangue (
  idNPC INT NOT NULL,
  tipo VARCHAR(30) NULL,
  
 PRIMARY KEY (idNPC),
 CONSTRAINT fk_MembroDegangue_NPC1
    FOREIGN KEY (idNPC)
    REFERENCES NPC (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  

-- Table Membro de gangue aliada
CREATE TABLE IF NOT EXISTS MembroDeGangueAliada (
  idNPC INT NOT NULL,
  tipoAliado INT NULL,
  vida INT NULL,
  
PRIMARY KEY (idNPC),
CONSTRAINT fk_MembroDeGangueAliada_MembroDeGangue1
    FOREIGN KEY (idNPC)
    REFERENCES MembroDeGangue(idNPC)
    ON DELETE NO ACTION);
  


-- Table Membro de gangue inimiga

CREATE TABLE IF NOT EXISTS MembroDeGangueInimiga (
  idNPC INT NOT NULL,
  tipoInimigo INT NULL,
  vida INT NULL,
  
 PRIMARY KEY (idNPC),
  CONSTRAINT fk_MembroDeGangueInimiga_MembroDeGangue1
    FOREIGN KEY (idNPC)
    REFERENCES MembroDeGangue (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  


-- Table Policial

CREATE TABLE IF NOT EXISTS Policial (
  idNPC INT NOT NULL,
  vida INT NULL,
  tipoPolicial VARCHAR(10) NULL,
  
 PRIMARY KEY (idNPC),
 CONSTRAINT fk_Policial_NPC1
    FOREIGN KEY (idNPC)
    REFERENCES NPC (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  

-- Table Tarefas

CREATE TABLE IF NOT EXISTS Tarefas (
  nomeTarefa VARCHAR(30) NOT NULL,
  dificuldade INT NULL,
  objetivo VARCHAR(50) NULL,
  xp INT NULL,
  idNPC INT NOT NULL,
  
  PRIMARY KEY (nomeTarefa,idNPC),
  CONSTRAINT fk_Tarefas_MembroDeGangueAliada1
    FOREIGN KEY (idNPC)
    REFERENCES MembroDeGangueAliada (idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  
  

-- Table Mapa

CREATE TABLE IF NOT EXISTS Mapa (
  idMapa INT NOT NULL,
  descricao VARCHAR(50) NULL,
  idArea INT NOT NULL,
  Area_idArea INT NOT NULL,
  Area_nomeLoja VARCHAR(20) NOT NULL,
  Area_idVeiculo INT NOT NULL,
  Area_idNPC INT NOT NULL,
  PRIMARY KEY (idMapa),
  CONSTRAINT fk_Mapa_Area1
    FOREIGN KEY (Area_idArea , Area_nomeLoja , Area_idVeiculo , Area_idNPC)
    REFERENCES Area (idArea , nomeLoja , idVeiculo , idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- Table Jogador_has_Tarefas
	
CREATE TABLE IF NOT EXISTS Jogador_has_Tarefas (
  Jogador_idJogador INT NOT NULL,
  Tarefas_nomeTarefa VARCHAR(30) NOT NULL,
  Tarefas_idNPC INT NOT NULL,
  PRIMARY KEY (Jogador_idJogador, Tarefas_nomeTarefa, Tarefas_idNPC),
  CONSTRAINT fk_Jogador_has_Tarefas_Jogador1
    FOREIGN KEY (Jogador_idJogador)
    REFERENCES Jogador (idJogador)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Jogador_has_Tarefas_Tarefas1
    FOREIGN KEY (Tarefas_nomeTarefa , Tarefas_idNPC)
    REFERENCES Tarefas (nomeTarefa , idNPC)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

```

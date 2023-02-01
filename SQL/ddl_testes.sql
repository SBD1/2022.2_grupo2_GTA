CREATE TABLE IF NOT EXISTS Tarefas (
    id_tarefa SERIAL,
    nome_tarefa VARCHAR(30) NOT NULL,
    PRIMARY KEY (id_tarefa)
);

CREATE TABLE IF NOT EXISTS Jogador (
    id_jogador SERIAL,
    fk_tarefa_atual INT NOT NULL,
    PRIMARY KEY (id_Jogador)
    FOREIGN KEY (fk_tarefa_atual)
        REFERENCES Tarefas(id_tarefa)
);

CREATE TABLE IF NOT EXISTS Jogador_has_tarefas (
    fk_id_jogador INT NOT NULL,
    fk_id_tarefa INT NOT NULL,

    PRIMARY KEY (fk_id_jogador, fk_id_tarefa),

    FOREIGN KEY (fk_id_jogador)
        REFERENCES Jogador(id_jogador),
    FOREIGN KEY (fk_id_tarefa)
        REFERENCES Tarefas(id_tarefa)
);

CREATE TABLE IF NOT EXISTS Tarefas_concluidas (
    id_tarefa SERIAL,
    fk_id_jogador INT NOT NULL,
    tarefa_1 INT NOT NULL DEFAULT 0,
    tarefa_2 INT NOT NULL DEFAULT 0,

    PRIMARY KEY (id_tarefa),
    FOREIGN KEY (fk_id_jogador)
        REFERENCES Jogador(id_jogador)
);
INSERT INTO Jogador DEFAULT VALUES;

INSERT INTO Tarefas(nome_tarefa)
VALUES
('primeiros passos');

INSERT INTO Jogador_has_tarefas(fk_id_jogador, fk_id_tarefa)
VALUES
(1,1);

INSERT INTO Tarefas_concluidas(fk_id_jogador, tarefa_1)
VALUES
(1,0);
--- TRIGGERS PARA TAREFA CONCLUÍDA
CREATE OR REPLACE FUNCTION check_tarefa_cumprida() RETURNS trigger AS $check_tarefa_cumprida$
BEGIN 
    if new.status = 'Concluida' and old.status <> 'Concluida' and new.id_tarefa/* ou missão*/ = (select max(id_tarefa) from tarefas where id_tarefa = new.id_tarefa) then
        UPDATE Jogador J SET experiencia = experiencia + /*qtd_exp*/ FROM tarefa t
        WHERE J.nome_save = new.id_jogador_save and J.id_jogador = new.id_nome_jogador and t.id_tarefa = new.id_tarefa;
    end if;
    return new;
END;
$check_tarefa_cumprida$ LANGUAGE plpgsql;

/* 
    - Um trigger / stored p/ cada quest
    - Alterar o jogador.has_tarefa
    - Alterar tarefa 3 para matar 10 soldados
    - 

*/


CREATE OR REPLACE FUNCTION remove_tarefa(id_jogador, id_tarefa) RETURNS BOOLEAN AS $remove_tarefa$
BEGIN
    UPDATE Tarefas_concluidas
        if id_tarefa = 'primeiros passos' then
            SET tarefa1 = 1
            WHERE Tarefas_concluidas.idJogador = id_jogador
            RETURN FOUND;
        end if;
END;
$remove_tarefa$ LANGUAGE plpgsql

CREATE TRIGGER remove_tarefa
AFTER UPDATE ON Jogador_has_Tarefas
FOR EACH ROW EXECUTE PROCEDURE remove_tarefa(jogador_idJogador, Tarefas_nomeTarefa)

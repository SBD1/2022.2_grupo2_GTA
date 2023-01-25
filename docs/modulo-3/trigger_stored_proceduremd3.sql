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



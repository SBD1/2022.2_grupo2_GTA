BEGIN;

--- TRIGGERS PARA TAREFA CONCLUÍDA
CREATE OR REPLACE FUNCTION check_tarefa_cumprida() RETURNS trigger AS $check_tarefa_cumprida$
BEGIN 
    if new.status = 'Concluida' and old.status <> 'Concluida' and new.id_tarefa  = (select max(id_tarefa) from tarefas where id_tarefa = new.id_tarefa) then
        UPDATE Jogador J SET experiencia = experiencia + FROM tarefa t
        WHERE J.nome_save = new.id_jogador_save and J.id_jogador = new.id_nome_jogador and t.id_tarefa = new.id_tarefa;
    end if;
    return new;
END;
$check_tarefa_cumprida$ LANGUAGE plpgsql;


--------------------------------------------------

-- TRIGGER PARA AS REGRAS DE NEGÓCIO DOS ATRIBUTOS DE JOGADOR

CREATE OR REPLACE FUNCTION check_atributos_jogador() RETURNS trigger AS $check_atributos_jogador$
BEGIN

    IF NEW.vida <= 0 THEN
        RAISE NOTICE 'WASTED...';

        UPDATE jogador SET vida=100 WHERE idJogador = NEW.idJogador;
    END IF;

    IF NEW.nivelProcurado > 1 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 1';

        UPDATE nivelProcurado SET nivelProcurado=1 WHERE nivelProcurado = NEW.nivelProcurado;
    END IF;
    
    IF NEW.xp >100 THEN
        RAISE NOTICE 'Você subiu de nível!';

        UPDATE xp SET xp=100 WHERE xp = NEW.xp;
    END IF;

    RETURN NULL;
END;
 $check_atributos_jogador$ LANGUAGE plpgsql;

 CREATE TRIGGER check_atributos_jogador
 AFTER UPDATE ON Jogador
 FOR EACH ROW EXECUTE PROCEDURE check_atributos_jogador();

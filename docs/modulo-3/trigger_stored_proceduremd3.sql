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

    IF NEW.nivelProcurado == 1 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 1';

        UPDATE nivelProcurado SET nivelProcurado=1 WHERE nivelProcurado = NEW.nivelProcurado;
    ELSE IF NEW.nivelProcurado == 2 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 2';

        UPDATE nivelProcurado SET nivelProcurado=3 WHERE nivelProcurado = NEW.nivelProcurado;
    ELSE IF NEW.nivelProcurado == 3 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 3';

        UPDATE nivelProcurado SET nivelProcurado=4 WHERE nivelProcurado = NEW.nivelProcurado;
    ELSE IF NEW.nivelProcurado == 4 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 4';

        UPDATE nivelProcurado SET nivelProcurado=2 WHERE nivelProcurado = NEW.nivelProcurado;
    ELSE IF NEW.nivelProcurado == 5 THEN
        RAISE NOTICE 'Você esta com nivel de procurado 5';

        UPDATE nivelProcurado SET nivelProcurado=5 WHERE nivelProcurado = NEW.nivelProcurado;        
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
 
--------------------------------------------------------------------------------------------- 
 --- TRIGGERS PARA POLICIAL
 
CREATE OR REPLACE FUNCTION check_vida_policial() RETURNS trigger AS $check_vida_policial$
BEGIN

  IF NEW.vida <= 0 THEN
    RAISE NOTICE 'Você matou o inimigo!';
    
  END IF;

  IF NEW.vida <= 0 THEN
    UPDATE Policial SET vida = 100 WHERE idNPC = NEW.idNPC;

  END IF;

  IF NEW.vida <= 0 THEN
    UPDATE Policial SET idArea = 4 WHERE idNPC = NEW.idNPC;
    UPDATE Jogador SET nivelProcurado ++1 WHERE idJogador = NEW.idNPC;
    RAISE NOTICE 'Seu nivel de proucurado é' nivelProcurado;
  END IF;
 
 IF NEW.vida <= 0 THEN
    UPDATE Jogador SET nivelProcurado ++1 WHERE idJogador = NEW.idNPC;

  END IF;
  
  IF NEW.vida <= 0 THEN
    RAISE NOTICE 'Seu nivel de proucurado é' nivelProcurado;
    
  END IF;

  

  RETURN NULL;
END;
$check_vida_policial$ LANGUAGE plpgsql;

CREATE TRIGGER check_vida_policial
AFTER UPDATE ON policial
FOR EACH ROW EXECUTE PROCEDURE check_vida_policial();

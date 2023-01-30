
CREATE OR REPLACE FUNCTION verifica_posicao() 
RETURNS trigger AS $verifica_posicao$
BEGIN
		 ---SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
		if new.idarea <> old.idarea then
			PERFORM * FROM areacarea WHERE ida1 = old.idarea and ida2 = new.idarea;
			IF not FOUND THEN
				RAISE notice 'área não existe ou não conectada';
				return old;
			END IF;
		end if;
		return new;
END;
$verifica_posicao$ LANGUAGE plpgsql;

CREATE Or Replace TRIGGER verifica_posicao
BEFORE UPDATE ON Jogador	
for each row EXECUTE PROCEDURE verifica_posicao();
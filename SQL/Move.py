import psycopg2
import os

con = psycopg2.connect(
        host='localhost',
        dbname='gta',
        user='postgres',
        password='postgres'
    )

print('Bem vindo a GTA! VC esta jogando com Jogador 1\n\n')
v = 1


while v != 0:
    with con:
        cursor = con.cursor()
        cursor.execute('SELECT idArea FROM Jogador WHERE idJogador=%s', [1])
        resultados = cursor.fetchone()
        areajogador = resultados[0]
        cursor.execute('SELECT descricao FROM area WHERE idArea=%s', [areajogador])
        areaAtual = cursor.fetchone()
        
        print('Voce esta em:')
        print(areaAtual[0])
        print('\nPara onde ir?\n')

        cursor.execute('SELECT idA2 FROM AreaCArea WHERE idA1=%s', [areajogador])
        areas = cursor.fetchall()
        var = len(areas)
        for idA2 in areas:
            cursor.execute('SELECT descricao FROM Area WHERE idArea=%s', [idA2])
            resp = cursor.fetchone()
            id = idA2[0]
            descricao = resp[0]
            print(f'{id} - {descricao}')

        novarea = input("\nDiga a area que quer ir(digite zero para sair):")
        idjogador = 1
        if novarea != '0' and novarea != 'zero':
            cursor.execute('UPDATE Jogador SET idArea = %s WHERE idJogador=%s', [novarea, idjogador])
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            v = 0
con.close()

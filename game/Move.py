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

def mostraQuest(areajogador):
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM Jogador WHERE idJogador=%s', [1])
    resultados = cursor.fetchone()
    print("E Aí " + resultados[0])
    print('Seguinte, Tenho uma missão pra ti:')
    cursor.execute('SELECT idtarefa FROM Jogador WHERE idJogador=%s', [1])
    resultados2 = cursor.fetchone()
    idt = resultados2[0]
    if idt == 0:
        cursor.execute('SELECT objetivo FROM Tarefas WHERE NumTarefa=1')
        resultados3 = cursor.fetchone()
        print(resultados3[0])
        resposta = input("aceita(sim) ou não aceita(nao)?: ")
        newid = 1
    else:
        cursor.execute('SELECT idtarefa FROM jogador WHERE idjogador=%s', [1])
        resultados4 = cursor.fetchone()
        tj = resultados4[0]
        if tj <= 3:
            cursor.execute('SELECT objetivo FROM Tarefas WHERE NumTarefa=%s',[tj + 1])
            resultados3 = cursor.fetchone()
            print(resultados3[0])
            newid = tj + 1
            resposta = input("aceita(sim) ou não aceita(nao)?: ")
    
    if resposta == 'sim':
        cursor.execute('UPDATE Jogador SET idtarefa = %s WHERE idJogador=%s', [newid, 1])
    
    cursor.close()
    

    

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
    
        if areajogador == 2:
            print('10 - Falar com Trevor')

        novarea = input("\nDiga a area que quer ir(digite zero para sair):")
        idjogador = 1
        if novarea == '10' or novarea == 'dez':
            os.system('cls' if os.name == 'nt' else 'clear')
            mostraQuest(areajogador)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            if novarea != '0' and novarea != 'zero':
                cursor.execute('UPDATE Jogador SET idArea = %s WHERE idJogador=%s', [novarea, idjogador])
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                v = 0
con.close()

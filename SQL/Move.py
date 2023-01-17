entrada = 1
import psycopg2
con = psycopg2.connect(host='localhost', database='Teste9',
user='postgres', password='Thiagoareu1')
cur = con.cursor()
sql = 'SELECT * FROM Area'
cur.execute(sql)
con.commit()
recset = cur.fetchall()

for rec in recset:
    print (rec)



cur = con.cursor()
cur.execute('SELECT idArea FROM jogador')
con.commit()
recset = cur.fetchone()

for rec in recset:
    idArea_Jogador = rec

print ('\n') 

print(idArea_Jogador," = idArea")

print ('\n')

cur = con.cursor()
cur.execute(f'SELECT norte, sul, leste, oeste FROM Area WHERE idArea = {idArea_Jogador};')
con.commit()
recset = cur.fetchall()

for rec in recset:
    print (rec)

while entrada != 0:

    novo_local = idArea_Jogador
    print ('Escolha um numero referente ao lugar para qual você deseja se locomover!')
    print ('NORTE = 1') 
    print ('SUL = 2') 
    print ('LESTE = 3') 
    print ('OESTE = 4')
    print ('SAIR = 5')
    entrada = input ('Para onde voce dexeja se locomover?') 

    if entrada == '1':
        novo_local = novo_local - 3
        cur = con.cursor()
        cur.execute(f'UPDATE Jogador SET idArea = {novo_local};')
        con.commit()
    elif entrada == '2':
        novo_local = novo_local + 3
        cur = con.cursor()
        cur.execute(f'UPDATE Jogador SET idArea = {novo_local};')
        con.commit()
    elif entrada == '3':
        novo_local = novo_local + 1
        cur = con.cursor()
        cur.execute(f'UPDATE Jogador SET idArea = {novo_local};')
        con.commit()
    elif entrada == '4':
        novo_local = novo_local - 1
        cur = con.cursor()
        cur.execute(f'UPDATE Jogador SET idArea = {novo_local};')
        con.commit()
    elif entrada == '5':
        print("Você saiu do programa!!!")
        con.close()
        exit()


    cur = con.cursor()
    cur.execute(f'UPDATE Jogador SET idArea = {novo_local};')
    con.commit()


    cur = con.cursor()
    cur.execute(f'SELECT descricao FROM Area WHERE idArea = {novo_local}')
    con.commit()
    recset = cur.fetchone()

    for rec in recset:
        print (rec)


    cur = con.cursor()
    cur.execute('SELECT idArea FROM jogador ')
    con.commit()
    recset = cur.fetchone()

    for rec in recset:
        idArea_Jogador = rec

    print ('\n') 

    print(idArea_Jogador," = idArea")



con.close()


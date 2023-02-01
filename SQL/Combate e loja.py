#encoding: utf-8
import psycopg2
action = 1
escolha = 1
nivelDeProcurado = 0
seuDano = 20 
danoInimigo = 10


con = psycopg2.connect(
        host='localhost',
        dbname='Teste6',
        user='postgres',
        password='Thiagoareu1'
    )

cursor = con.cursor()

def idAreaJogador():
    cursor = con.cursor()
    cursor.execute('SELECT idArea FROM Jogador WHERE idJogador=%s', [1])
    idAreaJogador = cursor.fetchone()
    idAreaJogador = idAreaJogador[0]
    idAreaJogador = 1
    return idAreaJogador

def areaJogador():
    cursor.execute('SELECT descricao FROM Area WHERE idArea=%s', [idAreaJogador()])
    descAreaAtual = cursor.fetchone()
    descAreaAtual = descAreaAtual[0]
    return descAreaAtual

def NPCsOnArea():
    contPolice = 0
    contNPC = 0
    contMGI = 0
    cursor = con.cursor()
    cursor.execute('SELECT * FROM NPC WHERE idArea=%s', [idAreaJogador()])
    areaAll = cursor.fetchall()
    for rec in areaAll:
        if rec[2] == 'policial':
            contPolice = contPolice + 1
        elif rec[2] == 'membro de gangue inimiga':
            contMGI = contMGI + 1
        elif rec[2] == 'NPC':
            contNPC = contNPC + 1
    return (f'Na aera atual existe {contNPC} civil(s)\n'+ f'Na aera atual existe {contMGI} Membros de gangue inimiga(s)\n'+ f'Na aera atual existe {contPolice} policial(s)') 
   
def choseGun():
    items = []
    seuDano = 20
    cursor.execute('SELECT * FROM Inventario WHERE idJogador = %s', [1])
    idItems = cursor.fetchall()
    for index in idItems:
        cursor.execute('SELECT * FROM Arma WHERE idItem = %s', [index[2]])
        items.append(cursor.fetchone())
    
    if len(items) > 0:
        print("Você possui os items:")
        for nomeItems in items:
            print(nomeItems[1])
        arma = input('Digite o nome da arma que deseja escolher:\n')
        for rec in items:
            if rec[1] == arma:
                seuDano = rec[4]
                print(seuDano,"Seu dano esta aqui")
                return seuDano
        else:
            print("Você não possui nem um item!")

def enemyOnArea():
    contPolice = 0
    contNPC = 0
    contMGI = 0
    cursor = con.cursor()
    cursor.execute('SELECT * FROM NPC WHERE idArea=%s', [idAreaJogador()])
    areaAll = cursor.fetchall()
    for rec in areaAll:
        if rec[2] == 'policial':
            contPolice = contPolice + 1
        elif rec[2] == 'membro de gangue inimiga':
            contMGI = contMGI + 1
        elif rec[2] == 'NPC':
            contNPC = contNPC + 1
    return areaAll

def checkMoney():
    cursor.execute('SELECT * FROM Jogador WHERE idJogador = 1')
    inventario = cursor.fetchone()  
    dinheiro = inventario[3]
    return dinheiro

def wanted(nivelDeProcurado):
    if nivelDeProcurado > 0 and 'policial' in  enemyOnArea()[0][2]:
        fight(action, escolha)
        return wanted(nivelDeProcurado)
    else:
        print(enemyOnArea()[0][2],'???????')
        print('Não existem mais policiais na area!')
   
def fight(action,escolha):
    if action == '1':
        seuDano = 20 
        danoInimigo = 10
        cont = 1
        NPC = ''
        inimigoArea = (enemyOnArea())

        if (inimigoArea) != []:
            print(NPCsOnArea())
            listaInimigosArea = (enemyOnArea())
            for index in listaInimigosArea:
                print(cont,"-", index[2]) 
                cont += 1
            vitima = input('Digite o nome de quem você desaja atacar:\n')
            
            for x in range(0,len(listaInimigosArea)):
                if vitima == listaInimigosArea[x][2]:
                    NPC = listaInimigosArea[x]


            print('Voce iniciou uma briga!')
            cursor.execute('SELECT vida FROM Jogador WHERE idJogador = %s', [1])
            suaVida = cursor.fetchone()
            suaVida = int(suaVida[0])

            cursor.execute(f'SELECT vida FROM NPC WHERE idNPC = {NPC[0]}')
            vidaInimigo = cursor.fetchone()
            vidaInimigo = int(vidaInimigo[0])
        else:
            return print("Você esta sozinho nessa area!")
        
        while escolha  != '0':
            print('0 - Fugir da Briga!')
            print('1 - Atacar')
            print('2 - Escolher uma arma do seu inventario:\n')
            escolha = input('Escolha a sua ação:')
            if escolha == '0':
                print('Sua vida atual:', suaVida)
                print('Vida atual do inimigo:', vidaInimigo)
            if escolha == '1':
                vidaInimigo = vidaInimigo - seuDano #Alterar para valor causado pela arma
                print('Vida atual do inimigo:', vidaInimigo)
                #cursor.execute('UPDATE NPC SET vida = %s WHERE idNPC=%s', [vidaInimigo,areaAll[0]])
                if vidaInimigo <= 0:
                    print('O voce matou o inimigo!')
                    cursor.execute('SELECT nivelProcurado FROM Jogador WHERE idJogador = %s', [1])
                    nivelDeProcurado  = cursor.fetchone()
                    nivelDeProcurado = int(nivelDeProcurado[0])
                    print(f'Seu nivel de procurado era {nivelDeProcurado} estrela(s)!')
                    nivelDeProcurado  = nivelDeProcurado + 1
                    #cursor.execute('UPDATE Joagador SET nivelProcurado = %s WHERE idJogador = %s', [[nivelProcurado,[1]]) 
                    print(f'Seu nivel de procurado é {nivelDeProcurado} estrela(s)!')
                    #cursor.execute('UPDATE NPC SET idArea = %s WHERE idNPC=%s', ['4',areaAll[0]]) #id = 4: Area militar 
                    return nivelDeProcurado
                    
                suaVida = suaVida - danoInimigo #Alterar para valor causado pela arma
                print('Sua vida atual:', suaVida)
                #cursor.execute('UPDATE Jogador SET vida = %s WHERE idJogado=%s', [vidaInimigo,areaAll[0]])
            if escolha == '2':
                seuDano = choseGun()

def store(action, escolha):
    itemsLoja = []
    nomeItemLoja = []
    cont = 1
    dinheiro = 0

    cursor.execute('SELECT nomeLoja FROM Loja WHERE idArea = %s', str(idAreaJogador()))
    nomeLoja = cursor.fetchone()
    nomeLoja = str(nomeLoja[0])
    print(f'Você entrou na loja {nomeLoja}')
    cursor.execute(f'SELECT * FROM Loja_possui_Item')
    tuplaLoja = cursor.fetchall()
    for z in range(0,len(tuplaLoja)):
        if tuplaLoja[z][0] == 'Happy and Guns':
            itemsLoja.append(tuplaLoja[z][1])

    for index in itemsLoja:
        cursor.execute(f'SELECT preco, descricao, idItem   FROM arma WHERE idItem = {index}')
        nomeItemLoja.append(cursor.fetchone())

    print(f'Bem vindo a {nomeLoja}, de uma olhada no nosso catalogo!')
    for index in nomeItemLoja:
        print(f'{cont}) Item: {index[1]} | Preço: R${index[0]},00 ' )
        cont += 1 
    
    
    dinheiro = checkMoney()
    
    print(f'Você possui: R$ {dinheiro},00')
    compra = input("Digite o que deseja comprar:")
    for index in nomeItemLoja:
        if compra == index[1]:
            if dinheiro >= index[0]:
                print(index,"Analise")
                dinheiro -= int(index[0])
                dinheiro = dinheiro + 90
                cursor.execute('UPDATE Jogador SET dinheiro = %s WHERE idJogador = %s', [dinheiro, 1])
                
                cursor.execute(f'DELETE FROM Inventario WHERE idInventario = 8') #Para não ter que fixar mudando toda vez que executar, tocar Id para auto incre
                cursor.execute(f'INSERT INTO Inventario VALUES (8, 1, {index[2]})')
                print(f'Parabens pela compra! Aqui está sua {index[0]}') 
              
            else:
                print("Você não possui dinheiro sufuciente!")



            
          


    #cursor.execute(f'SELECT preco,descricao   FROM arma WHERE idItem = {index}')
    #nomeItemLoja.append(cursor.fetchone())


   
    #cursor.execute(f'SELECT idItem FROM Loja_possui_Item WHERE nomeLoja = "Happy and Guns"')
    #itemsLoja = cursor.fetchall()



               
print('Bem vindo a GTA! VC esta jogando com Jogador 1\n\n')
print(enemyOnArea())

while action  != '0':
    with con:
        cursor = con.cursor()
        
        print('Voce esta na area:', areaJogador())


        print(f'Voce possui: R${checkMoney()},00'  )
        print(f'{NPCsOnArea()}tambem esta presente na area.')
        print('0 - Sair do jogo')
        print('1 - Brigar!')
        print('2 - Ir para outra area')
        
        areaAtual = idAreaJogador()

        if areaAtual == 1 or areaAtual == 6:
            print("3 - Entrar na loja:")
        print('---------------------')
        action = input('O que deseja fazer?\n')

        if action == '1':
            nivelDeProcurado = fight(action, escolha)
        elif action == '2':
            print("Move")
        elif action == '3':
            store(action, escolha)
           
    
con.close()
import os
import sys
import psycopg2

action = 1
escolha = 1
nivelDeProcurado = 0
global seuDano
seuDano = 20 
seuDano = int(seuDano)
danoInimigo = 10
global nomeJogadorAtual 

con = psycopg2.connect(
        host='localhost',
        dbname='GTA4',
        user='postgres',
        password='Thiagoareu1'
    )

cursor = con.cursor()

def game_menu():
    game_name()
    print("Bem vindo ao GTA!")
    print("1. Começar novo jogo")
    print("2. Continuar último jogo")
    print("3. Tutorial")
    print("4. Sair")
    choice = input("O que você gostaria de fazer? ")
    if choice == "1":
        start_new_game()
    elif choice == "2":
        load_saved_game()
    elif choice == "3":
        game_tutorial()
    elif choice=="4":
        quit_game()
    else:
        print("Opção inválida, por favor tente de novo.")
        game_menu()

def sub_menu():
    print("1. Quero voltar ao menu")
    print("2. Quero sair do jogo")
    choice = input("O que você gostaria de fazer? ")
    if choice == "1":
        game_menu()
    elif choice == "2":
        quit_game()
    else:
        print("Opção inválida, por favor tente de novo.")
        sub_menu()

def game_name():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" $$$$$$\                                     $$\       $$$$$$$$\ $$\                  $$$$$$\    $$\            $$$$$$\              $$\               ")
    print("$$  $$\                                    $$ |      \__$$  |$$ |                $$  $$\   $$ |          $$  __$$\             $$ |              ")
    print("$$ /  \| $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ |         $$ |   $$$$$$$\   $$$$$$\  $$ /  \__|$$$$$$\         $$ /  $$ |$$\   $$\ $$$$$$\    $$$$$$\  ")
    print("$$ |$$$$\ $$  $$\ \____$$\ $$  __$$\ $$  __$$ |         $$ |   $$  __$$\ $$  __$$\ $$$$\     \_$$  _|        $$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\ ")
    print("$$ |\_$$ |$$ |  \|$$$$$$$ |$$ |  $$ |$$ /  $$ |         $$ |   $$ |  $$ |$$$$$$$$ |$$  _|      $$ |          $$  $$ |$$ |  $$ |  $$ |    $$ /  $$ |")
    print("$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |         $$ |   $$ |  $$ |$$   ____|$$ |        $$ |$$\       $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |")
    print("\$$$$$$  |$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |         $$ |   $$ |  $$ |\$$$$$$$\ $$ |        \$$$$  |      $$ |  $$ |\$$$$$$  |  \$$$$  |\$$$$$$  |")
    print(" \______/ \|      \_______|\__|  \__| \_______|         \__|   \__|  \__| \_______|\__|         \____/       \__|  \__| \______/    \____/  \______/ \n")
    pass

def start_new_game():
    game_name()
    create_player()
    
    pass

def load_saved_game():
    game_name()
    #chose_player()
    pass

def game_tutorial():
    game_name()
    print("Nosso jogo foi construído com o intuito de apresentar conehcimentos desenvolvidos durante a disciplina de Sistema de Banco de Dados 1")
    print("Ao entrar no mundo de Grand Theft Auto, dirija carros, compre itens, participe de combates e ajude seus aliados em missões ao longo do jogo!\n")
    print("Para iniciar um jogo, escolha a opção 1 do menu e crie seu jogador dando a ele um nome\n")
    print("Em seguida, você será redirecionado para o mapa do jogo, onde poderá interagir com os NPCs em sua área fazendo escolhas por meio do terminal\n")
    print("Pronto para jogar?")
    sub_menu()
    

def quit_game():
    game_name()
    print("Volte sempre!\n")
    sys.exit()
    pass

def save_name(name: str) -> None: 
    global nomeJogadorAtual
    nomeJogadorAtual = name
    with con:
        with con.cursor() as cursor:
            cursor.execute('INSERT INTO Jogador ( nome, vida, dinheiro, nivelProcurado, xp, idVeiculo, idNPC, idArea, idtarefa ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s);', [(name), 100, 0, 0, 0, 1, 100, 1,0])
    
def create_player() -> str:
    print("Bem vindo ao GTA!")
    while True:
        name = input("Qual será o nome do seu personagem? ").strip()
        if len(name)>0:
            break
        else:
            print("Insira um nome válido")
    save_name(name)
    return {'nome' : name}

game_menu()


def idJogadorAtual(nomeJogadorAtual):
    cursor = con.cursor()
    cursor.execute('SELECT idJogador FROM Jogador WHERE nome =%s', [nomeJogadorAtual])
    idJogador = cursor.fetchone()
    idJogador = idJogador[0]
    return str(idJogador)


def idAreaJogador():
    cursor = con.cursor()
    cursor.execute('SELECT idArea FROM Jogador WHERE idJogador=%s', [idJogadorAtual(nomeJogadorAtual)])
    idAreaJogador = cursor.fetchone()
    idAreaJogador = idAreaJogador[0]
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
    cursor.execute('SELECT * FROM Inventario WHERE idJogador = %s', [idJogadorAtual(nomeJogadorAtual)])
    idItems = cursor.fetchall()
    for index in idItems:
        cursor.execute('SELECT * FROM Arma WHERE idItem = %s', [index[2]])
        items.append(cursor.fetchone())
    
    if len(items) > 0:
        print("---------------------")
        print("Você possui os items:")
        print("---------------------")
        for nomeItems in items:
            print(nomeItems[1])
        arma = input('Digite o nome da arma que deseja escolher:\n')
        for rec in items:
            if rec[1] == arma:
                seuDano = rec[4]
                print("-----------------------------------------------")
                print(f'Sua Arma {arma} inflinge {seuDano} ao inimigo!')
                print("-----------------------------------------------")
                return seuDano
    else:
        print("----------------------------")
        print("Você não possui nem um item!")
        print("----------------------------")

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
    cursor.execute(f'SELECT * FROM Jogador WHERE idJogador = {idJogadorAtual(nomeJogadorAtual)}')
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

            print("-----------------------")
            print('Voce iniciou uma briga!')
            print("-----------------------")
            cursor.execute('SELECT vida FROM Jogador WHERE idJogador = %s', [idJogadorAtual(nomeJogadorAtual)])
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
                print("-----------------------------------")
                print('Sua vida atual:', suaVida)
                print('Vida atual do inimigo:', vidaInimigo)
                print("-----------------------------------")
            if escolha == '1':
                vidaInimigo = vidaInimigo - seuDano #Alterar para valor causado pela arma
                print('Vida atual do inimigo:', vidaInimigo)
                #cursor.execute('UPDATE NPC SET vida = %s WHERE idNPC=%s', [vidaInimigo,areaAll[0]])
                if vidaInimigo <= 0:
                    print('O voce matou o inimigo!')
                    cursor.execute('SELECT nivelProcurado FROM Jogador WHERE idJogador = %s', [idJogadorAtual(nomeJogadorAtual)])
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
                cursor.execute('UPDATE Jogador SET dinheiro = %s WHERE idJogador = %s', [dinheiro, idJogadorAtual(nomeJogadorAtual)])
                
                cursor.execute(f'DELETE FROM Inventario WHERE idInventario = 8') #Para não ter que fixar mudando toda vez que executar, tocar Id para auto incre
                cursor.execute(f'INSERT INTO Inventario VALUES ({idJogadorAtual(nomeJogadorAtual)}, {index[2]})')
                print("-----------------------------------------------")
                print(f'Parabens pela compra! Aqui está sua {index[0]}') 
                print("-----------------------------------------------")       
            else:
                print("------------------------------------")
                print("Você não possui dinheiro sufuciente!")
                print("------------------------------------")

def mostraQuest():
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM Jogador WHERE idJogador=%s', [idJogadorAtual(nomeJogadorAtual)])
    resultados = cursor.fetchone()
    print("E Aí " + resultados[0])
    print('Seguinte, Tenho uma missão pra ti:')
    cursor.execute('SELECT idtarefa FROM Jogador WHERE idJogador=%s', [idJogadorAtual(nomeJogadorAtual)])
    resultados2 = cursor.fetchone()
    idt = resultados2[0]
    if idt == 0:
        cursor.execute('SELECT objetivo FROM Tarefas WHERE NumTarefa=1')
        resultados3 = cursor.fetchone()
        print(resultados3[0])
        resposta = input("aceita(sim) ou não aceita(nao)?: ")
        newid = 1
    else:
        cursor.execute('SELECT idtarefa FROM jogador WHERE idjogador=%s', [idJogadorAtual(nomeJogadorAtual)])
        resultados4 = cursor.fetchone()
        tj = resultados4[0]
        if tj <= 3:
            cursor.execute('SELECT objetivo FROM Tarefas WHERE NumTarefa=%s',[tj + 1])
            resultados3 = cursor.fetchone()
            print(resultados3[0])
            newid = tj + 1
            resposta = input("aceita(sim) ou não aceita(nao)?: ")
    
    if resposta == 'sim':
        cursor.execute('UPDATE Jogador SET idtarefa = %s WHERE idJogador=%s', [newid, idJogadorAtual(nomeJogadorAtual)])


print('--------------------------------------------------------------------')      
print(f'Bem vindo a GTA! VC esta jogando com Jogador {nomeJogadorAtual}\n\n')
print('--------------------------------------------------------------------')

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
            
            cursor.execute('SELECT idA2 FROM AreaCArea WHERE idA1=%s', [idAreaJogador()])
            areas = cursor.fetchall()
            var = len(areas)
            for idA2 in areas:
                cursor.execute('SELECT descricao FROM Area WHERE idArea=%s', [idA2])
                resp = cursor.fetchone()
                id = idA2[0]
                descricao = resp[0]
                print(f'{id} - {descricao}')
        
            if idAreaJogador() == 2:
                print('10 - Falar com Trevor')

            novarea = input("\nDiga a area que quer ir(digite zero para sair):")
            idjogador = idJogadorAtual(nomeJogadorAtual)
            if novarea == '10' or novarea == 'dez':
                os.system('cls' if os.name == 'nt' else 'clear')
                mostraQuest()
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                if novarea != '0' and novarea != 'zero':
                    cursor.execute('UPDATE Jogador SET idArea = %s WHERE idJogador=%s', [novarea, idjogador])
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    action = 0
        elif action == '3':
            store(action, escolha)

con.close()
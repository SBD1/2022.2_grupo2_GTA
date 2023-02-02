import os
import sys
import psycopg2

con = psycopg2.connect(
        host='localhost',
        dbname='Teste6',
        user='postgres',
        password='Thiagoareu1'
    )

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
    print(" $$$$$$\                                   $$\       $$$$$$$$\ $$\                  $$$$$$\    $$\            $$$$$$\              $$\               ")
    print("$$  $$\                                    $$ |      \__$$  |$$ |                $$  $$\   $$ |              $$  __$$\             $$ |              ")
    print("$$ /  \| $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ |         $$ |   $$$$$$$\   $$$$$$\  $$ /  \__|$$$$$$\         $$ /  $$ |$$\   $$\ $$$$$$\    $$$$$$\  ")
    print("$$ |$$$$\ $$  $$\ \____$$\ $$  __$$\ $$  __$$ |         $$ |   $$  __$$\ $$  __$$\ $$$$\     \_$$  _|        $$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\ ")
    print("$$ |\_$$ |$$ |  \|$$$$$$$ |$$ |  $$ |$$ /  $$ |         $$ |   $$ |  $$ |$$$$$$$$ |$$  _|      $$ |          $$  $$ |$$ |  $$ |  $$ |    $$ /  $$ |")
    print("$$ |  $$ |$$ |   $$  __$$ |$$ |  $$ |$$ |  $$ |         $$ |   $$ |  $$ |$$   ____|$$ |      $$ |$$\         $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |")
    print("\$$$$$$  |$$ |   \$$$$$$$ |$$ |  $$ |\$$$$$$$ |         $$ |   $$ |  $$ |\$$$$$$$\ $$ |      \$$$$  |        $$ |  $$ |\$$$$$$  |  \$$$$  |\$$$$$$  |")
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
    cursor = con.cursor()
    cursor.execute('INSERT INTO Jogador (idJogador, nome, vida, xp, idVeiculo, idNPC, idArea ) VALUES (%s, %s, %s, %s, %s, %s, %s);', [7, name, 100, 0, 1, 300, 1])

    
def create_player() -> str:
    print("Bem vindo ao GTA!")
    while True:
        name = input("Qual será o nome do seu personagem? ").strip()
        if len(name)>0:
            break
        else:
            print("Insira um nome válido")
    save_name(name)
    #se tiver tempo, implementar função que verifica se existe nome igual
    return {'nome' : name}



game_menu()

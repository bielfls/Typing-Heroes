from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
#pegando as classes dos outros arquivos
from menuClass import Menu
from selectionClass import Selection
from gameClass import Game

#fazendo a janela
janela = Window(1152, 648)
janela.set_title("Typing Heroes")

#variavel que indicara qual tela o jogador está (começará no menu)
tela = "menu"

#teclado e cursor
cursor = janela.get_mouse()
teclado = janela.get_keyboard()

#variavel que fará o jogo fechar quando for False
janela.jogo_ativo = True

#definindo o menu usando a classe Menu criada no arquivo "menuClass"
menu = Menu()
#definindo a selecao de personagem usando a classe Selection criada no arquivo selectionClass
selection = Selection()
#definindo a tela do jogo usando a classe Game criada em "gameClass.py"
game = Game()
partida_inicia = False

#loop principal do jogo
while janela.jogo_ativo:

    match tela:

        #menu
        case "menu":
            #funcao de desenhar o menu na janela
            menu.menu_draw(janela)
            #torna funcional o botao sair
            if cursor.is_over_object(menu.botao_sair) and cursor.is_button_pressed(1):
                janela.jogo_ativo = False
            if cursor.is_over_object(menu.botao_jogar) and cursor.is_button_pressed(1):
                tela = "selection"


        #seleção de personagem
        case "selection":
            #volta pro menu se apertar esc
            if teclado.key_pressed("ESC"):
                tela = "menu"
                selection.reinicia_variaveis()
            #funçoes q fazem tudo
            selection.selection_draw(janela)
            selection.select_mecanica(janela, cursor)
            #quando os dois jogadores escolhem, a partida começa (esta menu por enquanto pq ainda n tem jogo)
            if selection.p1_escolheu and selection.p2_escolheu and cursor.is_over_object(selection.botao_jogar) and cursor.is_button_pressed(1):
                selection.reinicia_variaveis()
                partida_inicia = True
                tela = "game"


        #partida
        case "game":
            if not game.pause:
                if partida_inicia:
                    game.define_personagens(selection.p1_escolha, selection.p2_escolha)
                    partida_inicia = False
                game.animação_players(teclado) #AQUI ENTRARÁ A VARIAVEL QUE INDICA SE O PLAYER ACERTOU OU NAO A SETA
                game.game_draw(janela, selection.p1_escolha, selection.p2_escolha)
                if teclado.key_pressed("ESC"):
                    game.pause = True
            else:
                game.game_pause(janela)
                if cursor.is_over_object(game.botao_continuar) and cursor.is_button_pressed(1):
                    game.pause = False
                if cursor.is_over_object(game.botao_voltar) and cursor.is_button_pressed(1):
                    tela = "selection"
                    game.pause = False

    janela.update()
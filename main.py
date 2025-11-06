from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
#pegando as classes dos outros arquivos
from menuClass import Menu
from selectionClass import Selection

#fazendo a janela
janela = Window(1152, 648)
janela.set_title("Typing Heroes")

#variavel que indicara qual tela o jogador está (começará no menu)
tela = "menu"

#teclado e cursor
cursor = janela.get_mouse()
taclado = janela.get_keyboard()

#variavel que fará o jogo fechar quando for False
janela.jogo_ativo = True

#definindo o menu usando a classe Menu criada no arquivo "menuClass"
menu = Menu()
#definindo a selecao de personagem usando a classe Selection criada no arquivo selectionClass
selection = Selection()

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
            selection.selection_draw(janela)
            selection.select_mecanica(janela, cursor)
            #quando os dois jogadores escolhem, a partida começa (esta menu por enquanto pq ainda n tem jogo)
            if selection.p1_escolheu and selection.p2_escolheu:
                #selection.p1_escolheu = False
                #selection.p2_escolheu = False
                #fazer mudança de tela pra partida aqui
                pass

    janela.update()
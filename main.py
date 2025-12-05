from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *
#pegando as classes dos outros arquivos
from menuClass import Menu
from selectionClass import Selection
from gameClass import Game
from setaClass import MecanicaSetas
from gameoverClass import Gameover
import os

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
selection = Selection(janela)
#definindo a tela do jogo usando a classe Game criada em "gameClass.py"
game = Game()
entrou_game = False
partida_inicia = False
#definindo a mecanica de setas da classe criada em setaClass
mecanica_setas = MecanicaSetas(janela)
#definindo tela de gameover com a classe criada em gameoverClass
gameover = Gameover()
entrou_menu = True
entrou_selection = True
entrou_gameover = True
entrou_game_music = True
entrou_pause = True

#sons
assets_path = os.path.join(os.path.dirname(__file__), "Assets")
music_menu = Sound(os.path.join(assets_path, "menu.ogg"))
music_menu.set_volume(20)
music_menu.set_repeat(True)

music_selection = Sound(os.path.join(assets_path, "select.ogg"))
music_selection.set_volume(20)
music_selection.set_repeat(True)

music_battle = Sound(os.path.join(assets_path, "battle.wav"))
music_battle.set_volume(20)
music_battle.set_repeat(True)

sound_vitoria = Sound(os.path.join(assets_path, "vitoria.mp3"))
sound_vitoria.set_volume(20)
sound_vitoria.set_repeat(False)

#loop principal do jogo
while janela.jogo_ativo:

    match tela:

        #menu
        case "menu":
            if entrou_menu:
                music_menu.play()
                entrou_menu = False
            #funcao de desenhar o menu na janela
            menu.menu_draw(janela)
            #torna funcional o botao sair
            if cursor.is_over_object(menu.botao_sair) and cursor.is_button_pressed(1):
                janela.jogo_ativo = False
            if cursor.is_over_object(menu.botao_jogar) and cursor.is_button_pressed(1):
                tela = "selection"
                entrou_menu = True
                music_menu.stop()


        #seleção de personagem
        case "selection":
            if entrou_selection:
                music_selection.play()
                entrou_selection = False
            mecanica_setas.reinicia_variaveis(janela)
            #volta pro menu se apertar esc
            if teclado.key_pressed("ESC"):
                tela = "menu"
                entrou_selection = True
                music_selection.stop()
                selection.reinicia_variaveis()
            #funçoes q fazem tudo
            selection.selection_draw(janela)
            selection.select_mecanica(janela, cursor)
            #quando os dois jogadores escolhem, a partida começa (esta menu por enquanto pq ainda n tem jogo)
            if selection.p1_escolheu and selection.p2_escolheu and cursor.is_over_object(selection.botao_jogar) and cursor.is_button_pressed(1):
                selection.reinicia_variaveis()
                tela = "game"
                entrou_selection = True
                music_selection.stop()
                partida_inicia = False
                entrou_game = True


        #partida
        case "game":
                if entrou_game_music:
                    music_battle.play()
                    entrou_game_music = False
                if not game.pause:
                    if entrou_game:
                        game.define_personagens(selection.p1_escolha, selection.p2_escolha)
                        entrou_game = False
                    
                    game.animação_players(teclado) #AQUI ENTRARÁ A VARIAVEL QUE INDICA SE O PLAYER ACERTOU OU NAO A SETA
                    game.game_draw(janela, selection.p1_escolha, selection.p2_escolha)
                    if not partida_inicia:
                        game.contagem(janela)
                        if game.timer >= 3.5:
                            game.timer = 0
                            partida_inicia = True
                    else:
                        mecanica_setas.mecanica(janela, teclado)
                        if teclado.key_pressed("ESC"):
                            game.pause = True
                        #ve qual dos players venceu e muda pra tela de gameover
                        if mecanica_setas.lifebar_verde.y==mecanica_setas.lifebar_verde2.y==janela.height:
                            tela = "gameover"
                            music_battle.stop()
                            entrou_game_music = True
                            mecanica_setas.reinicia_variaveis(janela)
                            gameover.vencedor = 0
                        elif mecanica_setas.lifebar_verde.y>=janela.height:
                            tela = "gameover"
                            music_battle.stop()
                            entrou_game_music = True
                            mecanica_setas.reinicia_variaveis(janela)
                            gameover.vencedor = 2
                        elif mecanica_setas.lifebar_verde2.y>=janela.height:
                            tela = "gameover"
                            music_battle.stop()
                            entrou_game_music = True
                            mecanica_setas.reinicia_variaveis(janela)
                            gameover.vencedor = 1
                else:
                    game.game_pause(janela)
                    if entrou_pause:
                        music_battle.pause()
                        entrou_pause = False
                    if cursor.is_over_object(game.botao_continuar) and cursor.is_button_pressed(1):
                        music_battle.unpause()
                        game.pause = False
                        entrou_pause = True
                    if cursor.is_over_object(game.botao_voltar) and cursor.is_button_pressed(1):
                        tela = "selection"
                        music_battle.stop()
                        game.pause = False
                        entrou_pause = True
                        entrou_game_music = True
            
        #gameover
        case "gameover":
            if entrou_gameover:
                sound_vitoria.play()
                entrou_gameover = False
            gameover.desenha_gameover(janela)
            if cursor.is_over_object(gameover.botao_restart) and cursor.is_button_pressed(1):
                tela = "game"
                entrou_gameover = True
                sound_vitoria.stop()
                partida_inicia = False
            if cursor.is_over_object(gameover.botao_sair) and cursor.is_button_pressed(1):
                tela = "menu"
                entrou_gameover = True
                sound_vitoria.stop()

    janela.update()
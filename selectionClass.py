from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os
from knightP1Class import KnightP1
from knightP2Class import KnightP2
from samuraiP1Class import SamuraiP1
from samuraiP2Class import SamuraiP2

class Selection:
    def __init__(self):
        #acessando a pasta Assets e pegando as imagens
        self.knight_p1 = KnightP1()
        self.knight_p2 = KnightP2()
        self.samurai_p1 = SamuraiP1()
        self.samurai_p2 = SamuraiP2()
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.fundo = Sprite(os.path.join(assets_path, "selection_fundo.png"))
        self.knight_select_p1 = Sprite(os.path.join(assets_path, "knight_select.png"))
        self.knight_select_p2 = Sprite(os.path.join(assets_path, "knight_select.png"))
        self.samurai_select_p1 = Sprite(os.path.join(assets_path, "samurai_select.png"))
        self.samurai_select_p2 = Sprite(os.path.join(assets_path, "samurai_select.png"))

        #variaveis de escolha de personagem
        self.p1_escolheu = False
        self.p2_escolheu = False

    #função pra desenhar os blocos principais da tela de seleção
    def selection_draw(self, janela):
        self.fundo.set_position(0,0)
        self.knight_select_p1.set_position(15,15)
        self.knight_select_p2.set_position(janela.width - self.knight_select_p2.width - 15, 15)
        self.samurai_select_p1.set_position(15, 15*2 + self.knight_select_p2.height)
        self.samurai_select_p2.set_position(janela.width - self.knight_select_p2.width - 15, 15*2 + self.knight_select_p2.height)

        self.fundo.draw()
        self.knight_select_p1.draw()
        self.knight_select_p2.draw()
        self.samurai_select_p1.draw()
        self.samurai_select_p2.draw()
        
    
    def select_mecanica(self, janela, cursor):
        #quando o cursor passe pelos perfis, a imagem do personagem aparece
        if cursor.is_over_object(self.knight_select_p1):
                self.knight_p1.png.set_position(janela.width/2 - self.knight_p1.png.width - 50, janela.height - self.knight_p1.png.height)
                self.knight_p1.png.draw()
        if cursor.is_over_object(self.knight_select_p2):
                self.knight_p2.png.set_position(janela.width/2 + 50, janela.height - self.knight_p2.png.height)
                self.knight_p2.png.draw()

        if cursor.is_over_object(self.samurai_select_p1):
                self.samurai_p1.png.set_position(janela.width/2 - self.samurai_p1.png.width - 50, janela.height - self.samurai_p1.png.height)
                self.samurai_p1.png.draw()
        if cursor.is_over_object(self.samurai_select_p2):
                self.samurai_p2.png.set_position(janela.width/2 + 50, janela.height - self.samurai_p2.png.height)
                self.samurai_p2.png.draw()

        #quando o player escolhe o personagem clicando
        if cursor.is_over_object(self.knight_select_p1) and cursor.is_button_pressed(1):
              self.p1_escolheu = True
        if cursor.is_over_object(self.knight_select_p2) and cursor.is_button_pressed(1):
              self.p2_escolheu = True
        if cursor.is_over_object(self.samurai_select_p1) and cursor.is_button_pressed(1):
              self.p1_escolheu = True
        if cursor.is_over_object(self.samurai_select_p2) and cursor.is_button_pressed(1):
              self.p2_escolheu = True

              
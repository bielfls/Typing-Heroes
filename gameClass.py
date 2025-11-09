from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os
from knightP1Class import KnightP1
from knightP2Class import KnightP2
from samuraiP1Class import SamuraiP1
from samuraiP2Class import SamuraiP2

#classe da gameplay
class Game:
    def __init__(self):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.fundo = Sprite(os.path.join(assets_path, "fundo_oriental.png"))
        #mais tarde esses serao os personagens dos players
        self.p1 = ''
        self.p2 = ''
        self.pause = False
        self.fundo_pause = Sprite(os.path.join(assets_path, "fundo_pause.png"))
        self.botao_continuar = Sprite(os.path.join(assets_path, "botao_continuar.png"))
        self.botao_voltar = Sprite(os.path.join(assets_path, "botao_voltar.png"))
        
    
    def define_personagens(self, p1_escolha, p2_escolha):
         #definindo o personagem dos players
         if p1_escolha == "SAMURAI":
                self.p1 = SamuraiP1()
         elif p1_escolha == "KNIGHT":
                self.p1 = KnightP1()
            
         if p2_escolha == "SAMURAI":
                self.p2 = SamuraiP2()
         elif p2_escolha == "KNIGHT":
                self.p2 = KnightP2()

    def animação_players(self, teclado):
         #mecanica do player 1
         if teclado.key_pressed("Q"):
              self.p1.ataque_1()
         if teclado.key_pressed("W"):
              self.p1.ataque_2()
         if teclado.key_pressed("E"):
              self.p1.ataque_3()
         if teclado.key_pressed("R"):
              self.p1.ataque_1()

         #mecanica do player 2
         if teclado.key_pressed("U"):
              self.p2.ataque_1()
         if teclado.key_pressed("I"):
              self.p2.ataque_2()
         if teclado.key_pressed("O"):
              self.p2.ataque_3()
         if teclado.key_pressed("P"):
              self.p2.ataque_1()

    def game_draw(self, janela : Window, p1_escolha, p2_escolha):
            self.fundo.set_position(0,0)
            self.fundo.draw()

            self.p1.anim_atual.set_position(225, janela.height - self.p1.anim_atual.height)
            self.p1.atualiza_anim()
            self.p1.desenha()

            self.p2.anim_atual.set_position(janela.width - 225 - self.p2.anim_atual.width, janela.height - self.p2.anim_atual.height)
            self.p2.atualiza_anim()
            self.p2.desenha()
     
    def game_pause(self, janela : Window):
          self.fundo_pause.set_position(0,0)
          self.botao_continuar.set_position(janela.width/2-self.botao_continuar.width/2,50)
          self.botao_voltar.set_position(janela.width/2-self.botao_voltar.width/2,50+50+self.botao_continuar.height)

          self.fundo_pause.draw()
          self.botao_continuar.draw()
          self.botao_voltar.draw()
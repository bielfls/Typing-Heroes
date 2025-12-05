from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os
from knightP1Class import KnightP1
from knightP2Class import KnightP2
from samuraiP1Class import SamuraiP1
from samuraiP2Class import SamuraiP2
from esqueletoP1Class import EsqueletoP1
from esqueletoP2Class import EsqueletoP2
from loboP1Class import LoboP1
from loboP2Class import LoboP2
from PPlay.sound import *

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
        self.um = Sprite(os.path.join(assets_path, "UM.png"))
        self.dois = Sprite(os.path.join(assets_path, "DOIS.png"))
        self.tres = Sprite(os.path.join(assets_path, "TRES.png"))
        self.lutem = Sprite(os.path.join(assets_path, "LUTEM.png"))
        self.timer = 0
        self.blip = Sound(os.path.join(assets_path, "Blip.wav"))
        self.blip.set_volume(90)
        self.FIGHT = Sound(os.path.join(assets_path, "FIGHT!.mp3"))
        self.FIGHT.set_volume(90)
        self.passo_som = 0
        
    
    def define_personagens(self, p1_escolha, p2_escolha):
         #definindo o personagem dos players
         if p1_escolha == "SAMURAI":
                self.p1 = SamuraiP1()
         elif p1_escolha == "KNIGHT":
                self.p1 = KnightP1()
         elif p1_escolha == "ESQUELETO":
                self.p1 = EsqueletoP1()
         elif p1_escolha == "LOBO":
                self.p1 = LoboP1()
                
         if p2_escolha == "SAMURAI":
                self.p2 = SamuraiP2()
         elif p2_escolha == "KNIGHT":
                self.p2 = KnightP2()
         elif p2_escolha == "ESQUELETO":
                self.p2 = EsqueletoP2()
         elif p2_escolha == "LOBO":
                self.p2 = LoboP2()

          

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
            if p1_escolha == "KNIGHT" or p1_escolha == "SAMURAI":
               self.p1.anim_atual.set_position(225, janela.height - self.p1.anim_atual.height)
            else:
               self.p1.anim_atual.set_position(50, janela.height - self.p1.anim_atual.height)

            if p2_escolha == "KNIGHT" or p2_escolha == "SAMURAI":
               self.p2.anim_atual.set_position(janela.width - 225 - self.p2.anim_atual.width, janela.height - self.p2.anim_atual.height)
            else:
               self.p2.anim_atual.set_position(janela.width - 50 - self.p2.anim_atual.width, janela.height - self.p2.anim_atual.height)

            self.p1.atualiza_anim()
            self.p1.desenha()
            self.p2.atualiza_anim()
            self.p2.desenha()
     
    def game_pause(self, janela : Window):
          self.fundo_pause.set_position(0,0)
          self.botao_continuar.set_position(janela.width/2-self.botao_continuar.width/2,50)
          self.botao_voltar.set_position(janela.width/2-self.botao_voltar.width/2,50+50+self.botao_continuar.height)

          self.fundo_pause.draw()
          self.botao_continuar.draw()
          self.botao_voltar.draw()

    def contagem(self, janela:Window):
          self.timer += janela.delta_time()
          if self.timer <= 1:
                if self.passo_som == 0:
                     self.blip.play()
                     self.passo_som = 1
                self.um.set_position(janela.width/2-self.um.width/2, janela.height/2-self.um.height/2)
                self.um.draw()
          elif self.timer <= 2:
                if self.passo_som == 1:
                     self.blip.stop()
                     self.blip.play()
                     self.passo_som = 2
                self.dois.set_position(janela.width/2-self.um.width/2, janela.height/2-self.um.height/2)
                self.dois.draw()
          elif self.timer <= 3:
                if self.passo_som == 2:
                     self.blip.stop()
                     self.blip.play()
                     self.passo_som = 3
                self.tres.set_position(janela.width/2-self.tres.width/2, janela.height/2-self.tres.height/2)
                self.tres.draw()
          elif self.timer <= 4:
                if self.passo_som == 3:
                     self.blip.stop()
                     self.FIGHT.play()
                     self.passo_som = 0
                self.lutem.set_position(janela.width/2-self.lutem.width/2, janela.height/2-self.lutem.height/2)
                self.lutem.draw()
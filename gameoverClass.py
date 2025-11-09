from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os
from knightP1Class import KnightP1
from knightP2Class import KnightP2
from samuraiP1Class import SamuraiP1
from samuraiP2Class import SamuraiP2

class Gameover:
    def __init__(self):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.botao_sair=Sprite(os.path.join(assets_path, "SAIR.png"))
        self.botao_restart=Sprite(os.path.join(assets_path, "RESTART.png"))
        self.letreiro_gameover=Sprite(os.path.join(assets_path, "GAMEOVER.png"))
        self.fundo = Sprite(os.path.join(assets_path, "fundo_pause.png"))
        self.vencedor = ''

    def desenha_gameover(self,janela:Window):
        self.fundo.set_position(0,0)
        self.letreiro_gameover.set_position(janela.width/2-self.letreiro_gameover.width/2,0)
        self.botao_restart.set_position(15, janela.height-self.botao_restart.height -15)
        self.botao_sair.set_position(janela.width-self.botao_sair.width-15, janela.height-self.botao_sair.height -15)

        self.fundo.draw()
        self.letreiro_gameover.draw()
        self.botao_restart.draw()
        self.botao_sair.draw()

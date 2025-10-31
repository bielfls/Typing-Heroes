from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os

class Menu:
    def __init__(self):
        #acessando a pasta Assets e pegando as imagens
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.fundo = Sprite(os.path.join(assets_path, "menufundo.png"))
        self.logo = Sprite(os.path.join(assets_path, "logo.png"))
        self.botao_sair = Sprite(os.path.join(assets_path, "botão_sair.png"))
        self.botao_jogar = Sprite(os.path.join(assets_path, "botão_jogar.png"))

    #desenha o menu
    def menu_draw(self, janela):
        self.fundo.set_position(0,0)
        self.logo.set_position(janela.width/2 - self.logo.width/2, 100)
        self.botao_sair.set_position(janela.width/2 + 50, 500)
        self.botao_jogar.set_position(janela.width/2 - self.botao_jogar.width - 50, 500)

        self.fundo.draw()
        self.botao_jogar.draw()
        self.botao_sair.draw()
        self.logo.draw()

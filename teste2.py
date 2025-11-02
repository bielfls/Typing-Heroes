from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os
from knightP1Class import KnightP1

janela = Window(1080, 800)

#testando animações da classe q eu fiz
knight = KnightP1()
knight.anim_atual.set_position(180,-120)

while True:
    janela.set_background_color((25,25,25))

    knight.atualiza_anim()
    knight.desenha()
    janela.update()
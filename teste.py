from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os

janela = Window(800, 600)

#testando animações
assets_path = os.path.join(os.path.dirname(__file__), "Assets")
knight_path = os.path.join(assets_path, "Knight")
knight_atack_1 = Sprite(os.path.join(knight_path, "Attack 1.png"), 5)
knight_atack_1.image = pygame.transform.flip(knight_atack_1.image, True, False)
knight_atack_1.set_position(180,-120)
knight_atack_1.set_sequence(0, 5, loop=True)
knight_atack_1.set_total_duration(500)

while True:
    janela.set_background_color((25,25,25))

    knight_atack_1.update()
    knight_atack_1.draw()

    janela.update()
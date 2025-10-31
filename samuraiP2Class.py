from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os

class SamuraiP2:
    def __init__(self):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        samurai_path = os.path.join(assets_path, "Samurai")
        self.png = Sprite(os.path.join(samurai_path, "samurai.png"))
        #flipando o sprite
        self.png.image = pygame.transform.flip(self.png.image, True, False)
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os

class KnightP1:
    def __init__(self):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        knight_path = os.path.join(assets_path, "Knight")
        self.png = Sprite(os.path.join(knight_path, "knight.png"))
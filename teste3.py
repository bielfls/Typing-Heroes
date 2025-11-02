# Importa as bibliotecas necessárias da PPlay
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
import os

class Player:
    def __init__(self, x, y):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        knight_path = os.path.join(assets_path, "Knight")
        self.idle_anim = Sprite(os.path.join(knight_path, "Idle.png"), 4)
        self.attack_anim = Sprite(os.path.join(knight_path, "Attack 3.png"), 4)

        # Define a velocidade de cada animação (em milissegundos para o loop completo)
        self.idle_anim.set_total_duration(1000)  # 1 segundo para a animação idle
        self.attack_anim.set_total_duration(500) # 0.5 segundos para o ataque (mais rápido)

        # --- 2. Definir Estado Inicial ---
        self.state = "IDLE"  # Pode ser "IDLE" ou "ATTACKING"
        self.current_animation = self.idle_anim

        # --- 3. Posição ---
        # Define a posição inicial. Ambas animações devem estar no mesmo lugar.
        self.current_animation.set_position(x, y)
        self.attack_anim.set_position(x, y) # Garante que a de ataque comece no mesmo lugar

        # --- 4. Controle ---
        self.keyboard = Window.get_keyboard()

    def attack(self):
        """Muda o estado para 'ATACANDO', mas só se estiver 'PARADO'."""
        if self.state == "IDLE":
            self.state = "ATTACKING"
            
            # Troca a animação ativa
            self.current_animation = self.attack_anim
            
            # IMPORTANTE: Reinicia a animação de ataque para o frame 0
            self.current_animation.set_curr_frame(0)

    def updatee(self):
        """Atualiza a lógica do jogador a cada frame."""
        
        # --- 1. Checar Inputs ---
        # Se 'W' for pressionado, tenta iniciar o ataque
        if self.keyboard.key_pressed("W"):
            self.attack()

        # --- 2. Lógica de Animação e Estado ---
        
        # Armazena o frame ATUAL antes de chamar o update()
        # Isso é crucial para detectar o fim da animação
        prev_frame = self.current_animation.get_curr_frame()

        # Atualiza a animação (isso pode avançar o frame)
        self.current_animation.update()
        
        # --- 3. Checar Transição de Estado (Fim do Ataque) ---
        if self.state == "ATTACKING":
            # Pega o número total de frames (ex: 4)
            total_frames = self.current_animation.total_frames
            # O índice do último frame é (total_frames - 1), ou seja, 3
            last_frame_index = total_frames - 1
            
            # Pega o frame DEPOIS do update()
            current_frame = self.current_animation.get_curr_frame()

            # CONDIÇÃO: Se o frame ANTERIOR era o último (3) E
            # o frame ATUAL é o primeiro (0), significa que a animação acabou de "loopar".
            if prev_frame == last_frame_index and current_frame == 0:
                # O ataque terminou! Voltar para o estado IDLE.
                self.state = "IDLE"
                self.current_animation = self.idle_anim
                # A posição já está correta, pois ambas as sprites
                # foram inicializadas na mesma posição.

    def draww(self):
        """Desenha o jogador na tela."""
        # Desenha qualquer que seja a animação ativa no momento
        self.current_animation.draw()

# --- Configuração do Jogo (Loop Principal) ---

# 1. Inicializa a janela
largura, altura = 800, 600
janela = Window(largura, altura)
janela.set_title("Animação de Ataque e Idle")

# 2. Cria o jogador
# Coloca ele mais ou menos no centro da tela
assets_path = os.path.join(os.path.dirname(__file__), "Assets")
knight_path = os.path.join(assets_path, "Knight")
player_x = 180
player_y = -120
player = Player(player_x, player_y)

# 3. Game Loop
while True:
    # Limpa a tela (fundo preto)
    janela.set_background_color((25, 25, 25))

    # Atualiza a lógica do jogador
    player.updatee()

    # Desenha o jogador
    player.draww()

    # Atualiza a janela
    janela.update()
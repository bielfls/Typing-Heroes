from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import os

class LoboP2:
    def __init__(self):
        #definindo os caminhos dos arquivos pra pegar os sprites
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        lobo_path = os.path.join(assets_path, "Lobo")
        #definindo as animaçoes e quantos frames cada tem
        self.png = Sprite(os.path.join(lobo_path, "lobo.png"))
        self.idle_anim = Sprite(os.path.join(lobo_path, "Idle.png"), 8)
        self.attack1_anim = Sprite(os.path.join(lobo_path, "Attack_1.png"), 6)
        self.attack2_anim = Sprite(os.path.join(lobo_path, "Attack_2.png"), 4)
        self.attack3_anim = Sprite(os.path.join(lobo_path, "Attack_3.png"), 5)
        self.dead_anim = Sprite(os.path.join(lobo_path, "Dead.png"), 2)

        #flipando o sprite
        self.png.image = pygame.transform.flip(self.png.image, True, False)
        self.idle_anim.image = pygame.transform.flip(self.idle_anim.image, True, False)
        self.attack1_anim.image = pygame.transform.flip(self.attack1_anim.image, True, False)
        self.attack2_anim.image = pygame.transform.flip(self.attack2_anim.image, True, False)
        self.attack3_anim.image = pygame.transform.flip(self.attack3_anim.image, True, False)
        self.dead_anim.image = pygame.transform.flip(self.dead_anim.image, True, False)

        #definindo o tempo de animação de cada uma (em milisegundos)
        self.idle_anim.set_total_duration(1000)
        self.attack1_anim.set_total_duration(500)
        self.attack2_anim.set_total_duration(500)
        self.attack3_anim.set_total_duration(500)
        self.dead_anim.set_total_duration(1000)

        #definindo as variaveis para ajudar no controle das animaçoes
        self.estado = "IDLE"
        self.anim_atual = self.idle_anim

        #teclado pra controle das animacoes no meio da partida (vou usar na função de comportamento dos players na partida)
        self.teclado = Window.get_keyboard()

        self.dr=1
        self.dd=1
        self.duracao_especial=5
        self.timer_especial=0

    def especial(self):
        self.dd=1
        self.dr=0.5

    def padrao(self):
        self.dd=1
        self.dr=1
        self.timer_especial=0

    def ataque_1(self):
        #muda o estado para ataque
        if self.estado == "IDLE":
            self.estado = "ATACANDO_1"
            #muda a animação atual para o de ataque
            self.anim_atual = self.attack1_anim
            #reinicia a animação para o primeiro frame (para não dar problema quando vc trocar animações do meio de outras)
            self.anim_atual.set_curr_frame(0)

    def ataque_2(self):
        #muda o estado para ataque
        if self.estado == "IDLE":
            self.estado = "ATACANDO_2"
            #muda a animação atual para o de ataque
            self.anim_atual = self.attack2_anim
            #reinicia a animação para o primeiro frame (para não dar problema quando vc trocar animações do meio de outras)
            self.anim_atual.set_curr_frame(0)

    def ataque_3(self):
        #muda o estado para ataque
        if self.estado == "IDLE":
            self.estado = "ATACANDO_3"
            #muda a animação atual para o de ataque
            self.anim_atual = self.attack3_anim
            #reinicia a animação para o primeiro frame (para não dar problema quando vc trocar animações do meio de outras)
            self.anim_atual.set_curr_frame(0)

    def morre(self):
        #muda o estado para ataque
        if self.estado == "IDLE":
            self.estado = "MORRE"
            #muda a animação atual para o de ataque
            self.anim_atual = self.dead_anim
            #reinicia a animação para o primeiro frame (para não dar problema quando vc trocar animações do meio de outras)
            self.anim_atual.set_curr_frame(0)

    def atualiza_anim(self):
        #essa função faz com que quando vc chame a animação de ataque, quando a animação acaba volta para IDLE

        #pegar o ultimo frame antes do update
        frame_anterior = self.anim_atual.get_curr_frame()

        #atualiza a animacão
        self.anim_atual.update()

        if self.estado == "ATACANDO_1" or self.estado == "ATACANDO_2" or self.estado == "ATACANDO_3":
            #pega o numero total de frames da animacao atual
            total_frames = self.anim_atual.total_frames
            #pega o frame final (o qual sera o ultimo a ser animado)
            frame_final_index = total_frames - 1
            #pega o frame logo após do update
            frame_atual = self.anim_atual.get_curr_frame()

            #se o frame anterior é o frame final então o frame acabou de loopar
            if frame_anterior == frame_final_index and frame_atual == 0:
                #ataque acabou, precisa voltar pro IDLE
                self.estado = "IDLE"
                self.anim_atual = self.idle_anim

    def desenha(self):
        #desenha a animação atual certo
        self.anim_atual.draw()
#imports
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random
import os

class MecanicaSetas():
    def __init__(self, janela:Window):
        # listas de setas
        self.lista_az=[]; self.lista_am=[]; self.lista_vd=[]; self.lista_vm=[]
        self.lista_az2=[]; self.lista_am2=[]; self.lista_vd2=[]; self.lista_vm2=[]

        # variáveis de controle
        self.combo_max=self.combo_max2=0
        self.combo=self.combo2=0
        self.pontos=self.pontos2=0
        self.tempo=0
        self.vel_y=random.randint(400,600)
        self.contagem=[0,0,0,0]
        self.contagem2=[0,0,0,0]
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.lifebar_vermelha=Sprite(os.path.join(assets_path, "life_bar_vermelha.png")); self.lifebar_vermelha.set_position(0, janela.height-self.lifebar_vermelha.height)
        self.lifebar_verde=Sprite(os.path.join(assets_path, "life_bar_verde.png")); self.lifebar_verde.set_position(0, janela.height-self.lifebar_verde.height)
        self.lifebar_vermelha2=Sprite(os.path.join(assets_path, "life_bar_vermelha.png")); self.lifebar_vermelha2.set_position(janela.width-self.lifebar_vermelha.width, janela.height-self.lifebar_vermelha.height)
        self.lifebar_verde2=Sprite(os.path.join(assets_path, "life_bar_verde.png")); self.lifebar_verde2.set_position(janela.width-self.lifebar_verde.width, janela.height-self.lifebar_verde.height)
        self.lifebar_linha=Sprite(os.path.join(assets_path, "life_bar_linha.png")); self.lifebar_linha.set_position(0, janela.height-self.lifebar_linha.height)
        self.lifebar_linha2=Sprite(os.path.join(assets_path, "life_bar_linha.png")); self.lifebar_linha2.set_position(janela.width-self.lifebar_linha.width, janela.height-self.lifebar_linha.height)
        #tempo_partida=120 #(120s/2min)

        self.estadoanterior_p=self.estadoatual_p=False
        self.estadoanterior_o=self.estadoatual_o=False
        self.estadoanterior_i=self.estadoatual_i=False
        self.estadoanterior_u=self.estadoatual_u=False
        self.estadoanterior_r=self.estadoatual_r=False
        self.estadoanterior_e=self.estadoatual_e=False
        self.estadoanterior_w=self.estadoatual_w=False
        self.estadoanterior_q=self.estadoatual_q=False


        # setas fixas jogador 1
        self.seta_amarela=Sprite(os.path.join(assets_path, "hitboxamarelo.png")); self.seta_amarela.set_position(30,20)
        self.seta_vermelha=Sprite(os.path.join(assets_path, "hitboxvermelha.png")); self.seta_vermelha.set_position(30*2+self.seta_amarela.width ,20)
        self.seta_azul=Sprite(os.path.join(assets_path, "hitboxazul.png")); self.seta_azul.set_position(30*3+self.seta_amarela.width*2 ,20)
        self.seta_verde=Sprite(os.path.join(assets_path, "hitboxverde.png")); self.seta_verde.set_position(30*4+self.seta_amarela.width*3 ,20)

        # setas fixas jogador 2
        self.seta_amarela2=Sprite(os.path.join(assets_path, "hitboxamarelo.png")); self.seta_amarela2.set_position(janela.width - 30 - self.seta_amarela2.width,20)
        self.seta_vermelha2=Sprite(os.path.join(assets_path, "hitboxvermelha.png")); self.seta_vermelha2.set_position(janela.width - 30*2 - self.seta_amarela2.width*2,20)
        self.seta_azul2=Sprite(os.path.join(assets_path, "hitboxazul.png")); self.seta_azul2.set_position(janela.width - 30*3 - self.seta_amarela2.width*3,20)
        self.seta_verde2=Sprite(os.path.join(assets_path, "hitboxverde.png")); self.seta_verde2.set_position(janela.width - 30*4 - self.seta_amarela2.width*4,20)

        # controladores de colisão
        self.elimina_azul=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"))
        self.elimina_amarela=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"))
        self.elimina_verde=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"))
        self.elimina_vermelha=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"))

        self.elimina_azul2=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"))
        self.elimina_amarela2=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"))
        self.elimina_verde2=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"))
        self.elimina_vermelha2=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"))

        self.brilho_azul=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"));self.brilho_azul.set_position(30*3+self.seta_amarela.width*2 ,20)
        self.brilho_amarela=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"));self.brilho_amarela.set_position(30 ,20)
        self.brilho_verde=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"));self.brilho_verde.set_position(30*4+self.seta_amarela.width*3 ,20)
        self.brilho_vermelha=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"));self.brilho_vermelha.set_position(30*2+self.seta_amarela.width ,20)

        self.brilho_azul2=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"));self.brilho_azul2.set_position(janela.width - 30*3 - self.seta_amarela2.width*3,20)
        self.brilho_amarela2=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"));self.brilho_amarela2.set_position(janela.width - 30 - self.seta_amarela2.width,20)
        self.brilho_verde2=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"));self.brilho_verde2.set_position(janela.width - 30*4 - self.seta_amarela2.width*4,20)
        self.brilho_vermelha2=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"));self.brilho_vermelha2.set_position(janela.width - 30*2 - self.seta_amarela2.width*2,20)

        # controladores de qualidade do acerto
        self.perfect_az=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_az.set_position(self.seta_azul.x+self.seta_azul.width/2,self.seta_azul.y+self.seta_azul.height/2)
        self.perfect_am=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_am.set_position(self.seta_amarela.x+self.seta_amarela.width/2,self.seta_amarela.y+self.seta_amarela.height/2)
        self.perfect_vd=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_vd.set_position(self.seta_verde.x+self.seta_verde.width/2,self.seta_verde.y+self.seta_verde.height/2)
        self.perfect_vm=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_vm.set_position(self.seta_vermelha.x+self.seta_vermelha.width/2,self.seta_vermelha.y+self.seta_vermelha.height/2)

        self.perfect_az2=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_az2.set_position(self.seta_azul2.x+self.seta_azul2.width/2,self.seta_azul2.y+self.seta_azul2.height/2)
        self.perfect_am2=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_am2.set_position(self.seta_amarela2.x+self.seta_amarela2.width/2,self.seta_amarela2.y+self.seta_amarela2.height/2)
        self.perfect_vd2=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_vd2.set_position(self.seta_verde2.x+self.seta_verde2.width/2,self.seta_verde2.y+self.seta_verde2.height/2)
        self.perfect_vm2=Sprite(os.path.join(assets_path, "pixel_preto.png")); self.perfect_vm2.set_position(self.seta_vermelha2.x+self.seta_vermelha2.width/2,self.seta_vermelha2.y+self.seta_vermelha2.height/2)

        self.usos=self.usos2=0
        self.especial_ativo=self.especial_ativo2=False
        self.especial_timer=self.especial_timer2=0
        self.padronizou=self.padronizou2=True


        # inicializar fora da tela
        for e in [self.elimina_azul, self.elimina_amarela, self.elimina_verde, self.elimina_vermelha,
                self.elimina_azul2, self.elimina_amarela2, self.elimina_verde2, self.elimina_vermelha2]:
            e.set_position(3000,4000)

    def mecanica(self, janela:Window, teclado:keyboard):
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")
        dt = janela.delta_time()
        
        self.lifebar_vermelha.draw()
        self.lifebar_verde.draw()
        self.lifebar_vermelha2.draw()
        self.lifebar_verde2.draw()
        self.lifebar_linha.draw()
        self.lifebar_linha2.draw()
        # desenhar e mover setas jogador 1
        for lista, elimina, player_ref, perfect, estadoanterior_letra, estadoatual_letra in [
            (self.lista_vd, self.elimina_verde, "p1", self.perfect_vd, self.estadoanterior_r, self.estadoatual_r),
            (self.lista_vm, self.elimina_vermelha, "p1", self.perfect_vm, self.estadoanterior_w, self.estadoatual_w),
            (self.lista_am, self.elimina_amarela, "p1", self.perfect_am,  self.estadoanterior_q, self.estadoatual_q),
            (self.lista_az, self.elimina_azul, "p1", self.perfect_az, self.estadoanterior_e, self.estadoatual_e)
        ]:
            acertou = False
            for seta in lista[:]:
                seta.draw()
                seta.y -= self.vel_y * dt
                if elimina.collided(seta):
                    acertou=True
                    if player_ref=="p1":
                        if perfect.collided(seta):
                            self.lifebar_verde2.y+=2
                            #perfeito=1
                            #desenha sprite do perfeito
                            #perfect_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        self.lifebar_verde2.y+=1#+(combo_p1/10)
                        #if not perfeito:
                            #desenha sprite do good
                            #good_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        #perfeito=0
                    lista.remove(seta)
                elif seta.y < -seta.height:
                    lista.remove(seta)
                    if player_ref=="p1":
                        self.lifebar_verde.y+=1
                        #desenha sprite do miss
                        #miss_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        combo=0
            
            if estadoatual_letra and not estadoanterior_letra and not acertou:
                if player_ref=="p1":
                    self.lifebar_verde.y += 1
                    #desenha sprite do miss
                    #miss_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                    combo=0

            if self.combo>=20:
                self.combo_max=True
            else:
                self.combo_max=False
            if acertou:
                if not self.combo_max:
                    self.combo+=1

        # desenhar e mover setas jogador 2
        for lista, elimina, player_ref, perfect, estadoanterior_letra, estadoatual_letra in [
            (self.lista_az2, self.elimina_azul2, "p2", self.perfect_az2, self.estadoanterior_p, self.estadoatual_p),
            (self.lista_am2, self.elimina_amarela2, "p2", self.perfect_am2, self.estadoanterior_i, self.estadoatual_i),
            (self.lista_vd2, self.elimina_verde2, "p2", self.perfect_vd2, self.estadoanterior_u, self.estadoatual_u),
            (self.lista_vm2, self.elimina_vermelha2, "p2", self.perfect_vm2, self.estadoanterior_o, self.estadoatual_o)
        ]:
            acertou = False
            for seta in lista[:]:
                seta.draw()
                seta.y -= self.vel_y * dt
                if elimina.collided(seta):
                    acertou=True
                    if player_ref=="p2":
                        if perfect.collided(seta):
                            self.lifebar_verde.y+=2
                            #perfeito=1
                            #desenha sprite do perfeito
                            #perfect_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        self.lifebar_verde.y+=1#+(combo_p2/10)
                        #if not perfeito:
                            #desenha sprite do good
                            #good_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        #perfeito=0
                    lista.remove(seta)
                elif seta.y < -seta.height:
                    lista.remove(seta)
                    if player_ref=="p2":
                        self.lifebar_verde2.y+=1
                        #desenha sprite do miss
                        #miss_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                        self.combo2=0

            if estadoatual_letra and not estadoanterior_letra and not acertou:
                if player_ref=="p2":
                    self.lifebar_verde2.y += 1
                    #desenha sprite do miss
                    #miss_sprite.set_position(perfect.x-sprite.width/2,perfect.y+um pouquinho)
                    self.combo2=0

            if self.combo2>=20:
                self.combo_max2=True
            else:
                self.combo_max2=False
            if acertou:
                if not self.combo_max2:
                    self.combo2+=1


        # geração de novas setas
        self.tempo += dt
        if self.tempo >= random.uniform(0.4, 0.7):
            self.tempo = 0

            setas_simultaneas = random.randint(1, 3)

            tipos = random.sample([1, 2, 3, 4], setas_simultaneas)

            for gerador in tipos:

                self.contagem[gerador - 1] += 1

                if gerador == 1:
                    nova = Sprite(os.path.join(assets_path, "setaazul.png"))
                    nova.set_position(30*3 + self.seta_amarela.width*2, 648)
                    self.lista_az.append(nova)

                elif gerador == 2:
                    nova = Sprite(os.path.join(assets_path, "setaamarela.png"))
                    nova.set_position(30, 648)
                    self.lista_am.append(nova)

                elif gerador == 3:
                    nova = Sprite(os.path.join(assets_path, "setaverde.png"))
                    nova.set_position(30*4 + self.seta_amarela.width*3, 648)
                    self.lista_vd.append(nova)

                elif gerador == 4:
                    nova = Sprite(os.path.join(assets_path, "setavermelha.png"))
                    nova.set_position(30*2 + self.seta_amarela.width, 648)
                    self.lista_vm.append(nova)

            tipos2 = random.sample([1, 2, 3, 4], setas_simultaneas)

            for gerador2 in tipos2:   

                self.contagem[gerador - 1] += 1

                if gerador2==1: 
                    nova=Sprite(os.path.join(assets_path, "setaazul.png"))
                    nova.set_position(janela.width - 30*3 - self.seta_amarela.width*3,648)
                    self.lista_az2.append(nova)
                elif gerador2==2: 
                    nova=Sprite(os.path.join(assets_path, "setaamarela.png"))
                    nova.set_position(janela.width - 30 - self.seta_amarela.width,648)
                    self.lista_am2.append(nova)
                elif gerador2==3: 
                    nova=Sprite(os.path.join(assets_path, "setaverde.png"))
                    nova.set_position(janela.width - 30*4 - self.seta_amarela.width*4,648)
                    self.lista_vd2.append(nova)
                elif gerador2==4: 
                    nova=Sprite(os.path.join(assets_path, "setavermelha.png"))
                    nova.set_position(janela.width - 30*2 - self.seta_amarela.width*2,648)
                    self.lista_vm2.append(nova)

        self.estadoanterior_r = self.estadoatual_r
        self.estadoanterior_w = self.estadoatual_w
        self.estadoanterior_q = self.estadoatual_q
        self.estadoanterior_e = self.estadoatual_e
        self.estadoanterior_p = self.estadoatual_p
        self.estadoanterior_i = self.estadoatual_i
        self.estadoanterior_u = self.estadoatual_u
        self.estadoanterior_o = self.estadoatual_o

        self.estadoatual_r = teclado.key_pressed("R")
        self.estadoatual_w = teclado.key_pressed("W")
        self.estadoatual_q = teclado.key_pressed("Q")
        self.estadoatual_e = teclado.key_pressed("E")
        self.estadoatual_p = teclado.key_pressed("P")
        self.estadoatual_i = teclado.key_pressed("I")
        self.estadoatual_u = teclado.key_pressed("U")
        self.estadoatual_o = teclado.key_pressed("O")
        
        

        for s in [self.seta_azul,self.seta_verde,self.seta_vermelha,self.seta_amarela,self.seta_azul2,self.seta_verde2,self.seta_vermelha2,self.seta_amarela2]:
            s.draw()

        for estadoanterior_letra, estadoatual_letra, seta, elimina, x, brilho_letra in [
            (self.estadoanterior_i, self.estadoatual_i, self.seta_azul2, self.elimina_azul2, janela.width - 30*3 - self.seta_amarela.width*3, self.brilho_azul2),
            (self.estadoanterior_o, self.estadoatual_o, self.seta_vermelha2, self.elimina_vermelha2, janela.width - 30*2 - self.seta_amarela.width*2, self.brilho_vermelha2),
            (self.estadoanterior_p, self.estadoatual_p, self.seta_amarela2, self.elimina_amarela2, janela.width - 30 - self.seta_amarela.width, self.brilho_amarela2),
            (self.estadoanterior_u, self.estadoatual_u, self.seta_verde2, self.elimina_verde2, janela.width - 30*4 - self.seta_amarela.width*4, self.brilho_verde2),
            (self.estadoanterior_r, self.estadoatual_r, self.seta_verde, self.elimina_verde, 30*4+self.seta_amarela.width*3, self.brilho_verde),
            (self.estadoanterior_e, self.estadoatual_e, self.seta_azul, self.elimina_azul, 30*3+self.seta_amarela.width*2, self.brilho_azul),
            (self.estadoanterior_w, self.estadoatual_w, self.seta_vermelha, self.elimina_vermelha, 30*2+self.seta_amarela.width, self.brilho_vermelha),
            (self.estadoanterior_q, self.estadoatual_q, self.seta_amarela, self.elimina_amarela, 30, self.brilho_amarela)
        ]:
            if estadoatual_letra:
                brilho_letra.draw()
            if estadoanterior_letra==False and estadoatual_letra==True:
                seta.draw()
                elimina.set_position(x,20)
                elimina.draw()
            else:
                elimina.set_position(3000,4000)

    def reinicia_variaveis(self, janela:Window):
        # inicializar fora da tela
        for e in [self.elimina_azul, self.elimina_amarela, self.elimina_verde, self.elimina_vermelha,
                self.elimina_azul2, self.elimina_amarela2, self.elimina_verde2, self.elimina_vermelha2]:
            e.set_position(3000,4000)
        
        self.estadoanterior_p=self.estadoatual_p=False
        self.estadoanterior_o=self.estadoatual_o=False
        self.estadoanterior_i=self.estadoatual_i=False
        self.estadoanterior_u=self.estadoatual_u=False
        self.estadoanterior_r=self.estadoatual_r=False
        self.estadoanterior_e=self.estadoatual_e=False
        self.estadoanterior_w=self.estadoatual_w=False
        self.estadoanterior_q=self.estadoatual_q=False

        self.lifebar_verde.set_position(0, janela.height-self.lifebar_verde.height)
        self.lifebar_verde2.set_position(janela.width-self.lifebar_verde.width, janela.height-self.lifebar_verde.height)

        self.contagem=[0,0,0,0]
        self.contagem2=[0,0,0,0]

        # listas de setas
        self.lista_az=[]; self.lista_am=[]; self.lista_vd=[]; self.lista_vm=[]
        self.lista_az2=[]; self.lista_am2=[]; self.lista_vd2=[]; self.lista_vm2=[]
#imports
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random
import os

# janela e teclado
janela = Window(1152, 648)
teclado = Window.get_keyboard()
janela.set_title("Jogo")

# listas de setas
lista_az=[]; lista_am=[]; lista_vd=[]; lista_vm=[]
lista_az2=[]; lista_am2=[]; lista_vd2=[]; lista_vm2=[]

# variáveis de controle
pontos=pontos2=0
tempo=0
vel_y=400
contagem=[0,0,0,0]
contagem2=[0,0,0,0]
assets_path = os.path.join(os.path.dirname(__file__), "Assets")
lifebar_vermelha=Sprite(os.path.join(assets_path, "life_bar_vermelha.png")); lifebar_vermelha.set_position(0, janela.height-lifebar_vermelha.height)
lifebar_verde=Sprite(os.path.join(assets_path, "life_bar_verde.png")); lifebar_verde.set_position(0, janela.height-lifebar_verde.height)
lifebar_vermelha2=Sprite(os.path.join(assets_path, "life_bar_vermelha.png")); lifebar_vermelha2.set_position(janela.width-lifebar_vermelha.width, janela.height-lifebar_vermelha.height)
lifebar_verde2=Sprite(os.path.join(assets_path, "life_bar_verde.png")); lifebar_verde2.set_position(janela.width-lifebar_verde.width, janela.height-lifebar_verde.height)
lifebar_linha=Sprite(os.path.join(assets_path, "life_bar_linha.png")); lifebar_linha.set_position(0, janela.height-lifebar_linha.height)
lifebar_linha2=Sprite(os.path.join(assets_path, "life_bar_linha.png")); lifebar_linha2.set_position(janela.width-lifebar_linha.width, janela.height-lifebar_linha.height)
#tempo_partida=120 #(120s/2min)

# função pra criar sprite redimensionado (mantém hitbox certa)
def criar_sprite(caminho, largura, altura):
    s = Sprite(caminho)
    s.image = pygame.transform.scale(s.image, (largura, altura))
    s.width = largura
    s.height = altura
    return s
    
estadoanterior_p=estadoatual_p=False
estadoanterior_o=estadoatual_o=False
estadoanterior_i=estadoatual_i=False
estadoanterior_u=estadoatual_u=False
estadoanterior_r=estadoatual_r=False
estadoanterior_e=estadoatual_e=False
estadoanterior_w=estadoatual_w=False
estadoanterior_q=estadoatual_q=False


# setas fixas jogador 1
seta_amarela=Sprite(os.path.join(assets_path, "hitboxamarelo.png")); seta_amarela.set_position(30,20)
seta_vermelha=Sprite(os.path.join(assets_path, "hitboxvermelha.png")); seta_vermelha.set_position(30*2+seta_amarela.width ,20)
seta_azul=Sprite(os.path.join(assets_path, "hitboxazul.png")); seta_azul.set_position(30*3+seta_amarela.width*2 ,20)
seta_verde=Sprite(os.path.join(assets_path, "hitboxverde.png")); seta_verde.set_position(30*4+seta_amarela.width*3 ,20)

# setas fixas jogador 2
seta_amarela2=Sprite(os.path.join(assets_path, "hitboxamarelo.png")); seta_amarela2.set_position(janela.width - 30 - seta_amarela2.width,20)
seta_vermelha2=Sprite(os.path.join(assets_path, "hitboxvermelha.png")); seta_vermelha2.set_position(janela.width - 30*2 - seta_amarela2.width*2,20)
seta_azul2=Sprite(os.path.join(assets_path, "hitboxazul.png")); seta_azul2.set_position(janela.width - 30*3 - seta_amarela2.width*3,20)
seta_verde2=Sprite(os.path.join(assets_path, "hitboxverde.png")); seta_verde2.set_position(janela.width - 30*4 - seta_amarela2.width*4,20)

# controladores de colisão
elimina_azul=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"))
elimina_amarela=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"))
elimina_verde=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"))
elimina_vermelha=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"))

elimina_azul2=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"))
elimina_amarela2=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"))
elimina_verde2=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"))
elimina_vermelha2=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"))

brilho_azul=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"));brilho_azul.set_position(30*3+seta_amarela.width*2 ,20)
brilho_amarela=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"));brilho_amarela.set_position(30 ,20)
brilho_verde=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"));brilho_verde.set_position(30*4+seta_amarela.width*3 ,20)
brilho_vermelha=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"));brilho_vermelha.set_position(30*2+seta_amarela.width ,20)

brilho_azul2=Sprite(os.path.join(assets_path, "seta_azul_brilhante.png"));brilho_azul2.set_position(janela.width - 30*3 - seta_amarela2.width*3,20)
brilho_amarela2=Sprite(os.path.join(assets_path, "seta_amarela_brilhante.png"));brilho_amarela2.set_position(janela.width - 30 - seta_amarela2.width,20)
brilho_verde2=Sprite(os.path.join(assets_path, "seta_verde_brilhante.png"));brilho_verde2.set_position(janela.width - 30*4 - seta_amarela2.width*4,20)
brilho_vermelha2=Sprite(os.path.join(assets_path, "seta_vermelha_brilhante.png"));brilho_vermelha2.set_position(janela.width - 30*2 - seta_amarela2.width*2,20)

# controladores de qualidade do acerto
perfect_az=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_az.set_position(seta_azul.x+seta_azul.width/2,seta_azul.y+seta_azul.height/2)
perfect_am=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_am.set_position(seta_amarela.x+seta_amarela.width/2,seta_amarela.y+seta_amarela.height/2)
perfect_vd=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_vd.set_position(seta_verde.x+seta_verde.width/2,seta_verde.y+seta_verde.height/2)
perfect_vm=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_vm.set_position(seta_vermelha.x+seta_vermelha.width/2,seta_vermelha.y+seta_vermelha.height/2)

perfect_az2=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_az2.set_position(seta_azul2.x+seta_azul2.width/2,seta_azul2.y+seta_azul2.height/2)
perfect_am2=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_am2.set_position(seta_amarela2.x+seta_amarela2.width/2,seta_amarela2.y+seta_amarela2.height/2)
perfect_vd2=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_vd2.set_position(seta_verde2.x+seta_verde2.width/2,seta_verde2.y+seta_verde2.height/2)
perfect_vm2=Sprite(os.path.join(assets_path, "pixel_preto.png")); perfect_vm2.set_position(seta_vermelha2.x+seta_vermelha2.width/2,seta_vermelha2.y+seta_vermelha2.height/2)

# inicializar fora da tela
for e in [elimina_azul, elimina_amarela, elimina_verde, elimina_vermelha,
          elimina_azul2, elimina_amarela2, elimina_verde2, elimina_vermelha2]:
    e.set_position(3000,4000)
    
# loop principal
while True:
    janela.set_background_color((25, 25, 25))
    dt = janela.delta_time()
    
    lifebar_vermelha.draw()
    lifebar_verde.draw()
    lifebar_vermelha2.draw()
    lifebar_verde2.draw()
    lifebar_linha.draw()
    lifebar_linha2.draw()
    # desenhar e mover setas jogador 1
    for lista, elimina, player_ref, perfect, letra, estadoanterior_letra, estadoatual_letra in [
        (lista_vd, elimina_verde, "p1", perfect_vd, "R", estadoanterior_r, estadoatual_r),
        (lista_vm, elimina_vermelha, "p1", perfect_vm, "W", estadoanterior_w, estadoatual_w),
        (lista_am, elimina_amarela, "p1", perfect_am, "Q", estadoanterior_q, estadoatual_q),
        (lista_az, elimina_azul, "p1", perfect_az, "E", estadoanterior_e, estadoatual_e)
    ]:
        for seta in lista[:]:
            seta.draw()
            seta.y -= vel_y * dt
            if elimina.collided(seta):
                if player_ref=="p1":
                    if perfect.collided(seta):
                        pontos+=200
                    pontos+=100
                lista.remove(seta)
            elif seta.y < -seta.height:
                lista.remove(seta)
                if player_ref=="p1":
                    pontos2+=100
            else:
                if estadoatual_letra==True and estadoanterior_letra==False:
                    if player_ref=="p1":
                        pontos2+=100
                        
                    
    # desenhar e mover setas jogador 2
    for lista, elimina, player_ref, perfect, letra, estadoanterior_letra, estadoatual_letra in [
        (lista_az2, elimina_azul2, "p2", perfect_az2, "P", estadoanterior_p, estadoatual_p),
        (lista_am2, elimina_amarela2, "p2", perfect_am2, "I", estadoanterior_i, estadoatual_i),
        (lista_vd2, elimina_verde2, "p2", perfect_vd2, "U", estadoanterior_u, estadoatual_u),
        (lista_vm2, elimina_vermelha2, "p2", perfect_vm2, "O", estadoanterior_o, estadoatual_o)
    ]:
        for seta in lista[:]:
            seta.draw()
            seta.y -= vel_y * dt
            if elimina.collided(seta):
                if player_ref=="p2":
                    if perfect.collided(seta):
                        pontos2+=200
                    pontos2+=100
                lista.remove(seta)
            elif seta.y < -seta.height:
                lista.remove(seta)
                if player_ref=="p2":
                    pontos+=100
            else:
                if estadoatual_letra==True and estadoanterior_letra==False:
                    if player_ref=="p2":
                        pontos+=100

    # geração de novas setas
    tempo += dt
    if tempo >= random.uniform(0.4, 0.7):
        tempo = 0
        qtd = len(lista_az)+len(lista_am)+len(lista_vd)+len(lista_vm)
        qtd2 = len(lista_az2)+len(lista_am2)+len(lista_vd2)+len(lista_vm2)

        if qtd < 7:
            if qtd%2==0:
                gerador = contagem.index(min(contagem)) + 1 
            else:
                gerador=random.randint(1,4)
            contagem[gerador-1] += 1
            if gerador==1:
                nova=Sprite(os.path.join(assets_path, "setaazul.png"))
                nova.set_position(30*3+seta_amarela.width*2,648)
                lista_az.append(nova)
            elif gerador==2:
                nova=Sprite(os.path.join(assets_path, "setaamarela.png"))
                nova.set_position(30,648)
                lista_am.append(nova)
            elif gerador==3:
                nova=Sprite(os.path.join(assets_path, "setaverde.png"))
                nova.set_position(30*4+seta_amarela.width*3,648)
                lista_vd.append(nova)
            elif gerador==4:
                nova=Sprite(os.path.join(assets_path, "setavermelha.png"))
                nova.set_position(30*2+seta_amarela.width,648)
                lista_vm.append(nova)

        if qtd2 < 7:
            if qtd2%2==0:
                gerador2 = contagem2.index(min(contagem2)) + 1 
            else:
                gerador2=random.randint(1,4)
            contagem2[gerador2-1] += 1
            if gerador2==1: 
                nova=Sprite(os.path.join(assets_path, "setaazul.png"))
                nova.set_position(janela.width - 30*3 - seta_amarela.width*3,648)
                lista_az2.append(nova)
            elif gerador2==2: 
                nova=Sprite(os.path.join(assets_path, "setaamarela.png"))
                nova.set_position(janela.width - 30 - seta_amarela.width,648)
                lista_am2.append(nova)
            elif gerador2==3: 
                nova=Sprite(os.path.join(assets_path, "setaverde.png"))
                nova.set_position(janela.width - 30*4 - seta_amarela.width*4,648)
                lista_vd2.append(nova)
            elif gerador2==4: 
                nova=Sprite(os.path.join(assets_path, "setavermelha.png"))
                nova.set_position(janela.width - 30*2 - seta_amarela.width*2,648)
                lista_vm2.append(nova)

    estadoanterior_r = estadoatual_r
    estadoanterior_w = estadoatual_w
    estadoanterior_q = estadoatual_q
    estadoanterior_e = estadoatual_e
    estadoanterior_p = estadoatual_p
    estadoanterior_i = estadoatual_i
    estadoanterior_u = estadoatual_u
    estadoanterior_o = estadoatual_o

    estadoatual_r = teclado.key_pressed("R")
    estadoatual_w = teclado.key_pressed("W")
    estadoatual_q = teclado.key_pressed("Q")
    estadoatual_e = teclado.key_pressed("E")
    estadoatual_p = teclado.key_pressed("P")
    estadoatual_i = teclado.key_pressed("I")
    estadoatual_u = teclado.key_pressed("U")
    estadoatual_o = teclado.key_pressed("O")
    
    lifebar_verde.y+=pontos2*0.00001
    lifebar_verde2.y+=pontos*0.00001

    for s in [seta_azul,seta_verde,seta_vermelha,seta_amarela,seta_azul2,seta_verde2,seta_vermelha2,seta_amarela2]:
        s.draw()

    for estadoanterior_letra, estadoatual_letra, seta, elimina, x, brilho_letra in [
        (estadoanterior_i, estadoatual_i, seta_azul2, elimina_azul2, janela.width - 30*3 - seta_amarela.width*3, brilho_azul2),
        (estadoanterior_o, estadoatual_o, seta_vermelha2, elimina_vermelha2, janela.width - 30*2 - seta_amarela.width*2, brilho_vermelha2),
        (estadoanterior_p, estadoatual_p, seta_amarela2, elimina_amarela2, janela.width - 30 - seta_amarela.width, brilho_amarela2),
        (estadoanterior_u, estadoatual_u, seta_verde2, elimina_verde2, janela.width - 30*4 - seta_amarela.width*4, brilho_verde2),
        (estadoanterior_r, estadoatual_r, seta_verde, elimina_verde, 30*4+seta_amarela.width*3, brilho_verde),
        (estadoanterior_e, estadoatual_e, seta_azul, elimina_azul, 30*3+seta_amarela.width*2, brilho_azul),
        (estadoanterior_w, estadoatual_w, seta_vermelha, elimina_vermelha, 30*2+seta_amarela.width, brilho_vermelha),
        (estadoanterior_q, estadoatual_q, seta_amarela, elimina_amarela, 30, brilho_amarela)
    ]:
        if estadoatual_letra:
            brilho_letra.draw()
        if estadoanterior_letra==False and estadoatual_letra==True:
            seta.draw()
            elimina.set_position(x,20)
            elimina.draw()
        else:
            elimina.set_position(3000,4000)

    if teclado.key_pressed("ESC"): janela.close()

    # placar
    janela.draw_text(f"P1: {pontos}", 10, 10, 20, (255,255,255))
    janela.draw_text(f"P2: {pontos2}", 800, 10, 20, (255,255,255))
    
    
    #---------GAMEOVER-------------#
    #tempo_partida-=1
    #if tempo_partida<=0:
        #if lifebar_verde.y>lifebar_verde2.y:
            #player1 vence
        #elif lifebar_verde.y<lifebar_verde2.y:
            #player2 vence
        #else:
            #empate
    #elif lifebar_verde.y<=0:
        #if lifebar_verde2.y<=0:
            #empate
        #else:
            #player2 vence
    #elif lifebar_verde2.y<=0:
        #player1 vence

    janela.update()

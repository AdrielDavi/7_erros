import pygame #parte gráfica
from pygame import mixer
from pygame.locals import *

pygame.init() #iniciar o pygame
pygame.display.set_caption("7 ERROS") #Título do programa
#Imagens
verdadeira = pygame.image.load("images/poseidon1.jpg") #499x312
alterada = pygame.image.load("images/poseidon.jpg") 
pngegg = pygame.image.load("images/pngegg.png")
pngegg2 = pygame.transform.scale(pngegg, (250, 200))
circulo = pygame.image.load("images/circulo.png")
circulo2 = pygame.transform.scale(circulo, (25, 20))
lvl2 = pygame.image.load("images/lvl2.png")
lvl2c = pygame.image.load("images/lvl2c.png")
lvl3 = pygame.image.load("images/lvl3.png")
lvl3c = pygame.image.load("images/lvl3c.png")
hades_true = pygame.image.load("images/hades.jpg")
hadesf = pygame.image.load("images/hadesf.jpg")
zeus_true = pygame.image.load("images/zeus_true.jpg")
zeus_f = pygame.image.load("images/zeus_f.jpg")
fim = pygame.image.load("images/fim.png")

#tamanho da janela do Pupila
largura = 1130
altura = 400
tela = pygame.display.set_mode((largura, altura))
#Cores 
cinza = (107, 107, 107)
branco = (255, 255, 255)
#Variavéis
acertos = 0
braco = 0
coroa = 0
espinho = 0
cintura = 0 
barriga = 0
mao = 0
espada = 0
level = 1
#Variavéis lvl2
coroah = 0
corrente = 0
pedra = 0
anel = 0
lanca = 0
olho = 0
triolho = 0
#Variavéis lvl3
boca = 0
orelha = 0
raio = 0
cabelo = 0
ombroe = 0
ombrod = 0
olhoz = 0

#pygame
fonte = pygame.font.Font("GentiumPlus-6.200/GentiumPlus-BoldItalic.ttf", 36)
fontewin = pygame.font.Font("GentiumPlus-6.200/GentiumPlus-BoldItalic.ttf", 100)
fonteerro = pygame.font.Font("GentiumPlus-6.200/GentiumBookPlus-Italic.ttf", 18)
while True:
    for event in pygame.event.get():       
        #Sair
        if event.type == QUIT: 
            pygame.quit()
            exit()
            
        #imagens da tela
        if level == 1:
            tela.fill(cinza) 
            tela.blit(verdadeira,(50,30)) 
            tela.blit(alterada,(580,30))
            texto = fonte.render("Acertos "+str(acertos), True, branco)
            textowin = fontewin.render("VOCÊ GANHOU", True, branco)
            textoerro = fonteerro.render("Indique o erro na imagem a esquerda", True, branco)
            textoache = fonteerro.render("Compare as duas imagens e ache os 7 erros nesta ilustração de Poseidon o Deus dos mares ", True, branco)
            tela.blit(textoache, (330, 3))
            tela.blit(texto, (515, 350)) # CONTAGEM DE ACERTOS
            mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
            
            if braco == 1:
                tela.blit(circulo2, (105, 128))
            if coroa == 1:
                tela.blit(circulo2, (200, 45))
            if barriga == 1:
                tela.blit(circulo2, (206, 209))
            if cintura == 1:
                tela.blit(circulo2, (158, 230))
            if espinho == 1:
                tela.blit(circulo2, (115, 110))
            if espada == 1:
                tela.blit(circulo2, (381, 263))
            if mao == 1:
                tela.blit(circulo2, (360, 180))
            if acertos == 7:
                    tela.blit(textowin, (290, 100))
                    tela.blit(lvl2, (380, 240))
                    if mx >= 380 and mx <= 738 and my >= 240 and my <= 314:
                        tela.blit(lvl2c, (380, 240))
                    if event.type == MOUSEBUTTONDOWN:
                        if mx >= 380 and mx <= 738 and my >= 240 and my <= 314:
                            acertos = 0
                            level = 2
                        
                        
                        
                    
            # IMAGEM VERDADEIRA
            if event.type == MOUSEBUTTONDOWN:
                if mx >= 113 and mx <= 125 and my >= 135 and my <= 143:
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if braco == 0:
                        acertos = acertos + 1
                        braco = 1

                if mx >= 204 and mx <= 217 and my >= 34 and my <= 64 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if coroa == 0:
                        acertos = acertos + 1
                        coroa = 1  

                if mx >= 207 and mx <= 221 and my >= 201 and my <= 226 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if barriga == 0:
                        acertos = acertos + 1
                        barriga = 1  

                if mx >= 159 and mx <= 172 and my >= 226 and my <= 245 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if cintura == 0:
                        acertos = acertos + 1
                        cintura = 1 

                if mx >= 117 and mx <= 131 and my >= 114 and my <= 127 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if espinho == 0:
                        acertos = acertos + 1
                        espinho = 1

                if mx >= 381 and mx <= 404 and my >= 263 and my <= 278 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if espada == 0:
                        acertos = acertos + 1
                        espada = 1 
                if mx >= 360 and mx <= 391 and my >= 184 and my <= 202 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if mao == 0:
                        acertos = acertos + 1
                        mao = 1  
                #fora da imagem da tela
                if mx >= 578 and mx <= 1079 :
                    tela.blit(textoerro, (465, 342))
        
        #LEVEL 2
        
        if level == 2:
            tela.fill(cinza) 
            tela.blit(hades_true,(50,30)) 
            tela.blit(hadesf,(580,30))
            texto = fonte.render("Acertos "+str(acertos), True, branco)
            textowin = fontewin.render("VOCÊ GANHOU", True, branco)
            textoerro = fonteerro.render("Indique o erro na imagem a esquerda", True, branco)
            textoache = fonteerro.render("Compare as duas imagens e ache os 7 erros nesta ilustração de Hades o Deus do Submundo junto de seu cão de guarda Cérbero", True, branco)
            tela.blit(textoache, (150, 3))
            tela.blit(texto, (515, 350)) # CONTAGEM DE ACERTOS
            mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
            
   
            if coroah == 1:
                tela.blit(circulo2, (330, 58))
            if corrente == 1:
                tela.blit(circulo2, (203, 300))
            if pedra == 1:
                tela.blit(circulo2, (435, 43))
            if anel == 1:
                tela.blit(circulo2, (500, 90))
            if lanca == 1:
                tela.blit(circulo2, (495, 281))
            if olho == 1:
                tela.blit(circulo2, (132, 135))
            if triolho == 1:
                tela.blit(circulo2, (62, 186))
                
            if acertos == 7:
                    tela.blit(textowin, (290, 100))
                    tela.blit(lvl3, (380, 240))
                    if mx >= 380 and mx <= 738 and my >= 240 and my <= 314:
                        tela.blit(lvl3c, (380, 240))
                    if event.type == MOUSEBUTTONDOWN:
                        if mx >= 380 and mx <= 738 and my >= 240 and my <= 314:
                            acertos = 0
                            level = 3
                        
                        
                        
                    
            # IMAGEM VERDADEIRA
            if event.type == MOUSEBUTTONDOWN:
    
                if mx >= 203 and mx <= 233 and my >= 283 and my <= 334:
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if corrente == 0:
                        acertos = acertos + 1
                        corrente = 1

                if mx >= 336 and mx <= 348 and my >= 68 and my <= 81 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if coroah == 0:
                        acertos = acertos + 1
                        coroah = 1  

                if mx >= 495 and mx <= 528 and my >= 281 and my <= 335 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if lanca == 0:
                        acertos = acertos + 1
                        lanca = 1  

                if mx >= 405 and mx <= 505 and my >= 33 and my <= 68 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if pedra == 0:
                        acertos = acertos + 1
                        pedra = 1 

                if mx >= 138 and mx <= 148 and my >= 140 and my <= 153 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if olho == 0:
                        acertos = acertos + 1
                        olho = 1

                if mx >= 62 and mx <= 90 and my >= 186 and my <= 209 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if triolho == 0:
                        acertos = acertos + 1
                        triolho = 1 
                if mx >= 508 and mx <= 519 and my >= 97 and my <= 109 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if anel == 0:
                        acertos = acertos + 1
                        anel = 1  
                #fora da imagem da tela
                if mx >= 578 and mx <= 1079 :
                    tela.blit(textoerro, (465, 342))
        #LEVEL 3
        
        if level == 3:
            tela.fill(cinza) 
            tela.blit(zeus_true,(50,30)) 
            tela.blit(zeus_f,(580,30))
            texto = fonte.render("Acertos "+str(acertos), True, branco)
            textowin = fontewin.render("VOCÊ GANHOU", True, branco)
            textoerro = fonteerro.render("Indique o erro na imagem a esquerda", True, branco)
            textoache = fonteerro.render("Compare as duas imagens e ache os 7 erros nesta ilustração de Zeus o Deus do Raio", True, branco)
            tela.blit(textoache, (150, 3))
            tela.blit(texto, (515, 350)) # CONTAGEM DE ACERTOS
            mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
            
   
            if boca == 1:
                tela.blit(circulo2, (340, 174))
            if ombroe == 1:
                tela.blit(circulo2, (190, 300))
            if ombrod == 1:
                tela.blit(circulo2, (453, 260))
            if orelha == 1:
                tela.blit(circulo2, (240, 130))
            if raio == 1:
                tela.blit(circulo2, (475, 122))
            if cabelo == 1:
                tela.blit(circulo2, (310, 59))
            if olhoz == 1:
                tela.blit(circulo2, (319, 115))
                
            if acertos == 7:
                    tela.blit(textowin, (290, 100))
                    level = 4
                   
                        
                        
                        
                    
            # IMAGEM VERDADEIRA
            if event.type == MOUSEBUTTONDOWN:
                
                
                if mx >= 319 and mx <= 335 and my >= 115 and my <= 129:
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if olhoz == 0:
                        acertos = acertos + 1
                        olhoz = 1

                if mx >= 326 and mx <= 367 and my >= 174 and my <= 193 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if boca == 0:
                        acertos = acertos + 1
                        boca = 1  

                if mx >= 222 and mx <= 285 and my >= 112 and my <= 174 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if orelha == 0:
                        acertos = acertos + 1
                        orelha = 1  

                if mx >= 182 and mx <= 223 and my >= 287 and my <= 335 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if ombroe == 0:
                        acertos = acertos + 1
                        ombroe = 1 

                if mx >= 453 and mx <= 490 and my >= 247 and my <= 303 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if ombrod == 0:
                        acertos = acertos + 1
                        ombrod = 1

                if mx >= 293 and mx <= 350 and my >= 59 and my <= 80 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if cabelo == 0:
                        acertos = acertos + 1
                        cabelo = 1 
                if mx >= 449 and mx <= 528 and my >= 40 and my <= 146 :
                    if acertos != 7:
                        tela.blit(pngegg2,(900,130))
                    if raio == 0:
                        acertos = acertos + 1
                        raio = 1  
                #fora da imagem da tela
                if mx >= 578 and mx <= 1079 :
                    tela.blit(textoerro, (465, 342))
        if level == 4:
            tela.blit(fim, (0, 0))
            

                

    
                 
                
            
    pygame.display.update() #Atualiza o  pygame (pupila parte gráfica)
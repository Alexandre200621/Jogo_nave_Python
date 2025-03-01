from time import sleep
from random import randint
import pygame
from pygame.locals import *
from sys import exit
#sleep(3600)
#print(f"Feliz ano novo")
def tirochefao(qualtiro):
    if nave.colliderect(qualtiro):
        global tiro_chefao1, tiro_chefao2, tiro_chefao3, tiro_chefao4, tiro_chefao5, tiro_chefao6, y, vidas
        vidas = vidas - 1
        tiro_chefao1 = False
        tiro_chefao2 = False
        tiro_chefao3 = False
        tiro_chefao4 = False
        tiro_chefao5 = False
        tiro_chefao6 = False
        y = 8999

def gameroveralien1(v):
    global vidas_do_alien, x_a, fase, y_a, pontos
    if vidas_do_alien == v:
        x_a = randint(20, 650)
        y_a = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien = vidas_do_alien + 6

        if fase == 2:
            vidas_do_alien = vidas_do_alien + 9

        if fase == 3:
            vidas_do_alien = vidas_do_alien + 12

        if fase == 4:
            vidas_do_alien = vidas_do_alien + 15

        if fase == 5:
            vidas_do_alien = vidas_do_alien + 18
        pontos = pontos + 200

def gameoverchefao(v):
    global vidas_do_chefao, y_chefao
    if vidas_do_chefao == v:
        y_chefao = 100000

def fasedojogo(a, b):
    global y_m, y_m1, y_m2, fase
    if fase == a:
        y_m = y_m + b
        y_m1 = y_m1 + b
        y_m2 = y_m2 + b

def tirocolide(qualobjeto, pos, pos1):
    global pontos, x_m, y_m, triggered, x_tiro, y_tiro
    if tiro.colliderect(qualobjeto):
        pos = - 3000
        pos1 = randint(10, 1000)
        pontos = pontos + 100
        triggered = False
        if triggered == False:
            x_tiro = x + 25
            y_tiro = y + 25

def colisaodetiro(a, b):
    global triggered
    if tiro.colliderect(a):
        b = b - 1
        triggered = False



pygame.init()

som = pygame.mixer.Sound('somdoepaquito.wav')
somdotirodanave = pygame.mixer.Sound('somdotirodanave.wav')


largura = 1020
altura = 700



x = 450
y = 450
x_tiro = 480
y_tiro = 480
x_tiro1 = 480
y_tiro1 = 480
x_fun = 0
y_fun = 0
x_fun2 = 0
y_fun2 = -719
x_chefao = 330
y_chefao = -500
x_a = randint(20, 650)
y_a = randint(- 2000, -1000)
x_a1 = randint(20, 650)
y_a1 = randint(- 2000, -1000)
x_m = -50
y_m = randint(20, 1000)
x_m1 = -50
y_m1 = randint(20, 1000)
x_m2 = -50
y_m2 = randint(20, 1000)
x_v = randint(20, 1000)
y_v = randint(-11000, -10000)
x_avidoc = 22
y_avidoc = 80

x_tiro_alien = -100
y_tiro_alien = -100
x_tiro_alien1 = -100
y_tiro_alien1 = -100

x_tiro_chefao1 = -100
y_tiro_chefao1 = -100
x_tiro_chefao2 = -100
y_tiro_chefao2 = -100
x_tiro_chefao3 = -100
y_tiro_chefao3 = -100
x_tiro_chefao4 = -100
y_tiro_chefao4 = -100
x_tiro_chefao5 = -100
y_tiro_chefao5 = -100
x_tiro_chefao6 = -100
y_tiro_chefao6 = -100

fundo = pygame.image.load('estrelas.png')
fundo2 = pygame.image.load('estrelas.png')

nav = pygame.image.load('nave02.png')

navenemigo = pygame.image.load('enemigo.png')
navenemigo2 = pygame.image.load('enemigo.png')

triggered = False
triggered1 = False
ta = False
ta1 = False
SOM = True
tiro_chefao1 = False
tiro_chefao2 = False
tiro_chefao3 = False
tiro_chefao4 = False
tiro_chefao5 = False
tiro_chefao6 = False


meteor = pygame.image.load('meteoro1.png')
meteor2 = pygame.image.load('meteoro2.png')
meteor3 = pygame.image.load('meteoro3.png')
meteor5 = pygame.image.load('meteoro5.png')
meteor6 = pygame.image.load('meteoro6.png')
meteor7 = pygame.image.load('meteoro7.png')

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('meteoro1.png'))
        self.sprites.append(pygame.image.load('meteoro2.png'))
        self.sprites.append(pygame.image.load('meteoro3.png'))
        self.sprites.append(pygame.image.load('meteoro5.png'))
        self.sprites.append(pygame.image.load('meteoro6.png'))
        self.sprites.append(pygame.image.load('meteoro7.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 10000

        self.animar = False

    def explidir(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.4
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

pontos = 0
fase = 1
vidas = 3
vidas_do_chefao = 25
vidas_do_alien = 6
vidas_do_alien1 = 6

fonte = pygame.font.SysFont('arial', 40, True, True)
fonte2 = pygame.font.SysFont('arial', 40, True, True)
avisos = pygame.font.SysFont('arial', 15, True, True)
aviso2 = pygame.font.SysFont('arial', 15, True, True)
gameover = pygame.font.SysFont('arial', 80, True, False)
clikR = pygame.font.SysFont('arial', 14, True, True)
vida0 = pygame.font.SysFont('arial', 40, True, True)
fase1 = pygame.font.SysFont('arial', 40, True, True)
avisodechefao = pygame.font.SysFont('arial', 40, True, True)
anonovo = pygame.font.SysFont('arial', 80, True, True)

vidadoa = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((largura, altura)) #tela do jogo
pygame.display.set_caption('Ataque Alienígena')#nome do jogo
morreu = False
relogio = pygame.time.Clock()

def reiniciar_jogo():
    global pontos, vidas, y, y_m, y_m1, y_m2, x, x_a, y_a1, x_a1, x_m, x_m1, x_m2, y_a, morreu, x_tiro, y_tiro, triggered, x_tiro_alien, y_tiro_alien, x_tiro_alien1, y_tiro_alien1, ta1, ta, x_v, y_v, y_chefao, vidas_do_alien, vidas_do_alien1, fase, vidas_do_chefao, y_chefao, x_chefao, y_chefao
    pontos = 0
    vidas = 3
    fase = 1
    y = 400
    x = 450
    x_v = randint(20, 1000)
    y_v = randint(-11000, -10000)
    y_m = - 500
    x_m = - 200
    y_m1 = - 500
    x_m1 = - 200
    y_m2 = - 500
    x_m2 = - 200
    x_chefao = 330
    y_chefao = -500
    y_a = randint(-5000, -3000)
    y_a = y_a + 4
    x_tiro = x + 25
    y_tiro = y
    y_chefao = -500
    x_chefao = 330
    x_tiro_alien = x_a
    x_tiro_alien1 = x_a1
    y_tiro_alien = y_a
    y_tiro_alien1 = y_a1
    vidas_do_alien = 6
    vidas_do_alien1 = 6
    vidas_do_chefao = 25
    ta1 = False
    ta = False
    morreu = False
    triggered = False

running = True
while running:
    tela.fill((0, 0, 0))# para limpar onde obj passa

    vida00 = 'VIDAS: 0'
    mesagem = f'VIDA: {vidas}'
    mesagem2 = f'PONTOS: {pontos}'
    aviso = f'Você está com {vidas} vidas pegue mais esferas azul!'
    avis2 = 'Cuidado você está com uma vida!!'
    gameove = 'GAME OVER'
    gameoveavi = 'Clique R para reiniciar o jogo'
    fases = f'FASE: {fase}'
    avisodechefao1 = f'CHEFÃO'
    anonovo1  = 'Feliz ano novo'

    vidadoaa = f'vidas_do_alien --> {vidas_do_alien}, vidas_do_alien1 --> {vidas_do_alien1}'

    texto = fonte.render(mesagem, True, (255, 255, 255))
    texto2 = fonte2.render(mesagem2, True, (255, 255, 255))
    avis = avisos.render(aviso, True, (200, 200, 0))
    avis2 = aviso2.render(avis2, True, (255, 0, 0))
    gov = gameover.render(gameove, False, (255, 0, 0))
    avidover = clikR.render(gameoveavi, False, (200, 200, 0))
    vida000 = vida0.render(vida00, False, (255, 255, 255))
    fase11 = fase1.render(fases, True, (255, 255, 255))
    avisodec = avisodechefao.render(avisodechefao1, True, (255, 0, 0))
    vidadoaaa = vidadoa.render(vidadoaa, True, (255, 255, 255))
    anonovo0 = anonovo.render(anonovo1, True, (255, 0, 0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            x = x - 27
            if not triggered:
                x_tiro = x_tiro - 27
        if pygame.key.get_pressed()[K_d]:
            x = x + 27
            if not triggered:
                x_tiro = x_tiro + 27
        if pygame.key.get_pressed()[K_w]:
            y = y - 27
            if not triggered:
                y_tiro = y_tiro - 27
        if pygame.key.get_pressed()[K_s]:
            y = y + 27
            if not triggered:
                y_tiro = y_tiro + 27
        if pygame.key.get_pressed()[K_SPACE]:
            triggered = True
            if triggered == True:
                if y_tiro < 0:
                    triggered = False
                    y_tiro = y_tiro + 10
                if y_tiro < 0:
                    y_tiro = y
                    x_tiro = x + 25
                if SOM == True:
                    somdotirodanave.play()
        if pygame.key.get_pressed()[K_SPACE]:
            if triggered == True:
                triggered1 = True
                if triggered1 == True:
                    if y_tiro1 < 0:
                        triggered1 = False
                        y_tiro1 = y_tiro1 + 10
                    if y_tiro1 < 0:
                        y_tiro1 = y
                        x_tiro1 = x + 25
                    if SOM == True:
                        somdotirodanave.play()


        if pygame.key.get_pressed()[K_o]:
            SOM = False
        if pygame.key.get_pressed()[K_i]:
            SOM = True
        if pygame.key.get_pressed()[K_q]:
            if pygame.key.get_pressed()[K_e]:
                if pygame.key.get_pressed()[K_p]:
                    if pygame.key.get_pressed()[K_0]:
                        vidas = vidas + 999
    if triggered == True:
        y_tiro = y_tiro - 10

    if triggered1 == True:
        y_tiro1 = y_tiro1 - 10

    tela.blit(fundo, (x_fun2, y_fun2))

    if y_fun2 >= altura + 100:
        y_fun2 = 0
        x_fun2 = 0
    if fase == 1:
        y_fun2 = y_fun2 + 0.1
    if fase == 2:
        y_fun2 = y_fun2 + 0.2
    if fase == 3:
        y_fun2 = y_fun2 + 0.3
    if fase == 4:
        y_fun2 = y_fun2 + 0.4
    if fase == 5:
        y_fun2 = y_fun2 + 0.4
    if fase == 6:
        y_fun2 = y_fun2 + 0.4
    if y_fun2 > 700:
        y_fun2 = -700

    tela.blit(fundo2, (x_fun, y_fun))
    if y_fun >= altura + 100:
        y_fun = 0
        x_fun = 0
    if fase == 1:
        y_fun = y_fun + 0.1
    if fase == 2:
        y_fun = y_fun + 0.2
    if fase == 3:
        y_fun = y_fun + 0.3
    if fase == 4:
        y_fun = y_fun + 0.4
    if fase == 5:
        y_fun = y_fun + 0.4
    if fase == 6:
        y_fun = y_fun + 0.4
    if y_fun > 700:
        y_fun = -700

    tela.blit(texto2, (30, 40))
    tela.blit(texto, (650, 40))
    tela.blit(fase11, (30, 600))
    #tela.blit(vidadoaaa, (500, 400))
    #tela.blit(anonovo0, (250, 390))
    vida = pygame.draw.circle(tela, (255, 0, 0), (x_v, y_v), 14)

    tiro = pygame.draw.circle(tela, (0, 100, 200), (x_tiro, y_tiro), 14)
    tiro1 = pygame.draw.circle(tela, (0, 100, 200), (x_tiro1, y_tiro1), 14)

    if pontos >= 1000:
        y_chefao = y_chefao + 2
        if y_chefao == -10:
            tiro_chefao1 = True
            tiro_chefao2 = True
            tiro_chefao3 = True
            tiro_chefao4 = True
            tiro_chefao5 = True
            tiro_chefao6 = True
            y_chefao = y_chefao - 2
            tela.blit(avisodec, (x_avidoc, y_avidoc))

    tiro_chefa01 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao1, y_tiro_chefao1), 25)
    if x_tiro_chefao1 > 1100:
        tiro_chefao1 = False
    if x_tiro_chefao1 < -20:
        tiro_chefao1 = False
    if y_tiro_chefao1 > 900:
        tiro_chefao1 = False

    tiro_chefa02 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao2, y_tiro_chefao2), 25)
    if x_tiro_chefao2 > 1100:
        tiro_chefao2 = False
    if x_tiro_chefao2 < -20:
        tiro_chefao2 = False
    if y_tiro_chefao2 > 900:
        tiro_chefao2 = False

    tiro_chefa03 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao3, y_tiro_chefao3), 25)
    if x_tiro_chefao3 > 1100:
        tiro_chefao3 = False
    if x_tiro_chefao3 < -20:
        tiro_chefao3 = False
    if y_tiro_chefao3 > 900:
        tiro_chefao3 = False

    tiro_chefa04 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao4, y_tiro_chefao4), 25)
    if x_tiro_chefao4 > 1100:
        tiro_chefao4 = False
    if x_tiro_chefao4 < -20:
        tiro_chefao4 = False
    if y_tiro_chefao4 > 900:
        tiro_chefao4 = False

    tiro_chefa05 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao5, y_tiro_chefao5), 25)
    if tiro_chefao5 == False:
        x_tiro_chefao5 = x_chefao + 150
        y_tiro_chefao5 = y_chefao
        tcf5 = randint(-5, 5)
    if x_tiro_chefao5 > 1100:
        tiro_chefao5 = False
    if x_tiro_chefao5 < -20:
        tiro_chefao5 = False
    if y_tiro_chefao5 > 900:
        tiro_chefao5 = False

    tiro_chefa06 = pygame.draw.circle(tela, (255, 32, 0), (x_tiro_chefao6, y_tiro_chefao6), 25)
    if x_tiro_chefao6 > 1100:
        tiro_chefao6 = False
    if x_tiro_chefao6 < -20:
        tiro_chefao6 = False
    if y_tiro_chefao6 > 900:
        tiro_chefao6 = False

    tiro_alien = pygame.draw.circle(tela, (255, 0, 0), (x_tiro_alien, y_tiro_alien), 19)
    tiro_alien1 = pygame.draw.circle(tela, (255, 0, 0), (x_tiro_alien1, y_tiro_alien1), 19)
    chefao = pygame.draw.rect(tela, (0, 255, 0), (x_chefao, y_chefao, 300, 70))

    if tiro_chefao1 == True:
        y_tiro_chefao1 = y_tiro_chefao1 + 2
        x_tiro_chefao1 = x_tiro_chefao1 + tcf1
    if tiro_chefao2 == True:
        y_tiro_chefao2 = y_tiro_chefao2 + 2
        x_tiro_chefao2 = x_tiro_chefao2 + tcf2
    if tiro_chefao3 == True:
        y_tiro_chefao3 = y_tiro_chefao3 + 2
        x_tiro_chefao3 = x_tiro_chefao3 + tcf3
    if tiro_chefao4 == True:
        y_tiro_chefao4 = y_tiro_chefao4 + 2
        x_tiro_chefao4 = x_tiro_chefao4 + tcf4
    if tiro_chefao5 == True:
        y_tiro_chefao5 = y_tiro_chefao5 + 2
        x_tiro_chefao5 = x_tiro_chefao5 + tcf5
    if tiro_chefao6 == True:
        y_tiro_chefao6 = y_tiro_chefao6 + 2
        x_tiro_chefao6 = x_tiro_chefao6 + tcf6

    alien = pygame.draw.rect(tela, (0, 0, 0), (x_a, y_a, 110, 20))
    if y_a >= altura + 100:
        y_a = randint(-17000, -10000)
        x_a = randint(25, 900)
    y_a = y_a + 4
    if y_a > 180:
        y_a = y_a - 4
        x_a = x_a + 3
        ta = True
    if x_a > 1030:
         x_a = -150

    alien2 = pygame.draw.rect(tela, (0, 0, 0), (x_a1, y_a1, 110, 20))
    if y_a1 >= altura + 100:
        y_a1 = randint(-17000, -10000)
        x_a1 = randint(25, 900)
    y_a1 = y_a1 + 4
    if y_a1 > 100:
        y_a1 = y_a1 - 4
        x_a1 = x_a1 - 3
        ta1 = True
    if x_a1 < -150:
        x_a1 = 1050

    vida_estra = pygame.draw.circle(tela, (0, 0, 255), (x_v, y_v), 14)
    if y_v >= altura + 100:
        y_v = randint(-17000, -10000)
        x_v = randint(10, 1000)
    y_v = y_v + 3

    if y_a > 180:
        x_tiro_alien = x_a + 55
        y_tiro_alien = y_a + 20

    if y_a1 > 100:
        x_tiro_alien1 = x_a1 + 55
        y_tiro_alien1 = y_a1 + 20

    if ta == False:
        x_tiro_alien = x_a + 55
        y_tiro_alien = y_a + 20

    if ta1 == False:
        x_tiro_alien1 = x_a1 + 55
        y_tiro_alien1 = y_a1 + 20

    if fase == 1:
        if ta == True:
            y_tiro_alien = y_tiro_alien + 6

        if ta1 == True:
            y_tiro_alien1 = y_tiro_alien1 + 6

    if fase == 2:
        if ta == True:
            y_tiro_alien = y_tiro_alien + 7

        if ta1 == True:
            y_tiro_alien1 = y_tiro_alien1 + 7

    if fase == 3:
        if ta == True:
            y_tiro_alien = y_tiro_alien + 8

        if ta1 == True:
            y_tiro_alien1 = y_tiro_alien1 + 8

    if fase == 4:
        if ta == True:
            y_tiro_alien = y_tiro_alien + 9

        if ta1 == True:
            y_tiro_alien1 = y_tiro_alien1 + 9

    if fase == 5:
        if ta == True:
            y_tiro_alien = y_tiro_alien + 10

        if ta1 == True:
            y_tiro_alien1 = y_tiro_alien1 + 10

    if y_tiro_alien > randint(700, 3000):
        x_tiro_alien = x_a + 55
        y_tiro_alien = y_a + 20
        ta = False

    if y_tiro_alien1 > randint(700, 3000):
        x_tiro_alien1 = x_a1 + 55
        y_tiro_alien1 = y_a1 + 20
        ta1 = False

    nave = pygame.draw.rect(tela, (0, 0, 0), (x, y, 50, 60))

    met = pygame.draw.circle(tela, (0, 0, 0), (x_m, y_m), 35)
    if y_m >= altura + 100:
        y_m = randint(-2000, -1000)
        x_m = randint(0, 1020)

    met1 = pygame.draw.circle(tela, (0, 0, 0), (x_m1, y_m1), 35)
    if y_m1 >= altura + 100:
        y_m1 = randint(-2000, -1000)
        x_m1 = randint(0, 1020)

    met2 = pygame.draw.circle(tela, (0, 0, 0), (x_m2, y_m2), 35)
    if y_m2 >= altura + 100:
        y_m2 = randint(-2000, -1000)
        x_m2 = randint(0, 1020)

    fasedojogo(1, 10)

    fasedojogo(2, 11)

    fasedojogo(3, 12)

    fasedojogo(4, 13)

    fasedojogo(5, 14)

    colisaodetiro(alien, vidas_do_alien)

    colisaodetiro(alien2, vidas_do_alien1)

    if tiro1.colliderect(alien):
        vidas_do_alien = vidas_do_alien - 1
        triggered1 = False

    if tiro1.colliderect(alien2):
        vidas_do_alien1 = vidas_do_alien1 - 1
        triggered1 = False

    if nave.colliderect(met):
        if SOM == True:
            som.play()
        vidas = vidas - 1
        y = 8999
        x_tiro = 480
        y_tiro = 480
        triggered = False
        if triggered == False:
            x_tiro = x + 25
            y_tiro = y + 25
        triggered = False
        sapo.explidir()

    if nave.colliderect(met1):
        if SOM == True:
            som.play()
        vidas = vidas - 1
        y = 8999
        x_tiro = 480
        y_tiro = 480
        triggered = False
        if triggered == False:
            x_tiro = x + 25
            y_tiro = y + 25
        triggered = False
        sapo.explidir()

    if nave.colliderect(tiro_alien):
        vidas = vidas - 1
        ta = False
        y = 8999

    if nave.colliderect(tiro_alien1):
        vidas = vidas - 1
        ta = False
        y = 8999

    tirochefao(tiro_chefa01)
    tirochefao(tiro_chefa02)
    tirochefao(tiro_chefa03)
    tirochefao(tiro_chefa04)
    tirochefao(tiro_chefa05)
    tirochefao(tiro_chefa06)

    if nave.colliderect(met2):
        if SOM == True:
            som.play()
        vidas = vidas - 1
        y = 8999
        x_tiro = 480
        y_tiro = 480
        triggered = False
        if triggered == False:
            x_tiro = x + 25
            y_tiro = y + 25
        triggered = False

    if y == 8999:
        x = 450
        y = 450
        y_m = randint(-2000, -1000)
        y_m1 = randint(-2000, -1000)
        y_m2 = randint(-2000, -1000)
        x_m = randint(10, 1000)
        x_m1 = randint(10, 1000)
        x_m2 = randint(10, 1000)
        x_a = randint(20, 650)
        y_a = randint(- 2000, -1000)
        x_a1 = randint(20, 650)
        y_a1 = randint(- 2000, -1000)
        x_tiro_alien = x_a
        x_tiro_alien1 = x_a1
        y_tiro_alien = y_a
        y_tiro_alien1 = y_a1
        y_chefao = -1000
        x_v = randint(20, 1000)
        y_v = randint(-11000, -10000)
        tiro_chefao1 = False
        tiro_chefao2 = False
        tiro_chefao3 = False
        tiro_chefao4 = False
        tiro_chefao5 = False
        tiro_chefao6 = False
        ta1 = False
        ta = False
        triggered = False
        triggered1 = False
        sleep(2)


    tirocolide(met, y_m, x_m)
    tirocolide(met1, y_m1, x_m1)
    tirocolide(met2, y_m2, x_m2)

    if tiro1.colliderect(met):
        y_m = - 3000
        x_m = randint(10, 1000)
        pontos = pontos + 100
        triggered1 = False
        if triggered1 == False:
            x_tiro1 = x + 25
            y_tiro1 = y + 25

    if tiro1.colliderect(met1):
        y_m1 = - 3000
        x_m1 = randint(10, 1000)
        pontos = pontos + 100
        triggered1 = False
        if triggered1 == False:
            x_tiro1 = x + 25
            y_tiro1 = y + 25

    if tiro1.colliderect(met2):
        y_m2 = - 3000
        x_m2 = randint(10, 1000)
        pontos = pontos + 100
        triggered1 = False
        if triggered1 == False:
            x_tiro1 = x + 25
            y_tiro1 = y + 25

    if tiro.colliderect(chefao):
        vidas_do_chefao = vidas_do_chefao - 1
        triggered = False
        if triggered == False:
            x_tiro = x + 25
            y_tiro = y + 25

    if tiro1.colliderect(chefao):
        vidas_do_chefao = vidas_do_chefao - 1
        triggered1 = False
        if triggered1 == False:
            x_tiro1 = x + 25
            y_tiro1 = y + 25

    if nave.colliderect(vida_estra):
        vidas = vidas + 1
        x_v = 3000

    tela.blit(nav, (x - 101, y - 80))
    tela.blit(navenemigo, (x_a - 18, y_a - 25))
    tela.blit(navenemigo2, (x_a1 - 18, y_a1 - 25))
    tela.blit(meteor, (x_m - 240, y_m - 120))
    tela.blit(meteor, (x_m1 - 240, y_m1 - 120))
    tela.blit(meteor, (x_m2 - 240, y_m2 - 120))

    if vidas == 2:
        tela.blit(avis, (650, 80))

    if vidas == 1:
        tela.blit(avis2, (650, 80))

    if vidas == 0:
        morreu = True
        while morreu:
            vidas = 0
            tela.blit(fundo, (x_fun2, y_fun2))

            if y_fun2 >= altura + 100:
                y_fun2 = 0
                x_fun2 = 0
            y_fun2 = y_fun2 + 0.01
            if y_fun2 > 700:
                y_fun2 = -700

            tela.blit(fundo2, (x_fun, y_fun))
            if y_fun >= altura + 100:
                y_fun = 0
                x_fun = 0
            y_fun = y_fun + 0.01
            if y_fun > 700:
                y_fun = -700
            tela.blit(vida000, (650, 40))
            tela.blit(texto2, (30, 40))
            tela.blit(gov, (250, 300))
            tela.blit(avidover, (250, 390))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            pygame.display.flip()

    if vidas == -1:
        morreu = True
        while morreu:
            vidas = 0
            tela.blit(fundo, (x_fun2, y_fun2))

            if y_fun2 >= altura + 100:
                y_fun2 = 0
                x_fun2 = 0
            y_fun2 = y_fun2 + 0.1
            if y_fun2 > 700:
                y_fun2 = -700

            tela.blit(fundo2, (x_fun, y_fun))
            if y_fun >= altura + 100:
                y_fun = 0
                x_fun = 0
            y_fun = y_fun + 0.1
            if y_fun > 700:
                y_fun = -700
            tela.blit(vida000, (650, 40))
            tela.blit(texto2, (30, 40))
            tela.blit(gov, (250, 300))
            tela.blit(avidover, (250, 390))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            pygame.display.flip()

    if vidas == -2:
        morreu = True
        while morreu:
            vidas = 0
            tela.blit(fundo, (x_fun2, y_fun2))

            if y_fun2 >= altura + 100:
                y_fun2 = 0
                x_fun2 = 0
            y_fun2 = y_fun2 + 0.1
            if y_fun2 > 700:
                y_fun2 = -700

            tela.blit(fundo2, (x_fun, y_fun))
            if y_fun >= altura + 100:
                y_fun = 0
                x_fun = 0
            y_fun = y_fun + 0.1
            if y_fun > 700:
                y_fun = -700
            tela.blit(vida000, (650, 40))
            tela.blit(texto2, (30, 40))
            tela.blit(gov, (250, 300))
            tela.blit(avidover, (250, 390))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            pygame.display.flip()

    if vidas_do_alien == 0:
        x_a = randint(20, 650)
        y_a = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien = vidas_do_alien + 6

        if fase == 2:
            vidas_do_alien = vidas_do_alien + 9

        if fase == 3:
            vidas_do_alien = vidas_do_alien + 12

        if fase == 4:
            vidas_do_alien = vidas_do_alien + 15

        if fase == 5:
            vidas_do_alien = vidas_do_alien + 18
        pontos = pontos + 200

    if vidas_do_alien == -1:
        x_a = randint(20, 650)
        y_a = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien = vidas_do_alien + 6

        if fase == 2:
            vidas_do_alien = vidas_do_alien + 9

        if fase == 3:
            vidas_do_alien = vidas_do_alien + 12

        if fase == 4:
            vidas_do_alien = vidas_do_alien + 15

        if fase == 5:
            vidas_do_alien = vidas_do_alien + 18
        pontos = pontos + 200

    if vidas_do_alien == -2:
        x_a = randint(20, 650)
        y_a = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien = vidas_do_alien + 6

        if fase == 2:
            vidas_do_alien = vidas_do_alien + 9

        if fase == 3:
            vidas_do_alien = vidas_do_alien + 12

        if fase == 4:
            vidas_do_alien = vidas_do_alien + 15

        if fase == 5:
            vidas_do_alien = vidas_do_alien + 18
        pontos = pontos + 200

    if vidas_do_alien == -3:
        x_a = randint(20, 650)
        y_a = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien = vidas_do_alien + 6

        if fase == 2:
            vidas_do_alien = vidas_do_alien + 9

        if fase == 3:
            vidas_do_alien = vidas_do_alien + 12

        if fase == 4:
            vidas_do_alien = vidas_do_alien + 15

        if fase == 5:
            vidas_do_alien = vidas_do_alien + 18
        pontos = pontos + 200

    if vidas_do_alien1 == 0:
        x_a1 = randint(20, 650)
        y_a1 = randint(- 6000, -5000)
        if fase == 1:
            vidas_do_alien1 = vidas_do_alien1 + 6

        if fase == 2:
            vidas_do_alien1 = vidas_do_alien1 + 9

        if fase == 3:
            vidas_do_alien1 = vidas_do_alien1 + 12

        if fase == 4:
            vidas_do_alien1 = vidas_do_alien1 + 15

        if fase == 5:
            vidas_do_alien1 = vidas_do_alien1 + 18
        pontos = pontos + 200

    gameroveralien1(-1)

    gameroveralien1(-2)

    gameroveralien1(-3)

    gameoverchefao(0)

    gameoverchefao(-1)

    gameoverchefao(-2)


    if y_chefao == 100000:
        pontos = pontos + 1500
        vidas_do_chefao = vidas_do_chefao + 1
        if fase == 1:
            fase = fase + 1
        x_avidoc = -300
        tiro_chefao1 = False
        tiro_chefao2 = False
        tiro_chefao3 = False
        tiro_chefao4 = False
        tiro_chefao5 = False
        tiro_chefao6 = False
        y_chefao = 200000
        x_chefao = 20000

    if x > 970:
        x = 970
    if x < 20:
        x = 20
    if y < 250:
        y = 250
    if y > 620:
        y = 620

    if x_tiro > 990:
        x_tiro = 990
    if x_tiro < 20:
        x_tiro = 20
    if y_tiro > 620:
        y_tiro = 620

    if triggered == False:
        x_tiro = x + 25
        y_tiro = y + 25

    if triggered1 == False:
        x_tiro1 = x + 25
        y_tiro1 = y + 25

    if tiro_chefao1 == False:
        x_tiro_chefao1 = x_chefao + 150
        y_tiro_chefao1 = y_chefao
        tcf1 = randint(-5, 5)

    if tiro_chefao2 == False:
        x_tiro_chefao2 = x_chefao + 150
        y_tiro_chefao2 = y_chefao
        tcf2 = randint(-5, 5)

    if tiro_chefao3 == False:
        x_tiro_chefao3 = x_chefao + 150
        y_tiro_chefao3 = y_chefao
        tcf3 = randint(-5, 5)

    if tiro_chefao4 == False:
        x_tiro_chefao4 = x_chefao + 150
        y_tiro_chefao4 = y_chefao
        tcf4 = randint(-5, 5)

    if tiro_chefao5 == False:
        x_tiro_chefao5 = x_chefao + 150
        y_tiro_chefao5 = y_chefao
        tcf5 = randint(-5, 5)

    if tiro_chefao6 == False:
        x_tiro_chefao6 = x_chefao + 150
        y_tiro_chefao6 = y_chefao
        tcf6 = randint(-5, 5)

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
    relogio.tick(60)#velocidade do jogo


pygame.quit()
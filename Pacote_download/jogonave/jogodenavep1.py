from time import sleep
from random import randint
import pygame
from pygame.locals import *
from sys import exit
import os
#O projeto não está pronto então está parte do código não irá funcionar.
pygame.init()

largura = 1020
altura = 700

fps = 30

preto = (0, 0, 0)
azul = (0, 0, 255)

fonte = 'arial'

x = 700
y = 600

class Game:
    def __init__(self):
        #cria a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Ataque Alienígena')
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(fonte)
        self.carregar_aquirvos()

    def jogop1(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        self.jogando = True
        while self.jogando:
            self.relogio.tick(fps)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    if self.jogando:
                        self.jogando = False
                    self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(preto)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_aquirvos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        #self.spritesheet = os.path.join(diretorio_imagens, 'logodojogo.png')
        self.logo_jogo = os.path.join(diretorio_imagens, 'logodojogo.png')
        self.logo_jogo = pygame.image.load(self.logo_jogo).convert()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)                                    
        self.tela.blit(texto, texto_rect)
    def mostrar_tela_start(self):
        self.mostrar_texto('pressione uma tecla para jogar', 32, azul)

g = Game()

g.mostrar_tela_start()


while g.esta_rodando:
    g.jogop1()




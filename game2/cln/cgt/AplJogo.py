from random import randint
import pygame
from cln.cdp.EntradaUsuario import EntradaUsuario
from cln.cdp.Obstaculo import Obstaculo
from cln.cdp.Personagem import Personagem

__author__ = 'dell'


class AplJogo:

    def __init__(self):
        self.personagem = Personagem(350, 250)
        self.obstaculo = Obstaculo(700, randint(0, 445))
        #TODO trocar esses objetos estaticos e gerar aleatoriamente
        self.obstaculo2 = Obstaculo(700, randint(0, 445))
        self.pontos = 0
        self.pontosatual = 0
        self.fimdejogo = False
        self.desceu = True

    def config(self):
        self.clock = pygame.time.Clock()
        self.entradas = EntradaUsuario()

    def player_input(self):
        for event in pygame.event.get():
            self.entradas.reset()
            if event.type == pygame.QUIT:
                self.entradas.quit_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entradas.quit_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.diminui_velocidade()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.aumenta_velocidade()
            pygame.key.set_repeat(1)

    def aumenta_velocidade(self):
        self.personagem.velocidadey = 10

    def diminui_velocidade(self):
        self.personagem.velocidadey = -15

    def movimenta_personagem(self):
        self.personagem.modifica_posicao(self.personagem.posicao.eixox, self.personagem.posicao.eixoy + self.personagem.velocidadey)

    def movimenta_obstaculo_horizontalmente(self):
        self.obstaculo.modifica_posicao(self.obstaculo.posicao.eixox - self.obstaculo.velocidadex , self.obstaculo.posicao.eixoy)
        self.obstaculo2.modifica_posicao(self.obstaculo2.posicao.eixox - self.obstaculo2.velocidadex , self.obstaculo2.posicao.eixoy)

    def movimenta_obstaculo_verticalmente(self):
        if self.obstaculo.posicao.eixoy <= 0:
            self.desceu = True
        elif self.obstaculo.posicao.eixoy >= 450:
            self.desceu = False

        if self.desceu == True:
            self.obstaculo.desce()
        elif self.desceu == False:
            self.obstaculo.sobe()

        #por enquanto gera "obstaculos estaticos", futuramente serao gerados automaticamente e aleatoriamente
        if self.obstaculo2.posicao.eixoy <= 0:
            self.desceu = True
        elif self.obstaculo2.posicao.eixoy >= 450:
            self.desceu = False

        if self.desceu == True:
            self.obstaculo2.desce()
        elif self.desceu == False:
            self.obstaculo2.sobe()

    def verifica_limite_da_tela(self):
        self.personagem.atingiu_limite_da_tela()

    def incrementa_pontuacao(self):
        if self.personagem.posicao.eixox > self.obstaculo.posicao.eixox and self.personagem.posicao.eixox < self.obstaculo.posicao.eixox+10:
            self.pontos += 1

    def proximo_obstaculo(self):
        #para aparecer varios obstaculos
        if self.obstaculo.posicao.eixox < -80:
            self.obstaculo.posicao.eixox = 700
            self.obstaculo.posicao.eixoy = randint(0,500)
            self.obstaculo2.posicao.eixox = 600
            self.obstaculo2.posicao.eixoy = randint(0,500)

    def verifica_colisao(self, rect1, rect2):
        if rect1.colliderect(rect2) and self.pontos != self.pontosatual:
            self.personagem.vida -= 1
            self.pontosatual = self.pontos

    def verifica_qtd_de_vidas(self):
        if self.personagem.acabou_vida():
            self.fimdejogo = True
            self.personagem.velocidadey = 0
            self.obstaculo.velocidadex = 0
            self.obstaculo2.velocidadex = 0

    def jogar(self):
        self.player_input()
        self.incrementa_pontuacao()
        self.movimenta_personagem()
        self.movimenta_obstaculo_horizontalmente()
        self.movimenta_obstaculo_verticalmente()
        self.proximo_obstaculo()
        self.verifica_limite_da_tela()
        self.verifica_qtd_de_vidas()
        if self.entradas.quit_pressed:
            exit(0)

        pygame.display.flip()
        self.clock.tick(60)


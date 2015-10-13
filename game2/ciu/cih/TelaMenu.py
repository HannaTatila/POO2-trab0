import pygame, os

__author__ = 'dell'


class TelaMenu:

    def __init__(self):
        self.branco = (255,255,255)
        self.preto = (0,0,0)
        self.ceu = (192,217,217)
        pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Mar&moto")

    def exibe_imagem(self, caminhoimagem, nomeimagem, posicao):
        imagem = pygame.image.load(os.path.join(caminhoimagem, nomeimagem))
        self.tela.blit(imagem, (posicao.eixox,posicao.eixoy))
        return imagem

    def exibe_texto_menu(self, texto, x, y):
        fonte = pygame.font.SysFont("Agency FB", 35, False, False)
        t = fonte.render(texto, True, self.preto)
        self.tela.blit(t, (x, (self.tamanhotelay/2)+y))

    def exibe_texto_menu2(self, texto, x, y):
        fonte = pygame.font.SysFont("Agency FB", 25, False, False)
        t = fonte.render(texto, True, (80,80,80))
        self.tela.blit(t, (x, (self.tamanhotelay/2)+y))
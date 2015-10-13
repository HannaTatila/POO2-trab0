from ciu.cci.Controlador import Controlador
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.Posicao import Posicao
import pygame
from pygame import KEYDOWN, KEYUP
from pygame import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_RETURN, K_ESCAPE

__author__ = 'dell'


class ControladorMenu():

    def __init__(self):
        pygame.init()
        self.telamenu = TelaMenu()
        self.controlador = Controlador()
        self.caminhoimagem = "C:/Users/dell/PycharmProjects/game2/recursos/imagem"


    def exibir_tela_menu(self):
        self.telamenu.exibe_imagem(self.caminhoimagem, "backmenu.jpg", Posicao(0,0))

    #TODO refatorar toda a parte do menu
    def fixo(self):
        self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(45, 266))

    def selecao(self, menuselecao):
        ## TELA 1
        if menuselecao == 1:
            self.telamenu.exibe_texto_menu("INICIAR", 102,  35)
            self.telamenu.exibe_texto_menu2("CADASTRAR", 102,  75)
            self.telamenu.exibe_texto_menu2("CONFIGURACOES", 102,  105)
            self.telamenu.exibe_texto_menu2("SAIR", 102,  135)

        elif menuselecao == 2:
            self.telamenu.exibe_texto_menu2("INICIAR", 102,  5)
            self.telamenu.exibe_texto_menu("CADASTRAR", 102,  35)
            self.telamenu.exibe_texto_menu2("CONFIGURACOES", 102,  75)
            self.telamenu.exibe_texto_menu2("SAIR", 102,  105)

        elif menuselecao == 3:
            self.telamenu.exibe_texto_menu2("INICIAR", 102,  -25)
            self.telamenu.exibe_texto_menu2("CADASTRAR", 102,  5)
            self.telamenu.exibe_texto_menu("CONFIGURACOES", 102,  35)
            self.telamenu.exibe_texto_menu2("SAIR", 102,  75)

        elif menuselecao == 4:
            self.telamenu.exibe_texto_menu2("INICIAR", 102,  -55)
            self.telamenu.exibe_texto_menu2("CADASTRAR", 102,  -25)
            self.telamenu.exibe_texto_menu2("CONFIGURACOES", 102,  5)
            self.telamenu.exibe_texto_menu("SAIR", 102,  35)

        ## REGRAS DA TELA 1:
        if menuselecao < 1: #nao incrementar estado se apertar p cima de novo
            menuselecao = 1
        if menuselecao == 5: #nao incrementar estado se apertar p baixo de novo
            menuselecao = 4
        if menuselecao == 13: # PARA, POR ENQUANTO, NAO FUNCIONAR NADA EM CONFIGURACOES
            menuselecao = 3
        if menuselecao == 14: # se escolher a opcao 'SAIR'
            exit()
        if menuselecao == 12: #se der enter na opcao 'CADASTRAR'
            menuselecao = 200
        if menuselecao == 11:
            #self.telajogo.tela.fill((255,255,255))
            self.controlador.jogo()

        ## TELA 2
        if menuselecao == 200:
            self.telamenu.exibe_texto_menu("NOME: ", 102,  35)
            pygame.draw.rect(self.telamenu.tela, (self.telamenu.branco), (190,280,300,30), 0)
            self.telamenu.exibe_texto_menu2("VOLTAR", 102,  75)
            pygame.display.flip()
            menuselecao = self.cadastrar()
        elif menuselecao == 201:
            self.telamenu.exibe_texto_menu2("NOME:", 102,  5)
            pygame.draw.rect(self.telamenu.tela, (self.telamenu.branco), (170,240,300,30), 0)
            self.telamenu.exibe_texto_menu("VOLTAR", 102,  35)

        ## REGRAS DA TELA 2
        if (menuselecao == 210) | (menuselecao == 199): # por enquanto, so escreve o nome na tela, mas nao persiste os dados
            menuselecao = 200
        if menuselecao == 202: #nao incrementar estado se apertar p baixo de novo
            menuselecao = 201
        if menuselecao == 211: #se clicar em voltar, volta para o menu inical
            menuselecao = 1

        return menuselecao

    def menu(self):
        menuselecao = 1
        while True:
            self.exibir_tela_menu()
            self.fixo()
            menuselecao = self.selecao(menuselecao)
            pygame.display.update()
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
                if e.type == KEYDOWN:
                    if e.key == K_DOWN:
                        menuselecao += 1
                    if e.key == K_UP:
                        menuselecao -= 1
                    if e.key == K_RETURN:
                        menuselecao += 10
                    if e.key == K_ESCAPE:
                        menuselecao -= 10

#---------------------------------------------------- Cadastro

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
              pass


    def imprime_nome(self, nome_corrente, tela):
        nome = ""
        for i in range(len(nome_corrente)):
            nome = nome + nome_corrente[i]

        fonte = pygame.font.SysFont("ARIAL", 24, False, False)
        texto = fonte.render(nome, True, (0,0,0))
        tela.blit(texto, (195,280))
        pygame.display.flip()
        return nome

    def escreve_arquivo(self, nome):
        arq = open("ranking.txt", "a")
        arq.write(nome + " ")

    def cadastrar(self):
        nome_corrente = []
        nome = ""
        while True:
            tecla = self.get_key()
            if tecla == K_RETURN:
                self.escreve_arquivo(nome)
                return 201
            elif tecla <= 127:
                nome_corrente.append(chr(tecla))
                nome = self.imprime_nome(nome_corrente, self.telamenu.tela)





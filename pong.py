import pygame
from pygame.locals import *
from OpenGL.GL import *
import keyboard

LARGURA_JANELA = 640
ALTURA_JANELA = 480

xDaBola = 0
yDaBola = 0
tamanhoDaBola = 15
velocidadeDaBolaEmX = 0.2
velocidadeDaBolaEmY = 0.2
pontosjogador1 = 0
pontosjogador2 = 0
yDoJogador1 = 0
yDoJogador2 = 0

def xDoJogador1():
    return -LARGURA_JANELA / 2 + larguraDosJogadores() / 2

def xDoJogador2():
    return LARGURA_JANELA / 2 - larguraDosJogadores() / 2

def larguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 5 * tamanhoDaBola

def atualizar():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoJogador1, yDoJogador2, pontosjogador1, pontosjogador2

    xDaBola = xDaBola + velocidadeDaBolaEmX
    yDaBola = yDaBola + velocidadeDaBolaEmY

    if (xDaBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador2 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador2 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if (xDaBola - tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador1 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador1 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if yDaBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if xDaBola < -LARGURA_JANELA / 2:
        pontosjogador1 = pontosjogador1 + 1
        xDaBola = 0
        yDaBola = 0
        print(pontosjogador1, pontosjogador2)
    
    if xDaBola > LARGURA_JANELA / 2:
        pontosjogador2 = pontosjogador2 + 1
        xDaBola = 0
        yDaBola = 0
        print(pontosjogador1, pontosjogador2)

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        if (yDoJogador1 + 25) < ALTURA_JANELA / 2:
            yDoJogador1 = yDoJogador1 + 1
        

    if keys[K_s]:
        if (yDoJogador1 - 25) > -ALTURA_JANELA / 2:
            yDoJogador1 = yDoJogador1 - 1

    if keys[K_UP]:
        if (yDoJogador2 + 25) < ALTURA_JANELA / 2:
            yDoJogador2 = yDoJogador2 + 1

    if keys[K_DOWN]:
        if (yDoJogador2 - 25) > -ALTURA_JANELA / 2:
            yDoJogador2 = yDoJogador2 - 1

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)
    desenharRetangulo(xDoJogador1(), yDoJogador1, larguraDosJogadores(), alturaDosJogadores(), 1, 0, 0)
    desenharRetangulo(xDoJogador2(), yDoJogador2, larguraDosJogadores(), alturaDosJogadores(), 0, 0, 1)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()
    pygame.event.pump()
    if keyboard.is_pressed("esc"):
        break

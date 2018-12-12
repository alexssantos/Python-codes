import pygame
import random

pygame.init()
tela = pygame.display.set_mode((1280, 720))

# Colors
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
black = (0, 0, 0)

posX1 = 580  # circle
posY1 = 60

posX2 = 550  # text
posY2 = 55

raioButton = 60
listColider = []


def clickCircle():
    circulo = pygame.draw.circle(
        tela, amarelo, (posX1, posY1), raioButton)
    font = pygame.font.Font(None, 30)
    text = font.render('CLICK', True, vermelho)

    tela.blit(text, (posX2, posY2))  # Print on screen

    for posArea in range(len(listColider)):      # não pegar o ultimo added
            if circulo.colliderect(listColider[posArea]):
                del listColider[posArea]       # Encostou
                redraw()
                break


class retangulo():
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.posX = random.randint(0, 1200)
        self.posY = random.randint(0, 700)
        self.area = pygame.Rect(              # area de colisao
            self.posX, self.posY, self.largura, self.altura)
        self.cor = amarelo

    def desenha(self):
        pygame.draw.rect(tela, self.cor, self.area)


def redraw():
    tela.fill(black)
    for index in range(0, len(listColider)):
        pygame.draw.rect(tela, amarelo, listColider[index])


finish = False
while not finish:

    # update screen by FPS
    pygame.display.update()

    # checar os eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:  # mapeamento Area Click
            if (posX1 - raioButton <= x <= posX1 + raioButton) and (posY1 - raioButton <= y <= posY1 + raioButton):
                retangulo().desenha()
                listColider.append(retangulo().area)
                # não pegar o ultimo added
                for posArea in range(len(listColider)-1):
                    if retangulo().area.colliderect(listColider[posArea]):
                        del listColider[posArea]   # Encostado
                        listColider.pop()       # Encostou
                        redraw()
                        break

        if event.type == pygame.QUIT:
            finish = True

    # pintar a tela a cada ciclo - colider não não funciona sem
    tela.fill(black)
    redraw()
    clickCircle()
    pygame.time.Clock().tick(60)

pygame.display.quit()
pygame.quit()

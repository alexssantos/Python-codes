import pygame
import random

pygame.init()
_screen = pygame.display.set_mode((1280, 720))

# Colors
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
black = (0, 0, 0)

posX1 = 580  # circle
posY1 = 60

posX2 = 550  # text
posY2 = 55

raioButton = 60
listCollider = []


class retangulo():          # Classe Facilita MUITO
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.posX = random.randint(0, 1200)
        self.posY = random.randint(0, 700)
        self.area = pygame.Rect(              # area de colisao
            self.posX, self.posY, self.largura, self.altura)
        self.cor = amarelo

    def desenha(self):
        pygame.draw.rect(_screen, self.cor, self.area)


def clickCircle():
    circulo = pygame.draw.circle(
        _screen, amarelo, (posX1, posY1), raioButton)
    font = pygame.font.Font(None, 30)
    text = font.render('CLICK', True, vermelho)

    _screen.blit(text, (posX2, posY2))  # Print on screen

    for posArea in range(len(listCollider)):      # não pegar o ultimo added
        if circulo.colliderect(listCollider[posArea]):
            del listCollider[posArea]       # Encostou
            redraw()
            break


def redraw():
    _screen.fill(black)
    for index in range(0, len(listCollider)):
        pygame.draw.rect(_screen, amarelo, listCollider[index])


finish = False
while not finish:

    # update screen by FPS
    pygame.display.update()

    # check mouse events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:  # tecla clicada
            if event.key == pygame.K_a:
                posX1 -= 5
                posX2 -= 5
            if event.key == pygame.K_d:
                posX1 += 5
                posX2 += 5
            if event.key == pygame.K_w:
                posY1 -= 5
                posY2 -= 5
            if event.key == pygame.K_s:
                posY1 += 5
                posY2 += 5

        if event.type == pygame.MOUSEBUTTONDOWN:  # mapping Click to click - circle
            if (posX1 - raioButton <= x <= posX1 + raioButton) and (posY1 - raioButton <= y <= posY1 + raioButton):
                retangulo().desenha()
                listCollider.append(retangulo().area)
                # não pegar o ultimo added
                for posArea in range(len(listCollider)-1):
                    if retangulo().area.colliderect(listCollider[posArea]):
                        del listCollider[posArea]   # Encostado
                        listCollider.pop()       # Encostou
                        redraw()
                        break

        if event.type == pygame.QUIT:
            finish = True

    # pintar a _screen a cada ciclo - colider não não funciona sem
    _screen.fill(black)
    redraw()
    clickCircle()
    pygame.time.Clock().tick(60)

pygame.display.quit()
pygame.quit()

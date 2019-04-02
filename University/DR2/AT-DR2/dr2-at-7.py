import pygame
import random

pygame.init()
tela = pygame.display.set_mode((1280, 720))

# Colors
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)

# X
# pygame.draw.line()
# pygame.draw.line()
posList = []


def retangulo():
    x = random.randint(0, 1200)
    y = random.randint(0, 700)

    # Retangulo
    quadrado = pygame.draw.rect(tela, amarelo, (x, y, 50, 50), 3)
    posList.append(quadrado)


finish = False
while not finish:

    # update screen by FPS
    pygame.display.update()

    # checar os eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                retangulo()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[2]:
                retangulo()

        if event.type == pygame.QUIT:
            finish = True

pygame.display.quit()
pygame.quit()

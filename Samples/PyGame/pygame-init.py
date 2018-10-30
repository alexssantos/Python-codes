import pygame

pygame.init()
tela = pygame.display.set_mode((1280, 720))

#Colors
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)

# Squad Args: screen, color, position, fill
pygame.draw.rect(tela, amarelo, (10,10,200,100), 3)
pygame.draw.rect(tela, vermelho, (400,300,50,50))

#Circle Args: screen, color, position, raio, fill
pygame.draw.circle(tela, vermelho, (200,200), 80, 5)
pygame.draw.circle(tela, amarelo, (600,600), 120, 120)


finish = False
while not finish:

    #atualiza 
    pygame.display.update()

    #checar os eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.display.quit()
pygame.quit()
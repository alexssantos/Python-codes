import pygame

pygame.init()
tela = pygame.display.set_mode((1280, 720))

#Colors
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)

# X
# pygame.draw.line()
# pygame.draw.line()

# Retangle
pygame.draw.rect(tela, amarelo, (10,10,200,100), 3)

#Circle 
pygame.draw.circle(tela, amarelo, (600,600), 120, 120)

#triangle
#pygame.draw.polygon(tela, (210,180,140), [[x, y], [x -10, y -10], [x + 10, y - 10]], 5)

finish = False
while not finish:

    #update screen by FPS
    pygame.display.update()

    #checar os eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.display.quit()
pygame.quit()
import pygame

pygame.init()

largura_tela = 1280
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))

finish = False
while not finish:

    #atualiza
    pygame.display.update()

    #checar os 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.display.quit()
pygame.quit()
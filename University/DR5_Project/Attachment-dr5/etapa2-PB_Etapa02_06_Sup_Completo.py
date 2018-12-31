import pygame
import psutil

# Inicializando fontes.
pygame.font.init()
font = pygame.font.Font(None, 32)

preto = (0,0,0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255,255,255)

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

# Cria superf[icies.
s1 = pygame.surface.Surface((largura_tela, altura_tela/3))
s2 = pygame.surface.Surface((largura_tela, altura_tela/3))
s3 = pygame.surface.Surface((largura_tela, altura_tela/3))

# Mostar uso de memória
def mostra_uso_memoria():
  mem = psutil.virtual_memory()
  larg = largura_tela - 2*20
  s1.fill(preto)
  pygame.draw.rect(s1, azul, (20, 50, larg, 70))
  larg = larg*mem.percent/100
  pygame.draw.rect(s1, vermelho, (20, 50, larg, 70))
  total = round(mem.total/(1024*1024*1024),2)
  texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
  text = font.render(texto_barra, 1, branco)
  s1.blit(text, (20, 10))
  tela.blit(s1, (0, 0))

def mostra_uso_cpu():
  capacidade = psutil.cpu_percent(interval=0)
  larg = largura_tela - 2*20
  s2.fill(preto)
  pygame.draw.rect(s2, azul, (20, 50, larg, 70))
  larg = larg*capacidade/100
  pygame.draw.rect(s2, vermelho, (20, 50, larg, 70))
  text = font.render("Uso de CPU:", 1, branco)
  s2.blit(text, (20, 10))
  tela.blit(s2, (0, altura_tela/3))

def mostra_uso_disco():
  disco = psutil.disk_usage('.')
  larg = largura_tela - 2*20
  s3.fill(preto)
  pygame.draw.rect(s3, azul, (20, 50, larg, 70))
  larg = larg*disco.percent/100
  pygame.draw.rect(s3, vermelho, (20, 50, larg, 70))
  total = round(disco.total/(1024*1024*1024), 2)
  texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
  text = font.render(texto_barra, 1, branco)
  s3.blit(text, (20, 10))
  tela.blit(s3, (0, 2*altura_tela/3))

# Cria relógio
clock = pygame.time.Clock()

# Contador de tempo
cont = 60

terminou = False

while not terminou:
  # Checar os eventos do mouse aqui:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          terminou = True
  # Fazer a atualização a cada segundo:
  if cont == 60:
      mostra_uso_memoria()
      #tela.blit(s1, (0, 0))

      mostra_uso_cpu()
      #tela.blit(s2, (0, altura_tela/3))
 
      mostra_uso_disco()
      #tela.blit(s3, (0, 2*altura_tela/3))
      cont = 0
  # Atualiza o desenho na tela
  pygame.display.update()
  # 60 frames por segundo
  clock.tick(60)
  cont = cont + 1
      
# Finaliza a janela
pygame.display.quit()

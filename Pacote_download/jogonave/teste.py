import pygame

# Inicializar o pygame
pygame.init()

# Definir a largura e altura da tela
screen = pygame.display.set_mode((640, 480))

# Criar um relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Definir a taxa de quadros por segundo (FPS)
fps = 60

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica do jogo
    # ...

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a velocidade do jogo a 60 FPS
    clock.tick(fps)

# Finalizar o pygame
pygame.quit()

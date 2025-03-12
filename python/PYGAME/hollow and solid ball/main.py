import pygame

pygame.init()

window = pygame.display.set_mode((400, 300))
window.fill((255, 255, 255))
Green = (0, 255, 0)
pygame.draw.circle(window, Green, (200, 150), 50)
pygame.draw.circle(window, (0, 0, 0), (200, 150), 50, 3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
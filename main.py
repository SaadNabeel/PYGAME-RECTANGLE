import pygame

pygame.init()

window = pygame.display.set_mode((700, 600))

done = False

GREEN = (0, 255, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    window.fill((0, 0, 0))

    
    pygame.draw.rect(window, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(window, GREEN, (300, 300), 50)
    pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

    pygame.display.flip()

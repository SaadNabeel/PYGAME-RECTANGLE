import pygame

pygame.init()

window = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Moving Rectangle")

done = False
GREEN = (0, 255, 0)
x, y = 100, 100
screen_width, screen_height = 700, 600
sprite_width, sprite_height = 60, 60
colors = {
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'white': (255, 255, 255)
}
current_color = colors['white']

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    window.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3

    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)

    if x == 0:
        current_color = colors['blue']
    elif x == screen_width - sprite_width:
        current_color = colors['yellow']
    elif y == 0:
        current_color = colors['red']
    elif y == screen_height - sprite_height:
        current_color = colors['green']
    else:
        current_color = colors['white']

    pygame.draw.rect(window, current_color, pygame.Rect(x, y, sprite_width, sprite_height))
    pygame.draw.circle(window, GREEN, (300, 300), 50)
    pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

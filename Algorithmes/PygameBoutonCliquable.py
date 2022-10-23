# Imports

import pygame

# Configuration
pygame.init()


screen = pygame.display.set_mode((640, 480))

# Before Main loop
rect = pygame.Rect(100, 200, 500, 300)
print(rect.width)
btn_surface = pygame.Surface(
    (rect.width, rect.height)
)

normal_color = (200, 100, 100)
hover_color = (100, 200, 100)

# Game loop.
while  True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   

    # In the Main loop
    if rect.collidepoint(pygame.mouse.get_pos()):
        btn_surface.fill(hover_color)
    else:
        btn_surface.fill(normal_color)

    screen.blit(btn_surface, rect)

    pygame.display.flip()
  
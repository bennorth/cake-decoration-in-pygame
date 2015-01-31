import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    # Redraw the background
    screen.fill(pygame.Color('grey'))

    pygame.draw.circle(screen, pygame.Color('black'), (300, 300), 120, 2)

    pygame.display.flip()


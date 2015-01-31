import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


icing_colours = ['red', 'green', 'blue', 'yellow']

while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    # Redraw the background
    screen.fill(pygame.Color('grey'))

    pygame.draw.circle(screen, pygame.Color('black'), (300, 300), 120, 2)

    for i in range(len(icing_colours)):
        pygame.draw.circle(screen,
                           pygame.Color(icing_colours[i]),
                           (60, 90 * (i + 1)),
                           25,
                           0)

    pygame.display.flip()


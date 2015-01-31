import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


icing_colours = ['red', 'green', 'blue', 'yellow']

current_icing_colour = None

while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_x, click_y = pygame.mouse.get_pos()
                print('button 1 clicked at %d, %d' % (click_x, click_y))
                if 35 <= click_x <= 85:
                    if 65 <= click_y <= 115:
                        current_icing_colour = 'red'
                    elif 155 <= click_y <= 205:
                        current_icing_colour = 'green'
                    elif 245 <= click_y <= 295:
                        current_icing_colour = 'blue'
                    elif 335 <= click_y <= 385:
                        current_icing_colour = 'yellow'
                    else:
                        print('no icing there')

    # Redraw the background
    screen.fill(pygame.Color('grey'))

    # Draw interior of cake first, so black edge is visible.
    if current_icing_colour is not None:
        pygame.draw.circle(screen, pygame.Color(current_icing_colour), (300, 300), 120, 0)

    pygame.draw.circle(screen, pygame.Color('black'), (300, 300), 120, 2)

    for i in range(len(icing_colours)):
        pygame.draw.circle(screen,
                           pygame.Color(icing_colours[i]),
                           (60, 90 * (i + 1)),
                           25,
                           0)

    pygame.display.flip()


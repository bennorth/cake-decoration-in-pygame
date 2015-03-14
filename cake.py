import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


icing_colours = ['red', 'white', 'green', 'yellow']
icing_places = [70, 210, 350, 490]

current_icing_colour = (230,150,60)

strawberry = pygame.image.load('strawberryedited.png')
strawberry.convert_alpha()
strawberry_x = None
strawberry_y = None

while True:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_x, click_y = pygame.mouse.get_pos()
                print('button 1 clicked at %d, %d' % (click_x, click_y))

                if 180 < click_x< 420 and 180 < click_y< 420:
                    print ('cake')
                    strawberry_x = click_x - strawberry.get_width() / 2
                    strawberry_y = click_y - strawberry.get_height() / 2

                if 28 < click_x < 171:
                    if 1 < click_y < 139:
                        current_icing_colour = (255, 0, 0)
                    elif 278 < click_y < 420:
                        current_icing_colour = (0, 255, 0)
                    elif 138 < click_y < 278:
                        current_icing_colour = (255, 255, 255)
                    elif 420 < click_y < 559:
                        current_icing_colour = (255, 255, 0)

    # Redraw the background
    screen.fill(pygame.Color('grey'))

    pygame.draw.circle(screen, pygame.Color(*current_icing_colour), (300, 300), 120, 0)

    pygame.draw.circle(screen, pygame.Color('black'), (300, 300), 120, 2)

    # Has the player put a strawberry onto the cake?  Draw it if so.
    if strawberry_x is not None:
        screen.blit(strawberry, (strawberry_x, strawberry_y))

    for i in range(len(icing_colours)):
        pygame.draw.circle(screen, pygame.Color(icing_colours[i]), (100, icing_places[i]), 70)

    pygame.display.flip()


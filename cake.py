import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


icing_colours = ['red', 'white', 'green', 'yellow']
icing_places = [70, 210, 350, 490]

current_icing_colour = (230,150,60)

strawberry = pygame.image.load('strawberryedited.png')
strawberry.convert_alpha()

marshmallows = pygame.image.load('Marshmallows.png')
marshmallows.convert_alpha()

sprinkles = pygame.image.load('awesomesprinkles.png')
sprinkles.convert_alpha()

jellybeans = pygame.image.load('awesomejellybeans.png')
jellybeans.convert_alpha()

chocolate_chips = pygame.image.load('awesomechocochips.png')
chocolate_chips.convert_alpha()

back_arrow = pygame.image.load('awesomepinkarrow.png')
back_arrow.convert_alpha()

decoration_menu = [strawberry, marshmallows, sprinkles, jellybeans, chocolate_chips]

current_decoration = strawberry

decorations = []

# Flashing background.

background_colours = [(204, 0, 204),
                      (0, 128, 255),
                      (204, 0, 102)]
current_bg = 0

done = False
while not done:
    # Limit frame speed to 30 FPS
    #
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_x, click_y = pygame.mouse.get_pos()
                print('button 1 clicked at %d, %d' % (click_x, click_y))

                if 180 < click_x< 420 and 180 < click_y< 420:
                    print ('cake')
                    decoration_x = click_x - current_decoration.get_width() / 2
                    decoration_y = click_y - current_decoration.get_height() / 2
                    decorations.append((decoration_x, decoration_y, current_decoration))

                if 28 < click_x < 171:
                    if 1 < click_y < 139:
                        current_icing_colour = (255, 0, 0)
                    elif 278 < click_y < 420:
                        current_icing_colour = (0, 255, 0)
                    elif 138 < click_y < 278:
                        current_icing_colour = (255, 255, 255)
                    elif 420 < click_y < 559:
                        current_icing_colour = (255, 255, 0)

                if click_x > 500:
                    if 20 < click_y < 67:
                        print('strawberry')
                        current_decoration = strawberry
                    elif 107 < click_y < 160:
                        print('marshmallows')
                        current_decoration = marshmallows
                    elif 184 < click_y < 224:
                        current_decoration = sprinkles
                    elif 259 < click_y < 316:
                        current_decoration = jellybeans
                    elif 345 < click_y < 379:
                        current_decoration = chocolate_chips
                    else:
                        print('in decoration menu but not on decoration')

                if 44 <= click_y <= 100 and 306 <= click_x <= 377:
                    if len(decorations) > 0:
                        del decorations [-1]

    # Redraw the background with its current colour
    screen.fill(pygame.Color(*background_colours[current_bg]))

    pygame.draw.circle(screen, pygame.Color(*current_icing_colour), (300, 300), 120, 0)

    pygame.draw.circle(screen, pygame.Color('black'), (300, 300), 120, 2)

    # Draw the menu where the player can choose which decoration they're
    # about to put on the cake.
    decoration_choice_y = 20
    for decoration_choice in decoration_menu:
        screen.blit(decoration_choice, (500, decoration_choice_y))
        decoration_choice_y += 80

    # Remind player what their current chosen decoration is.
    screen.blit(current_decoration, (300 - current_decoration.get_width() / 2,
                                     475 - current_decoration.get_height() / 2))

    # Has the player put any decorations onto the cake?  Draw them if so.
    for decoration in decorations:
        x, y, picture = decoration
        screen.blit(picture, (x, y))

    screen.blit(back_arrow, (300, 30))

    for i in range(len(icing_colours)):
        pygame.draw.circle(screen, pygame.Color(icing_colours[i]), (100, icing_places[i]), 70)

    pygame.display.flip()


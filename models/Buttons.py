import pygame
from config import SCR_SIZE, screen

color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color = (255, 255, 255)
smallfont = pygame.font.SysFont('Corbel', 35)
width = SCR_SIZE[0]
height = SCR_SIZE[1]


# Don't forget to replace it with sprites!
def simple_buttons(text, mod_x, mod_y, mouse):
    text = smallfont.render(text, True, color)
    if SCR_SIZE[0] / mod_x <= mouse[0] <= SCR_SIZE[0] / mod_x + 140 \
            and SCR_SIZE[1] / mod_y <= mouse[1] <= SCR_SIZE[1] / mod_y + 40:
        pygame.draw.rect(screen, color_light, [SCR_SIZE[0] / mod_x, SCR_SIZE[1] / mod_y, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [SCR_SIZE[0] / mod_x, SCR_SIZE[1] / mod_y, 140, 40])

    screen.blit(text, (width / mod_x + 50, height / mod_y))


class Buttons(pygame.sprite.Sprite):
    pass
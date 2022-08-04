import pygame
import load_files
from config import SCR_SIZE

color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color = (255, 255, 255)
smallfont = pygame.font.SysFont('Corbel', 35)
width = SCR_SIZE[0]
height = SCR_SIZE[1]


class Buttons(pygame.sprite.Sprite):

    def __init__(self, image, coords):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_files.load_image(image)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.mask = pygame.mask.from_surface(self.image)


import pygame
import load_files

SCR_SIZE = (700, 880)
FOR_QUIT = (2.9, 2.9)
FOR_PET = (2.9, 3.75)

pygame.init()
screen = pygame.display.set_mode(SCR_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('game!')
image = load_files.load_image('Background.png')
background_image = pygame.transform.scale(image, SCR_SIZE)

creatures = pygame.sprite.Group()
font = pygame.font.SysFont('agencyfb', 65)
font_min = pygame.font.SysFont('agencyfb', 25)

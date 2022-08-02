import pygame
import load_files
from config import SCR_SIZE


class Dog(pygame.sprite.Sprite):
    dog_image = load_files.load_image('Dog.png')

    def __init__(self, hunger, fun, dirty):
        pygame.sprite.Sprite.__init__(self)
        self.image = Dog.dog_image
        self.image = pygame.transform.scale(self.image, (SCR_SIZE[0] / 2, SCR_SIZE[1] / 2.5))
        self.rect = self.image.get_rect()
        self.rect.center = (370, 320)
        self.mask = pygame.mask.from_surface(self.image)
        self.hunger = hunger
        self.fun = fun
        self.dirty = dirty
        self.ded = False
        self.full_eat = False
        self.null_dirty = False
        self.full_fun = False
        self.fun_zero = False
        self.compl_dirty = False
        self.eat = False

    def set_hunger(self, eat=False):
        if not eat and self.hunger != 0:
            self.hunger -= 10
            self.full_eat = False
            self.eat = False
        if eat and self.hunger != 100:
            self.hunger += 10
            self.eat = True
        if self.hunger == 0:
            self.ded = True
            self.full_eat = False
            self.null_dirty = False
            self.full_fun = False
            self.fun_zero = False
            self.compl_dirty = False
        if self.hunger == 100 and eat:
            self.full_eat = True

    def set_fun(self, game=False):
        if not game and self.fun != 0:
            self.fun -= 10
            self.full_fun = False
        if game and self.fun != 100:
            self.fun += 10
            self.fun_zero = False
        if self.fun == 0:
            self.fun_zero = True
        if self.fun == 100 and game:
            self.full_fun = True

    def set_dirty(self, wash=False):
        if not wash and self.dirty != 100:
            self.dirty += 10
            self.null_dirty = False
        if wash and self.dirty != 0:
            self.dirty -= 10
            self.compl_dirty = False
        if self.dirty == 100:
            self.compl_dirty = True
        if self.dirty == 0 and wash:
            self.null_dirty = True


class Brush(pygame.sprite.Sprite):
    brush_image = load_files.load_image('brush.png')

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Brush.brush_image
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (470, 450)
        self.mask = pygame.mask.from_surface(self.image)


class Ball(pygame.sprite.Sprite):
    ball_image = load_files.load_image('ball.png')

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Ball.ball_image
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (570, 450)
        self.mask = pygame.mask.from_surface(self.image)


class Bowl(pygame.sprite.Sprite):
    #load_files.load_image('ball.png')
    bowl_image = ['empty_bowl.png', 'Eat_bowl.png']

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_files.load_image(Bowl.bowl_image[0])
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (150, 420)
        self.mask = pygame.mask.from_surface(self.image)

    def eat(self, eat=False):
        if eat:
            self.image = load_files.load_image(Bowl.bowl_image[1])
        else:
            self.image = load_files.load_image(Bowl.bowl_image[0])
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (150, 420)
        self.mask = pygame.mask.from_surface(self.image)


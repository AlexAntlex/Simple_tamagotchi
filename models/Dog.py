import pygame
import load_files


class Dog(pygame.sprite.Sprite):
    dog_image = load_files.load_image('Dog.png')

    def __init__(self, hunger, fun, dirty):
        pygame.sprite.Sprite.__init__(self)
        self.image = Dog.dog_image
        self.image = pygame.transform.scale(self.image, (350, 350))
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

    def set_hunger(self, eat=False):
        if not eat and self.hunger != 0:
            self.hunger -= 10
            self.full_eat = False
        if eat and self.hunger != 100:
            self.hunger += 10
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
            self.compl_dirty = False
        if wash and self.dirty != 0:
            self.dirty -= 10
            self.compl_dirty = False
        if self.dirty == 100:
            self.compl_dirty = True
        if self.dirty == 0 and wash:
            self.null_dirty = True

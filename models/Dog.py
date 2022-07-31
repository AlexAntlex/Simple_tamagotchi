import pygame
import load_files
from config import screen, font


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

    def set_hunger(self, eat=False):
        if not eat and self.hunger != 0:
            self.hunger -= 10
        if eat and self.hunger != 100:
            self.hunger += 10
        if self.hunger == 0:
            self.ded = True
        if self.hunger == 100 and eat:
            pass
            # screen.blit(font.render('Your pet is already full!', True, (252, 252, 252), [350, 650]))

    def set_fun(self, game=False):
        if not game and self.fun != 0:
            self.fun -= 10
        if game and self.fun != 100:
            self.fun += 10
        if self.fun == 0:
            print('Your pet is bored!')
        if self.fun == 100 and game:
            print("Your pet doesn't want to play!")

    def set_dirty(self, wash=False):
        if not wash and self.dirty != 100:
            self.dirty += 10
        if wash and self.dirty != 0:
            self.dirty -= 10
        if self.dirty == 100:
            print('Your pet is very dirty!')
        if self.dirty == 0 and wash:
            print('Your pet is now completely clean!')

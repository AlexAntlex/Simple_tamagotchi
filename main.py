from datetime import datetime
import sys

import keyboard
import pygame

from config import screen, background_image, clock, SCR_SIZE, FOR_QUIT, FOR_PET, creatures, font, font_min
from models.Buttons import simple_buttons
from models.Dog import Dog

pygame.init()


def pressed_key(event):
    if event.name == '1' and event.event_type == 'down':
        creature.set_hunger(True)
    if event.name == '2' and event.event_type == 'down':
        creature.set_fun(True)
    if event.name == '3' and event.event_type == 'down':
        creature.set_dirty(True)


def draw_params(pet, param, text_xy):
    text = font.render(f"{param}: ", True, (252, 252, 252))
    text2 = font.render(str(pet), True, (252, 252, 252))
    screen.blit(text, text_xy[0])
    screen.blit(text2, text_xy[1])


def pet():
    global creature
    creature = Dog(50, 20, 70)
    creatures.add(creature)
    time = datetime.today().strftime("%H.%M%S")
    keyboard.hook(pressed_key)
    while True:
        new_time = datetime.today().strftime("%H.%M%S")
        events = pygame.event.get()
        screen.blit(background_image, (0, 0))
        creatures.draw(screen)
        if float(new_time) - float(time) > 0.0005:
            time = datetime.today().strftime("%H.%M%S")
            creature.set_fun()
            creature.set_dirty()
            creature.set_hunger()
        if creature.ded:
            screen.blit(font.render('Your pet died...', True, (252, 252, 252)), [350, 550])
        if creature.null_dirty:
            screen.blit(font_min.render('Your pet is now completely clean!', True, (252, 252, 252)), [350, 550])
        if creature.full_fun:
            screen.blit(font_min.render("Your pet doesn't want to play!", True, (252, 252, 252)), [350, 585])
        if creature.full_eat:
            screen.blit(font_min.render('Your pet is already full!', True, (252, 252, 252)), [350, 610])
        if creature.fun_zero:
            screen.blit(font_min.render('Your pet is bored!', True, (252, 252, 252)), [350, 625])
        if creature.compl_dirty:
            screen.blit(font_min.render('Your pet is very dirty!', True, (252, 252, 252)), [350, 650])
        draw_params(creature.hunger, "Hunger", ([20, 20], [190, 20]))
        draw_params(creature.dirty, "Dirty", ([20, 80], [190, 80]))
        draw_params(creature.fun, "Fun", ([20, 140], [190, 140]))

        screen.blit(font_min.render("You can feed your pet by pressing '1'", True, (255, 255, 255)), [50, 650])
        screen.blit(font_min.render("You can play with your pet by pressing '2'", True, (255, 255, 255)), [50, 675])
        screen.blit(font_min.render("You can wash your pet by pressing '3'", True, (255, 255, 255)), [50, 700])
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        clock.tick(60)


def main():
    while True:
        mouse = pygame.mouse.get_pos()
        screen.blit(background_image, (0, 0))
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()

            if i.type == pygame.MOUSEBUTTONDOWN:
                if SCR_SIZE[0] / FOR_QUIT[0] <= mouse[0] <= SCR_SIZE[0] / FOR_QUIT[0] + 140 \
                        and SCR_SIZE[1] / FOR_QUIT[1] <= mouse[1] <= SCR_SIZE[1] / FOR_QUIT[1] + 40:
                    sys.exit()
                if SCR_SIZE[0] / FOR_PET[0] <= mouse[0] <= SCR_SIZE[0] / FOR_PET[0] + 140 \
                        and SCR_SIZE[1] / FOR_PET[1] <= mouse[1] <= SCR_SIZE[1] / FOR_PET[1] + 40:
                    pet()

        simple_buttons("Quit", FOR_QUIT[0], FOR_QUIT[1], mouse)
        simple_buttons("Pet", FOR_PET[0], FOR_PET[1], mouse)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

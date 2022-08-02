from datetime import datetime
import sys
import pygame
from config import screen, background_image, clock, SCR_SIZE, creatures, font, font_min, buttons
from models.Buttons import Buttons
from models.Dog import Dog, Brush, Ball, Bowl

pygame.init()


def draw_params(pet, param, text_xy):
    text = font.render(f"{param}: ", True, (252, 252, 252))
    text2 = font.render(str(pet), True, (252, 252, 252))
    screen.blit(text, text_xy[0])
    screen.blit(text2, text_xy[1])


def pet():
    global creature
    creature = Dog(50, 20, 70)
    brush = Brush()
    ball = Ball()
    bowl = Bowl()
    b_quit = Buttons('Quit.png', (SCR_SIZE[0] / 2, SCR_SIZE[1] / 5 * 4))
    creatures.add(creature, brush, ball, bowl, b_quit)
    time = datetime.today().strftime("%H.%M%S")
    while True:
        new_time = datetime.today().strftime("%H.%M%S")
        events = pygame.event.get()
        screen.blit(background_image, (0, 0))
        creatures.draw(screen)

        if creature.eat:
            bowl.eat(True)
        else:
            bowl.eat(False)
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

        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in creatures if s.rect.collidepoint(pos)]
                for cret in clicked_sprites:
                    if type(cret) == Brush:
                        creature.set_dirty(True)
                    if type(cret) == Bowl:
                        creature.set_hunger(True)
                    if type(cret) == Ball:
                        creature.set_fun(True)
                    if b_quit.rect == cret.rect:
                        sys.exit()
        pygame.display.update()
        clock.tick(60)


def main():
    while True:
        screen.blit(background_image, (0, 0))
        events = pygame.event.get()
        b_quit = Buttons('Quit.png', (SCR_SIZE[0] / 2, SCR_SIZE[1] / 2))
        b_start = Buttons('Start.png', (SCR_SIZE[0] / 2, SCR_SIZE[1] / 3.5))
        buttons.add(b_quit, b_start)
        buttons.draw(screen)
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in buttons if s.rect.collidepoint(pos)]
                for sprt in clicked_sprites:
                    if b_quit.rect == sprt.rect:
                        sys.exit()
                    if b_start.rect == sprt.rect:
                        pet()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

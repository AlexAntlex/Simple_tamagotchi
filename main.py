"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('game!')
background_image = pygame.image.load('image.jpg')


def main():
    while True:
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
"""
import sys
from datetime import datetime
from Creatures import Dog
import keyboard


def again_game():
    print("Do you want to start the game again?\nPlease, answer 'Yes' or 'No'")
    answer = input().lower()
    if answer == "yes":
        main()
    else:
        sys.exit()


def pressed_key(event):
    if event.name == '1' and event.event_type == 'down':
        creature.set_hunger(True)
        print(f"You have fed your pet! Hunger: {creature.hunger}")
    if event.name == '2' and event.event_type == 'down':
        creature.set_fun(True)
        print(f"You played with a pet! Fun: {creature.fun}")
    if event.name == '3' and event.event_type == 'down':
        creature.set_dirty(True)
        print(f"You have washed your pet! Dirty: {creature.dirty}")


def game():
    print("Your pet has appeared!")
    print(f"Your pet's condition:\n Hunger: {creature.hunger}\n Fun: {creature.fun}\n Dirty: {creature.dirty}")
    print('-'*10)
    print("Pet parameters will change every 5 minutes of inactivity")
    print("You can feed your pet by pressing '1'\nYou can play with your pet by pressing '2'\n"
          "You can wash your pet by pressing '3'")

    time = datetime.today().strftime("%H.%M%S")
    keyboard.hook(pressed_key)

    while creature.hunger != 0:
        new_time = datetime.today().strftime("%H.%M%S")
        if float(new_time) - float(time) > 0.0005:    # If 0.005 is here, then it means I'm still testing this code
            time = datetime.today().strftime("%H.%M%S")
            creature.set_fun()
            creature.set_dirty()
            creature.set_hunger()
            if creature.hunger != 0:
                if creature.hunger > 10:
                    print(f"Your pet's condition::\n "
                          f"Hunger: {creature.hunger}\n "
                          f"Fun: {creature.fun}\n "
                          f"Dirty: {creature.dirty}")
                else:
                    print(f"Your pet may starve to death!\n "
                          f"Hunger: {creature.hunger}\n " 
                          f"Fun: {creature.fun}\n "
                          f"Dirty: {creature.dirty}")
            else:
                print("Game Over")
                break


def main():
    global creature
    creature = Dog(30, 60, 10)
    game()


if __name__ == "__main__":
    print("Hi! Do you want to get yourself a pet?\nPlease, answer 'Yes' or 'No'")
    answer = input().lower()
    if answer == "yes":
        main()
    else:
        sys.exit()


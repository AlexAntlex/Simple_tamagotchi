class Dog(object):

    def __init__(self, hunger, fun, dirty):
        self.hunger = hunger
        self.fun = fun
        self.dirty = dirty

    def set_hunger(self, eat=False):
        if not eat and self.hunger != 0:
            self.hunger -= 10
        if eat and self.hunger != 100:
            self.hunger += 10
        if self.hunger == 0:
            print('Your pet died...')
        if self.hunger == 100 and eat:
            print('Your pet is already full!')

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


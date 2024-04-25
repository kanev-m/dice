from random import randint

class Dice():
    '''Класс, представляющий один кубик'''
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        '''Возвращает рандомное число от 1 до 6'''
        return randint(1, self.num_sides)
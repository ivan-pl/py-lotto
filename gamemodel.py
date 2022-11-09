from random import randint, shuffle


class GameModel:
    def __init__(self, rows=3, columns=9):
        self.rows = rows
        self.columns = columns
        self.player_card = None
        self.pc_card = None
        self.keg_generator = None

    def new_game(self):
        self.player_card = Card(self.rows, self.columns)
        self.pc_card = Card(self.rows, self.columns)
        self.keg_generator = GameModel._create_keg_generator()

    @staticmethod
    def _create_keg_generator():
        numbers = [x for x in range(1, 91)]
        shuffle(numbers)
        for num in numbers:
            yield num

    def next_keg(self):
        return next(self.keg_generator)


class Card:

    def __init__(self, rows=3, columns=9):
        self.rows = 3
        self.columns = 9
        self.card = None

    def generate_card(self):
        used_numbers = set()
        card = []
        for x in range(self.rows):
            row = []
            for y in range(self.columns):
                newNum = randint(1, 90)
                while newNum in used_numbers:
                    newNum = randint(1, 90)
                used_numbers.add(newNum)
                row.append(newNum)
            row.sort()
            card.append(row)
        self.card = card

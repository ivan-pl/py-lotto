from random import randint, shuffle


class GameModel:
    def __init__(self, rows=3, columns=9):
        self.rows = rows
        self.columns = columns
        self.player_card = None
        self.pc_card = None
        self.keg_generator = None
        self.current_keg = None

    def new_game(self):
        self.player_card = Card(self.rows, self.columns)
        self.pc_card = Card(self.rows, self.columns)
        self.keg_generator = GameModel._create_keg_generator()

    @staticmethod
    def _create_keg_generator():
        numbers = [x for x in range(1, 91)]
        shuffle(numbers)
        for (ind, num) in enumerate(numbers):
            yield (num, len(numbers) - 1 - ind)

    def next_keg(self):
        self.current_keg = next(self.keg_generator)
        return self.current_keg


class Card:

    def __init__(self, rows=3, columns=9):
        self.rows = rows
        self.columns = columns
        self.card = None
        self.generate_card()

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

    def __iter__(self):
        self._iter_cur_row = 0
        return self

    def __next__(self):
        if (self._iter_cur_row < len(self.card)):
            row = self.card[self._iter_cur_row]
            self._iter_cur_row += 1
            return row
        raise StopIteration


if __name__ == "__main__":
    card = Card()
    for row in card:
        print(row)

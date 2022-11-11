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
        self.current_keg, kegs_left = next(self.keg_generator)
        return self.current_keg, kegs_left

    def next_turn(self, answer):
        self.pc_card.mark(self.current_keg)
        isChanged = self.player_card.mark(self.current_keg)
        doChange = True if answer == "y" else False
        if (isChanged != doChange):
            return (True, "Игрок ошибся")
        if (self.pc_card.left_nums == 0 and self.player_card.left_nums == 0):
            return (True, "Ничья")
        if (self.player_card.left_nums == 0):
            return (True, "Игрок победил")
        if (self.pc_card.left_nums == 0):
            return (True, "Компьютер победил")
        return (False, "")


class Card:

    def __init__(self, rows=3, columns=9):
        self.rows = rows
        self.columns = columns
        self.left_nums = rows * columns
        self.card = None
        self.generate_card()

    def mark(self, kegNum):
        for row in self.card:
            for i, num in enumerate(row):
                if num == kegNum:
                    row[i] = 0
                    self.left_nums -= 1
                    return True
        return False

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

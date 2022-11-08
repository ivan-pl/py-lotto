from random import randint


class GameModel:
    def __init__(self):
        self.pc_card = Card()
        self.player_card = Card()


class Card:

    def __init__(self):
        pass

    @staticmethod
    def _generate_card(rows=3, columns=9):
        used_numbers = set()
        card = []
        for x in range(rows):
            row = []
            for y in range(columns):
                newNum = randint(1, 90)
                while newNum in used_numbers:
                    newNum = randint(1, 90)
                used_numbers.add(newNum)
                row.append(newNum)
            row.sort()
            card.append(row)
        return card

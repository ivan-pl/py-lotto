class GameView:

    def new_game(self):
        print("="*20, "НОВАЯ ИГРА", "="*20, sep="\n")

    def show_keg_info(self, keg_num, count_left):
        print(f"Новый бочонок: {keg_num} (осталось {count_left})")

    def show_card(self, card, card_owner):
        if card_owner == "player":
            print("-"*6, " Ваша карточка ", "-"*6)
        else:
            print("-"*3, " Карточка компьютера ", "-"*3)
        for row in card:
            str_line = ""
            for num in row:
                if num == 0:
                    str_line += f" - "
                elif num < 10:
                    str_line += f" {num} "
                else:
                    str_line += f"{num} "
            print(str_line)
        print("-"*29)

    def get_next_turn(self):
        answer = None
        while (answer not in ("y", "n")):
            answer = input("Зачеркнуть цифру? (y/n)")
        return answer

    def show_finish_game(self, reason):
        print("="*20, "Игра закончена", reason, "="*20, sep="\n")


if __name__ == "__main__":
    view = GameView()
    view.new_game()
    view.show_keg_info(21, 67)
    view.show_card([[1, 23, 3], [4, 55, 6]], "player")
    view.show_card([[12, 7, 3], [8, 6, 11]], "pc")

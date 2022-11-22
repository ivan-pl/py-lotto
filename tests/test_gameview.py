from pytest import fixture, mark, param
from gameview import GameView
import gameview


@fixture
def game_view_inst():
    return GameView()


players_card = """------  Ваша карточка  ------
 1  2  3 
 4  5  6 
-----------------------------
"""

pc_card = """---  Карточка компьютера  ---
 4  6  9 
 2  1  3 
-----------------------------
"""


class TestGameView:

    def test_new_game(self, game_view_inst, capfd):
        game_view_inst.new_game()
        out, err = capfd.readouterr()
        assert out == "====================\nНОВАЯ ИГРА\n====================\n"

    @mark.parametrize("game_view_inst, input_val, expected_val", [
        (..., 'y', 'y'),
        (..., 'n', 'n')
    ], indirect=["game_view_inst"])
    def test_get_next_turn(self, game_view_inst, input_val, expected_val):
        gameview.input = lambda _: input_val
        res = game_view_inst.get_next_turn()
        assert res == expected_val

    @mark.parametrize("game_view_inst, capfd, card, card_owner, expected_value", [
        param(..., ..., [[1, 2, 3], [4, 5, 6]], "player", players_card, id="Prints player card"),
        param(..., ..., [[4, 6, 9], [2, 1, 3]], "pc", pc_card, id="Prints pc card"),
    ], indirect=["game_view_inst", "capfd"])
    def test_show_card(self, game_view_inst, capfd, card, card_owner, expected_value):
        game_view_inst.show_card(card, card_owner)
        out, err = capfd.readouterr()
        assert out == expected_value

    @mark.parametrize("game_view_inst, capfd, keg_num, count_left, expected_val", [
        (..., ..., 23, 56, "Новый бочонок: 23 (осталось 56)\n"),
        (..., ..., 51, 11, "Новый бочонок: 51 (осталось 11)\n"),
    ], indirect=["game_view_inst", "capfd"])
    def test_show_keg_info(self, game_view_inst, capfd, keg_num, count_left, expected_val):
        game_view_inst.show_keg_info(keg_num, count_left)
        out, err = capfd.readouterr()
        assert out == expected_val

    @mark.parametrize("game_view_inst, capfd, reason, expected_val", [
        param(..., ..., "Игрок победил", "=" * 20 + "\nИгра закончена\nИгрок победил\n" + "=" * 20 + "\n", id="Player won")
    ], indirect=["game_view_inst", "capfd"])
    def test_show_finish_game(self, game_view_inst, capfd, reason, expected_val):
        game_view_inst.show_finish_game(reason)
        out, err = capfd.readouterr()
        assert out == expected_val

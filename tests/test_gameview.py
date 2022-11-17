from pytest import fixture, mark, param
from gameview import GameView
import gameview


@fixture
def game_view_inst():
    return GameView()


class TestGameView:

    def test_new_game(self, game_view_inst, capfd):
        game_view_inst.new_game()
        out, err = capfd.readouterr()
        assert out == "====================\nНОВАЯ ИГРА\n====================\n"

    @mark.parametrize("game_view_inst, input_val, expected_val", [
        (..., 'y', 'y'),
        (..., 'n', 'n')
    ], indirect=["game_view_inst"])
    def test_next_turn(self, game_view_inst, input_val, expected_val):
        gameview.input = lambda _: input_val
        res = game_view_inst.get_next_turn()
        assert res == expected_val


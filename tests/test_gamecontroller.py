from pytest import fixture
from unittest.mock import Mock, call
from gamemodel import GameModel
from gameview import GameView
from gamecontroller import GameController


@fixture
def game_controller_inst():
    game_model = GameModel()
    game_view = GameView()
    gamecontroller = GameController(game_view, game_model)
    return gamecontroller


class TestGameController:

    def test_start_game(self, game_controller_inst):
        finish_reason = "Game over"
        game_controller_inst.view = Mock()
        game_controller_inst.model = Mock()
        game_controller_inst.model.next_keg.side_effect = [(1, 10), (5, 9)]
        game_controller_inst.model.next_turn.side_effect = [(False, ""), (True, finish_reason)]
        game_controller_inst.start_game()

        game_controller_inst.view.new_game.assert_called_once()
        game_controller_inst.model.new_game.assert_called_once()
        keg_info_calls = [call(1, 10), call(5, 9)]
        game_controller_inst.view.show_keg_info.assert_has_calls(keg_info_calls)
        game_controller_inst.view.show_finish_game.assert_called_with(finish_reason)
        assert game_controller_inst.view.get_next_turn.call_count == 2

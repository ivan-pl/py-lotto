from pytest import fixture, param, mark
from gamemodel import GameModel, Card


@fixture
def game_model_inst(request):
    (rows, columns) = request.param
    game_model = GameModel(rows, columns)
    game_model.new_game()
    return game_model


class TestModel:

    @mark.parametrize("game_model_inst", [(2, 3)], indirect=True)
    def test_new_game(self, game_model_inst):
        assert isinstance(game_model_inst.player_card, Card)
        assert isinstance(game_model_inst.pc_card, Card)
        assert game_model_inst.player_card.rows == 2
        assert game_model_inst.player_card.columns == 3

    @mark.parametrize("game_model_inst", [(2, 3)], indirect=True)
    def test_next_keg(self, game_model_inst):
        prev_kegs_left = 101
        for i in range(10):
            cur_keg, kegs_left = game_model_inst.next_keg()
            assert type(cur_keg) is int
            assert type(kegs_left) is int
            assert kegs_left < prev_kegs_left
            prev_kegs_left = kegs_left

    def test__create_keg_generator(self):
        nums_set = set(num for (num, _) in GameModel._create_keg_generator())
        assert len(nums_set) == 90
        assert all([type(num) is int for num in nums_set])

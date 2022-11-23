from pytest import fixture, param, mark
from gamemodel import GameModel, Card


@fixture
def game_model_inst(request):
    game_model = GameModel(2, 3)
    game_model.new_game()
    return game_model


@fixture
def card_player_inst():
    arr2d = [[1, 2, 3], [4, 5, 6]]
    card = Card(len(arr2d), len(arr2d[0]))
    card.card = arr2d
    return card


@fixture
def card_pc_inst():
    arr2d = [[11, 12, 13], [14, 15, 16]]
    card = Card(len(arr2d), len(arr2d[0]))
    card.card = arr2d
    return card


class TestModel:

    @mark.parametrize("game_model_inst", [...], indirect=True)
    def test_new_game(self, game_model_inst):
        assert isinstance(game_model_inst.player_card, Card)
        assert isinstance(game_model_inst.pc_card, Card)
        assert game_model_inst.player_card.rows == 2
        assert game_model_inst.player_card.columns == 3

    @mark.parametrize("game_model_inst", [...], indirect=True)
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

    @mark.parametrize("game_model_inst, card_player_inst, card_pc_inst, cur_keg, answer, expected_val", [
        param(..., ..., ..., 1, 'n', (True, "Игрок ошибся"), id="Player makes mistake"),
        param(..., ..., ..., 1, 'y', (False, ""), id="Game continues"),
    ], indirect=["game_model_inst", "card_player_inst", "card_pc_inst"])
    def test_next_turn(self, game_model_inst, card_player_inst, card_pc_inst, cur_keg, answer, expected_val):
        game_model_inst.current_keg = cur_keg
        game_model_inst.player_card = card_player_inst
        game_model_inst.pc_card = card_pc_inst
        actual_answer = game_model_inst.next_turn(answer)
        assert actual_answer == expected_val

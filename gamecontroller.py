class GameController:
    def __init__(self, game_view, game_model):
        self.view = game_view
        self.model = game_model

    def start_game(self):
        self.model.new_game()
        self.view.new_game()
        is_finished = False
        while not is_finished:
            cur_keg, keg_left = self.model.next_keg()
            self.view.show_keg_info(cur_keg, keg_left)
            self.view.show_card(self.model.player_card, "player")
            self.view.show_card(self.model.pc_card, "pc")
            answer = self.view.get_next_turn()
            is_finished, reason = self.model.next_turn(answer)
            if is_finished:
                self.view.show_finish_game(reason)

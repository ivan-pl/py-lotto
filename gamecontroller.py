class GameController:
    def __init__(self, gameView, gameModel):
        self.view = gameView
        self.model = gameModel

    def start_game(self):
        self.model.new_game()
        self.view.new_game()
        isFinished = False
        while not isFinished:
            cur_keg, keg_left = self.model.next_keg()
            self.view.show_keg_info(cur_keg, keg_left)
            self.view.show_card(self.model.player_card, "player")
            self.view.show_card(self.model.pc_card, "pc")
            answer = self.view.get_next_turn()
            isFinished, reason = self.model.next_turn(answer)
            if (isFinished):
                self.view.show_finish_game(reason)
        

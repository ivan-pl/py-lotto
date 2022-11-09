class GameController:
    def __init__(self, gameView, gameModel):
        self.view = gameView
        self.model = gameModel

    def start_game(self):
        self.model.new_game()
        self.view.new_game()

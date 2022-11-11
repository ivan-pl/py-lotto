from gamecontroller import GameController
from gameview import GameView
from gamemodel import GameModel

if __name__ == "__main__":
    gameView = GameView()
    gameModel = GameModel(1, 1)
    gameController = GameController(gameView, gameModel)
    gameController.start_game()

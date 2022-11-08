from gamecontroller import GameController
from gameview import GameView
from gamemodel import GameModel

if __name__ == "__main__":
    gameView = GameView()
    gameModel = GameModel("player", "PC")
    gameController = GameController(gameView, gameModel)
    gameController.startGame()

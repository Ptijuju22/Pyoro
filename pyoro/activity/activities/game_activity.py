import logging

from pyoro.activity.activities.activity import Activity
from pyoro.game.controllers.user_controller import UserController
from pyoro.game.game_engine import GameEngine
from pyoro.game.game_state import GameMode
from pyoro.views.game_view import GameView


class GameActivity(Activity):
    def __init__(self, game_mode: GameMode):
        super().__init__()

        self.controller = UserController()
        self.game_engine = GameEngine(game_mode, self.controller)
        self.view = GameView(self.game_engine)

    def start(self) -> None:
        logging.info("Starting")
        self.game_engine.run()
        return super().start()

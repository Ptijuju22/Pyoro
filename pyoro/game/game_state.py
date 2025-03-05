import logging
import math

from pyoro.configuration import Configuration
from pyoro.game.game_mode import GameMode


class GameState:
    __slots__ = ("mode", "size", "speed", "background_id")

    def __init__(self, mode: GameMode):
        logging.info(f"Creating new game state for mode {mode.name}")

        configuration = Configuration()

        self.mode = mode
        self.size = (
            math.ceil(configuration.window_width / configuration.zoom),
            math.ceil(configuration.window_height / configuration.zoom),
        )
        self.speed = 1.0
        self.background_id = 0

    def speed_up(self, deltatime: float):
        configuration = Configuration()
        self.speed += configuration.speed_factor * deltatime

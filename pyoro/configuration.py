import logging
import typing

from pyoro.utils.singleton import singleton

DEFAULT_CONFIG: typing.Final = {
    "window_width": 640,
    "window_height": 576,
    "speed_factor": 0.02,
    "zoom": 32,
}


@singleton
class Configuration:
    __slots__ = ("window_width", "window_height", "speed_factor", "zoom")

    def __init__(self):
        logging.info("Initializing")
        self.window_width = int(DEFAULT_CONFIG["window_width"])
        self.window_height = int(DEFAULT_CONFIG["window_height"])
        self.speed_factor = float(DEFAULT_CONFIG["speed_factor"])
        self.zoom = float(DEFAULT_CONFIG["zoom"])

    def load(self):
        logging.info("Loading configuration")

    def save(self):
        pass

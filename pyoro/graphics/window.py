import logging
import pyglet

from pyoro.configuration import Configuration
from pyoro.utils.singleton import singleton


@singleton
class Window(pyglet.window.Window):
    def __init__(self):
        logging.info("Initializing")

        super().__init__()  # type: ignore

        configuration = Configuration()
        self.set_minimum_size(configuration.window_width, configuration.window_height)
        self.set_size(configuration.window_width, configuration.window_height)
        self.set_caption("Pyoro")  # type: ignore
        self.set_location(100, 100)  # type: ignore
        self.set_visible(True)  # type: ignore

    def force_update(self):
        self.draw(0)

import pyglet
import typing


class GameLoop:
    def __init__(self, on_tick: typing.Callable[[float], None]):
        self._on_tick = on_tick

    def start(self):
        pyglet.clock.schedule(self._on_tick)  # type: ignore

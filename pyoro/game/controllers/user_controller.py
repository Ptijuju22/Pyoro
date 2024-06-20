import pyglet

from pyglet.window import key  # type: ignore

from pyoro.entity.entity_direction import EntityDirection
from pyoro.game.controllers.controller import Controller
from pyoro.graphics.window import Window


class UserController(Controller):
    def __init__(self) -> None:
        super().__init__()

        self.key_state_handler = pyglet.window.key.KeyStateHandler()

        window = Window()
        window.push_handlers(self)  # type: ignore
        window.push_handlers(self.key_state_handler)  # type: ignore

    def some_key_pressed(self, *symbols: int) -> bool:
        for symbol in symbols:
            if self.key_state_handler[symbol]:
                return True
        return False

    def on_key_press(self, symbol: int, _modifiers: int) -> None:
        if symbol in (key.Q, key.LEFT):
            self.dispatch_event("on_move_start", EntityDirection.LEFT)  # type: ignore
        elif symbol in (key.D, key.RIGHT):
            self.dispatch_event("on_move_start", EntityDirection.RIGHT)  # type: ignore
        elif symbol == key.SPACE:
            self.dispatch_event("on_action_start")  # type: ignore

    def on_key_release(self, symbol: int, _modifiers: int) -> None:
        if symbol in (key.Q, key.LEFT):
            if not self.some_key_pressed(key.D, key.RIGHT):
                self.dispatch_event("on_move_end", EntityDirection.LEFT)  # type: ignore
        elif symbol in (key.D, key.RIGHT):
            if not self.some_key_pressed(key.Q, key.LEFT):
                self.dispatch_event("on_move_end", EntityDirection.RIGHT)  # type: ignore
        elif symbol == key.SPACE:
            self.dispatch_event("on_action_end")  # type: ignore

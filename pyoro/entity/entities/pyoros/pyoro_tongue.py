import pyglet
from pyoro.entity.entities.pyoros.pyoro import Pyoro
from pyoro.entity.entities.pyoros.pyoro_state import PyoroState
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.controllers.controller import Controller


class PyoroTongue(Pyoro):
    EAT_ANIMATION_INTERVAL = 0.03
    EAT_ANIMATION_DURATION = 0.6

    def __init__(self, pos: tuple[float, float], controller: Controller):
        super().__init__(EntityKind.PYORO, pos, controller)

        controller.push_handlers(on_action_start=self.start_action)  # type: ignore

    def start_action(self) -> None:
        self.stop_move()
        self.state = PyoroState.TONGING

    def end_action(self) -> None:
        self.state = PyoroState.NORMAL

    def can_move(self) -> bool:
        return self.state not in (PyoroState.TONGING, PyoroState.DYING)

    def start_move(self, direction: EntityDirection) -> None:
        if self.can_move():
            return super().start_move(direction)
        return None

    def stop_move(self) -> None:
        if self.can_move():
            return super().stop_move()
        return None

    def jump(self) -> None:
        if self.can_move():
            return super().jump()
        return None

    def eat(self) -> None:
        def switch(_dt: float) -> None:
            match self.state:
                case PyoroState.EATING:
                    self.state = PyoroState.NORMAL
                case _:
                    self.state = PyoroState.EATING

        def reset(_dt: float) -> None:
            if self.state == PyoroState.EATING:
                self.state = PyoroState.NORMAL

        pyglet.clock.schedule_interval_for_duration(  # type: ignore
            switch, self.EAT_ANIMATION_INTERVAL, self.EAT_ANIMATION_DURATION
        )
        pyglet.clock.schedule_once(reset, self.EAT_ANIMATION_DURATION)  # type: ignore

import pyglet
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_state import PyoroState
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_state import GameState


class Pyoro(Entity):
    SIZE = (2, 2)
    HITBOX = (0, 0, 2, 2)
    SPEED = 16
    FALLING_SPEED = 3
    JUMP_ANIMATION_INTERVAL = 0.04

    def __init__(
        self, kind: EntityKind, pos: tuple[float, float], controller: Controller
    ):
        super().__init__(kind, pos)
        self.vel = (0, 0)
        self.state: PyoroState = PyoroState.NORMAL
        self.score = 0

        controller.push_handlers(on_move_start=self.start_move, on_move_end=lambda _: self.stop_move())  # type: ignore

        pyglet.clock.schedule_interval(lambda _: self.jump(), self.JUMP_ANIMATION_INTERVAL)  # type: ignore

    def update(self, deltatime: float, game_state: GameState) -> None:
        super().update(deltatime, game_state)

        if self.pos[0] < 0:
            self.pos = (0, self.pos[1])
        if self.pos[0] + self.SIZE[0] > game_state.size[0]:
            self.pos = (game_state.size[0] - self.SIZE[0], self.pos[1])

    def start_move(self, direction: EntityDirection) -> None:
        self.direction = direction
        self.vel = (self.SPEED * self.direction.value, 0)

    def stop_move(self) -> None:
        self.vel = (0, 0)
        self.state = PyoroState.NORMAL

    def jump(self) -> None:
        if self.vel[0] != 0:
            if self.state == PyoroState.JUMPING:
                self.state = PyoroState.NORMAL
            elif self.state == PyoroState.NORMAL:
                self.state = PyoroState.JUMPING

    def die(self) -> None:
        self.state = PyoroState.DYING
        self.vel = (0, -self.FALLING_SPEED)

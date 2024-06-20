import math

from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_state import GameState


class Tongue(Entity):
    SIZE = (1.2, 1.2)
    HITBOX = (-0.2, -0.2, 1.6, 1.6)
    EXTRACT_SPEED = 20
    RETRACT_SPEED = 36
    ANGLE = math.pi / 4
    POS_OFFSET = (0.25, -0.25)
    BEAN_POS_OFFSET = (0.5, 0.5)

    def __init__(self, pyoro: PyoroTongue, controller: Controller):
        super().__init__(EntityKind.TONGUE, self.calculate_pos(pyoro))

        self.direction = pyoro.direction
        self._extending = False

        controller.push_handlers(  # type: ignore
            on_action_start=self.extract, on_action_end=self.retract
        )

    def get_extending(self) -> bool:
        return self._extending

    def calculate_pos(self, pyoro: PyoroTongue) -> tuple[float, float]:
        direction_factor = 1 if pyoro.direction == EntityDirection.RIGHT else 0
        return (
            pyoro.pos[0]
            + pyoro.SIZE[0] / 2
            - self.SIZE[0] * (1 - direction_factor)
            + self.POS_OFFSET[0] * pyoro.direction.value,
            pyoro.pos[1] + pyoro.SIZE[1] / 2 + self.POS_OFFSET[1],
        )

    def calculate_retract_vel(self) -> tuple[float, float]:
        return (
            -self.RETRACT_SPEED * math.cos(self.ANGLE) * self.direction.value,
            -self.RETRACT_SPEED * math.sin(self.ANGLE),
        )

    def extract(self):
        self._extending = True
        self.vel = (
            self.EXTRACT_SPEED * math.cos(self.ANGLE) * self.direction.value,
            self.EXTRACT_SPEED * math.sin(self.ANGLE),
        )

    def retract(self):
        self._extending = False
        self.vel = self.calculate_retract_vel()

    def update(self, deltatime: float, game_state: GameState) -> None:
        if (
            self.pos[0] + self.SIZE[0] > game_state.size[0]
            or self.pos[0] < 0
            or self.pos[1] + self.SIZE[1] > game_state.size[1]
            or self.pos[1] < 0
        ):
            self.retract()
        return super().update(deltatime, game_state)

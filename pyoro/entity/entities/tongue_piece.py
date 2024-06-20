from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.entity_kind import EntityKind


class TonguePiece(Entity):
    SIZE = (0.24, 0.24)
    HITBOX = (0, 0, 0, 0)

    def __init__(self, pyoro: PyoroTongue, tongue: Tongue, index: int):
        self.index = index

        super().__init__(EntityKind.TONGUE_PIECE, self.calculate_pos(pyoro, tongue))

        self.direction = pyoro.direction

    def calculate_pos(self, pyoro: PyoroTongue, tongue: Tongue) -> tuple[float, float]:
        x_offset = 0 if pyoro.direction == EntityDirection.RIGHT else -self.SIZE[0]
        return (
            pyoro.pos[0]
            + pyoro.SIZE[0] / 2
            + pyoro.direction.value
            * (self.index * self.SIZE[0] / 2 + tongue.POS_OFFSET[0])
            + x_offset,
            pyoro.pos[1]
            + pyoro.SIZE[1] / 2
            + self.index * self.SIZE[1] / 2
            + tongue.POS_OFFSET[1],
        )

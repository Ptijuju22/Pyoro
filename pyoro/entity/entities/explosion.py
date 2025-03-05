from pyoro.entity.entities.entity import Entity
from pyoro.entity.entity_kind import EntityKind


class Explosion(Entity):
    SIZE = (1.5, 1.5)
    HITBOX = (0, 0, 0, 0)
    POS_OFFSET = (0, -0.4)
    DURATION = 1.2

    def __init__(self, pos: tuple[float, float]):
        super().__init__(EntityKind.EXPLOSION, pos)

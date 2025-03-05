from pyoro.entity.entities.entity import Entity
from pyoro.entity.entity_kind import EntityKind


class Case(Entity):
    FALL_SPEED = 25

    def __init__(self, pos: tuple[float, float]):
        super().__init__(EntityKind.CASE, pos)

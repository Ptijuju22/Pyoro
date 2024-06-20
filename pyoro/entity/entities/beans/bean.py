import random
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entity_kind import EntityKind


class Bean(Entity):
    SIZE = (1.5, 1.5)
    HITBOX = (0.25, 0.25, 1, 1)
    FALL_SPEED_RANGE = (0.7, 1.2)
    SCHEDULE_REPARTITION = (1, 1)

    def __init__(self, kind: EntityKind, pos: tuple[float, float]):
        super().__init__(kind, pos)

        self.vel = (
            0,
            -(
                random.random() * (self.FALL_SPEED_RANGE[1] - self.FALL_SPEED_RANGE[0])
                + self.FALL_SPEED_RANGE[0]
            ),
        )
        self.dangerous = True

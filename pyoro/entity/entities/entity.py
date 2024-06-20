from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.game_state import GameState


class Entity:
    SIZE = (1, 1)
    HITBOX = (0, 0, 1, 1)

    def __init__(self, kind: EntityKind, pos: tuple[float, float]):
        self.kind = kind
        self.pos: tuple[float, float] = pos
        self.vel: tuple[float, float] = (0, 0)
        self.direction: EntityDirection = EntityDirection.RIGHT

    def is_colliding(self, other: "Entity") -> bool:
        self_x0 = self.pos[0] + self.HITBOX[0]
        self_x1 = self.pos[0] + self.HITBOX[0] + self.HITBOX[2]
        self_y0 = self.pos[1] + self.HITBOX[1]
        self_y1 = self.pos[1] + self.HITBOX[1] + self.HITBOX[3]

        other_x0 = other.pos[0] + other.HITBOX[0]
        other_x1 = other.pos[0] + other.HITBOX[0] + other.HITBOX[2]
        other_y0 = other.pos[1] + other.HITBOX[1]
        other_y1 = other.pos[1] + other.HITBOX[1] + other.HITBOX[3]

        return (
            self_x0 < other_x1
            and self_x1 > other_x0
            and self_y0 < other_y1
            and self_y1 > other_y0
        )

    def get_id(self) -> int:
        return hash(self)

    def update(self, deltatime: float, game_state: GameState) -> None:
        self.pos = (
            self.pos[0] + self.vel[0] * deltatime,
            self.pos[1] + self.vel[1] * deltatime,
        )

    def kill(self):
        del self

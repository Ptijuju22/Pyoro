from pyoro.entity.entities.entity import Entity
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.game_state import GameState


class Angel(Entity):
    SPEED = 10
    ARMS_LENGTH = 1.5

    def __init__(self, pos: tuple[float, float]):
        super().__init__(EntityKind.ANGEL, pos)
        self.vel = (0, -self.SPEED)

    def update(self, deltatime: float, game_state: GameState) -> None:
        super().update(deltatime, game_state)
        if self.pos[1] <= self.ARMS_LENGTH + 0.5:
            self.vel = (0, self.SPEED)

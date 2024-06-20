import enum

from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entity_kind import EntityKind


class ScoreValue(enum.Enum):
    SCORE_10 = 10
    SCORE_50 = 50
    SCORE_100 = 100
    SCORE_300 = 300
    SCORE_1000 = 1000


class Score(Entity):
    BLINK_INTERVAL = 0.05
    LIFE_TIME = 1
    SIZE = (1.5, 0.7)
    HITBOX_SIZE = (0, 0, 0, 0)

    def __init__(self, pos: tuple[float, float], value: ScoreValue, bean: Bean):
        super().__init__(EntityKind.SCORE, pos)
        self.value = value
        self.bean = bean

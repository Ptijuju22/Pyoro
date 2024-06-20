from typing import Callable, Iterable

import pyglet
from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.score import Score, ScoreValue
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.operators.operator import Operator
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_state import GameState


class ScoreOperator(Operator):
    def __init__(
        self,
        get_entities_fct: Callable[[], Iterable[Entity]],
        add_entity_fct: Callable[[Entity], None],
        remove_entity_fct: Callable[[Entity], None],
        controller: Controller,
    ) -> None:
        super().__init__(
            get_entities_fct, add_entity_fct, remove_entity_fct, controller
        )
        self.game_height: int = 0

    def calculate_score(self, bean: Bean) -> int:
        ratio = bean.pos[1] / self.game_height

        if ratio >= 0.7:
            return 1000
        if ratio >= 0.6:
            return 300
        if ratio >= 0.4:
            return 100
        if ratio >= 0.2:
            return 50
        return 10

    def spawn_score(self, bean: Bean) -> None:
        pos = (
            bean.pos[0] + bean.SIZE[0] / 2 - Score.SIZE[0] / 2,
            bean.pos[1] + bean.SIZE[1] / 2 - Score.SIZE[1] / 2,
        )
        score = Score(pos, ScoreValue(self.calculate_score(bean)), bean)
        self.add_entity(score)
        pyglet.clock.schedule_once(lambda _: self.remove_score(score), score.LIFE_TIME)  # type: ignore

    def remove_score(self, score: Score) -> None:
        self.remove_entity(score)

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if isinstance(entity1, Bean) and isinstance(entity2, Tongue):
            beans_already_scored = {score.bean for score in self.filter_entities(Score)}

            if entity1 not in beans_already_scored:
                self.spawn_score(entity1)
        return super().collide(entity1, entity2)

    def update(self, game_state: GameState) -> None:
        self.game_height = game_state.size[0]
        return super().update(game_state)

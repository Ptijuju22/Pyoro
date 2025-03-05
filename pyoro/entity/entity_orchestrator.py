import logging

from pyoro.entity.entities.entity import Entity
from pyoro.entity.operators.bean_operator import BeanOperator
from pyoro.entity.operators.case_operator import CaseOperator
from pyoro.entity.operators.explosion_operator import ExplosionOperator
from pyoro.entity.operators.operator import Operator
from pyoro.entity.operators.pyoro_operator import PyoroOperator
from pyoro.entity.operators.score_operator import ScoreOperator
from pyoro.entity.operators.tongue_operator import TongueOperator
from pyoro.entity.operators.tongue_piece_operator import TonguePieceOperator
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_state import GameMode, GameState


class EntityOrchestrator:
    def __init__(
        self, game_mode: GameMode, game_size: tuple[int, int], controller: Controller
    ):
        logging.info("Initializing")
        self.entities: list[Entity] = []
        self.operators: list[Operator] = []

        operator_classes = (
            CaseOperator,
            PyoroOperator,
            TongueOperator,
            TonguePieceOperator,
            BeanOperator,
            ExplosionOperator,
            ScoreOperator,
        )

        for operator_class in operator_classes:
            operator = operator_class(
                self.get_entities,
                self.add_entity,
                self.remove_entity,
                controller,
            )
            operator.setup(game_mode, game_size)
            self.operators.append(operator)

    def get_entities(self) -> tuple[Entity, ...]:
        return tuple(self.entities)

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        self.entities = [e for e in self.entities if e != entity]

    def update(self, deltatime: float, game_state: GameState) -> None:
        for entity in self.entities:
            entity.update(deltatime * game_state.speed, game_state)

        collisions: list[tuple[Entity, Entity]] = []
        for entity1 in self.entities:
            for entity2 in tuple(self.entities):
                if entity1 != entity2 and entity1.is_colliding(entity2):
                    collisions.append((entity1, entity2))

        for operator in self.operators:
            operator.update(game_state)

            for collision in collisions:
                operator.collide(*collision)

from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.case import Case
from pyoro.entity.entities.entity import Entity
from pyoro.entity.operators.operator import Operator
from pyoro.game.game_mode import GameMode


class CaseOperator(Operator):
    def setup(self, game_mode: GameMode, game_size: tuple[int, int]) -> None:
        for i in range(game_size[0]):
            self.add_entity(Case((i, 0)))

        return super().setup(game_mode, game_size)

    def remove_case(self, case: Case) -> None:
        self.remove_entity(case)
        case.kill()

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if (
            isinstance(entity1, Case)
            and isinstance(entity2, Bean)
            and entity2.dangerous
        ):
            self.remove_case(entity1)

        return super().collide(entity1, entity2)

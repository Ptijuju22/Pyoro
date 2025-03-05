from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.case import Case
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro import Pyoro
from pyoro.entity.entities.pyoros.pyoro_state import PyoroState
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entities.pyoros.pyoro_seed import PyoroSeed
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.operators.operator import Operator
from pyoro.game.game_mode import GameMode
from pyoro.game.game_state import GameState


class PyoroOperator(Operator):
    def setup(self, game_mode: GameMode, game_size: tuple[int, int]) -> None:
        match game_mode:
            case GameMode.TONGUE:
                self.add_entity(PyoroTongue((1, 1), self.controller))
            case GameMode.SHOOT:
                self.add_entity(PyoroSeed((1, 1), self.controller))
        return super().setup(game_mode, game_size)

    def update(self, game_state: GameState) -> None:
        pyoro = self.find_entity(Pyoro)
        cases = self.filter_entities(Case)

        def get_case_from_x(pos_x: int) -> Case | None:
            for c in cases:
                if c.pos[0] == pos_x:
                    return c
            return None

        def find_nearest_case(pos_x: int, direction: EntityDirection) -> Case | None:
            match direction:
                case EntityDirection.RIGHT:
                    for c in cases[::-1]:
                        if c.pos[0] <= pos_x:
                            return c
                    return None
                case EntityDirection.LEFT:
                    for c in cases:
                        if c.pos[0] >= pos_x:
                            return c
                    return None

        def move_pyoro_to_case(pyoro: Pyoro, c: Case) -> None:
            match pyoro.direction:
                case EntityDirection.RIGHT:
                    pyoro.pos = (c.pos[0] + c.SIZE[0] - pyoro.SIZE[0], pyoro.pos[1])
                case EntityDirection.LEFT:
                    pyoro.pos = (c.pos[0], pyoro.pos[1])

        if pyoro:
            match pyoro.direction:
                case EntityDirection.RIGHT:
                    front_case_x = int(pyoro.pos[0] + pyoro.SIZE[0])
                case EntityDirection.LEFT:
                    front_case_x = int(pyoro.pos[0])
            front_case = get_case_from_x(front_case_x)

            if not front_case:
                nearest_case = find_nearest_case(front_case_x, pyoro.direction)

                if nearest_case:
                    move_pyoro_to_case(pyoro, nearest_case)

        return super().update(game_state)

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if isinstance(entity1, PyoroTongue):
            if isinstance(entity2, Tongue):
                if not entity2.get_extending():
                    entity1.end_action()
            elif isinstance(entity2, Bean):
                if entity2.dangerous:
                    if entity1.state != PyoroState.DYING:
                        entity1.die()
                else:
                    entity1.eat()
        return super().collide(entity1, entity2)

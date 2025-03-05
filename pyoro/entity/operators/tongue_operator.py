from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.operators.operator import Operator
from pyoro.exceptions.pyoro_not_found import PyoroNotFoundException
from pyoro.game.game_mode import GameMode


class TongueOperator(Operator):
    def setup(self, game_mode: GameMode, game_size: tuple[int, int]) -> None:
        self.setup_controller(game_mode)
        return super().setup(game_mode, game_size)

    def setup_controller(self, game_mode: GameMode) -> None:
        if game_mode == GameMode.TONGUE:
            self.controller.push_handlers(on_action_start=self.spawn_tongue)  # type: ignore

    def spawn_tongue(self) -> None:
        pyoro = self.find_entity(PyoroTongue)
        tongue = self.find_entity(Tongue)

        if not pyoro:
            raise PyoroNotFoundException("Pyoro not found when trying to spawn tongue")
        if tongue:
            return None

        tongue = Tongue(pyoro, self.controller)
        tongue.extract()
        self.add_entity(tongue)

    def remove_tongue(self) -> None:
        tongue = self.find_entity(Tongue)

        if not tongue:
            return None

        self.remove_entity(tongue)
        tongue.kill()

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if isinstance(entity1, Tongue):
            if isinstance(entity2, PyoroTongue):
                if not entity1.get_extending():
                    self.remove_tongue()
            elif isinstance(entity2, Bean):
                if entity1.get_extending():
                    entity1.retract()
        return super().collide(entity1, entity2)

from pyoro.entity.entities.pyoros.pyoro import Pyoro
from pyoro.entity.entity_kind import EntityKind
from pyoro.game.controllers.controller import Controller


class PyoroSeed(Pyoro):
    def __init__(self, pos: tuple[float, float], controller: Controller):
        super().__init__(EntityKind.PYORO_2, pos, controller)

    def shoot(self):
        pass

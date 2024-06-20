import typing
from pyoro.entity.entities.entity import Entity
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_mode import GameMode
from pyoro.game.game_state import GameState

T = typing.TypeVar("T", bound=Entity)


class Operator:
    def __init__(
        self,
        get_entities_fct: typing.Callable[[], typing.Iterable[Entity]],
        add_entity_fct: typing.Callable[[Entity], None],
        remove_entity_fct: typing.Callable[[Entity], None],
        controller: Controller,
    ) -> None:
        self.get_entities = get_entities_fct
        self.add_entity = add_entity_fct
        self.remove_entity = remove_entity_fct
        self.controller = controller

    def setup(self, game_mode: GameMode, game_size: tuple[int, int]) -> None:
        pass

    def update(self, game_state: GameState) -> None:
        pass

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        pass

    def filter_entities(self, entity_cls: typing.Type[T]) -> list[T]:
        return [
            entity for entity in self.get_entities() if isinstance(entity, entity_cls)
        ]

    def find_entity(self, entity_cls: typing.Type[T]) -> T | None:
        for entity in self.get_entities():
            if isinstance(entity, entity_cls):
                return entity
        return None

import typing

from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entity_kind import EntityKind


class BeanPink(Bean):
    SCHEDULE_REPARTITION = (10, 3)

    def __init__(
        self,
        pos: tuple[float, float],
        spawn_angel_func: typing.Callable[[], None] | None = None,
    ):
        super().__init__(EntityKind.BEAN_PINK, pos)
        self.spawn_angel_func = spawn_angel_func

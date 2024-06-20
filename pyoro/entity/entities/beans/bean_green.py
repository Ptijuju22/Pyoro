from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entity_kind import EntityKind


class BeanGreen(Bean):
    SCHEDULE_REPARTITION = (4, 0.5)

    def __init__(self, pos: tuple[float, float]):
        super().__init__(EntityKind.BEAN_GREEN, pos)

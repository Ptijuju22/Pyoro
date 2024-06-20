import random
import typing
import numpy
import pyglet

from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.beans.bean_green import BeanGreen
from pyoro.entity.entities.beans.bean_pink import BeanPink
from pyoro.entity.entities.case import Case
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro import Pyoro
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.operators.operator import Operator
from pyoro.game.game_mode import GameMode
from pyoro.game.game_state import GameState


class BeanOperator(Operator):
    def setup(self, game_mode: GameMode, game_size: tuple[int, int]) -> None:
        self.bean_pink_scheduled = False
        self.random_generator = numpy.random.Generator(numpy.random.PCG64())
        self.schedule(BeanGreen, game_size)

        return super().setup(game_mode, game_size)

    def schedule(
        self,
        bean_cls: typing.Type[BeanGreen] | typing.Type[BeanPink],
        game_size: tuple[int, int],
    ) -> None:
        def on_clock(_dt: float) -> None:
            self.spawn_bean(bean_cls, game_size)

        delay = self.random_generator.normal(
            bean_cls.SCHEDULE_REPARTITION[0], bean_cls.SCHEDULE_REPARTITION[1]
        )
        pyglet.clock.schedule_once(on_clock, delay)  # type: ignore

    def spawn_bean(
        self,
        bean_cls: typing.Type[BeanGreen] | typing.Type[BeanPink],
        game_size: tuple[int, int],
    ) -> None:
        pos = (random.randint(0, game_size[0] - 1) - bean_cls.HITBOX[0], game_size[1])
        self.add_entity(bean_cls(pos))
        self.schedule(bean_cls, game_size)

    def update(self, game_state: GameState) -> None:
        pyoro = self.find_entity(Pyoro)
        beans = self.filter_entities(Bean)

        if pyoro and pyoro.score > 2000 and not self.bean_pink_scheduled:
            self.bean_pink_scheduled = True
            self.schedule(BeanPink, game_state.size)

        for bean in beans:
            if bean.pos[1] + bean.SIZE[1] < 0:
                self.remove_bean(bean)

        return super().update(game_state)

    def remove_bean(self, bean: Bean) -> None:
        self.remove_entity(bean)
        bean.kill()

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if isinstance(entity1, Bean):
            if isinstance(entity2, Tongue):
                entity1.pos = (
                    entity2.pos[0]
                    + entity2.SIZE[0] / 2
                    - entity1.SIZE[0] / 2
                    + entity2.BEAN_POS_OFFSET[0] * entity2.direction.value,
                    entity2.pos[1]
                    + entity2.SIZE[1] / 2
                    - entity1.SIZE[1] / 2
                    + entity2.BEAN_POS_OFFSET[1],
                )
                entity1.vel = entity2.calculate_retract_vel()
                entity1.dangerous = False
            elif isinstance(entity2, Pyoro):
                self.remove_bean(entity1)
            elif isinstance(entity2, Case):
                if entity1.dangerous:
                    self.remove_bean(entity1)

        return super().collide(entity1, entity2)

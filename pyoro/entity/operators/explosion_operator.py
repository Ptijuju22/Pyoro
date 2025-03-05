import pyglet

from pyoro.entity.entities.beans.bean import Bean
from pyoro.entity.entities.case import Case
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.explosion import Explosion
from pyoro.entity.entities.pyoros.pyoro import Pyoro
from pyoro.entity.operators.operator import Operator


class ExplosionOperator(Operator):
    def spawn_explosion(self, bean: Bean) -> None:
        explosion = Explosion(
            (
                bean.pos[0]
                + bean.SIZE[0] / 2
                + Explosion.POS_OFFSET[0]
                - Explosion.SIZE[0] / 2,
                bean.pos[1]
                + bean.SIZE[1] / 2
                + Explosion.POS_OFFSET[1]
                - Explosion.SIZE[1] / 2,
            )
        )
        self.add_entity(explosion)

        pyglet.clock.schedule_once(  # type: ignore
            lambda _: self.remove_explosion(explosion), explosion.DURATION  # type: ignore
        )

    def remove_explosion(self, explosion: Explosion) -> None:
        self.remove_entity(explosion)
        explosion.kill()

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if isinstance(entity1, Bean) and (
            (isinstance(entity2, Case) or isinstance(entity2, Pyoro))
            and entity1.dangerous
        ):
            self.spawn_explosion(entity1)
        return super().collide(entity1, entity2)

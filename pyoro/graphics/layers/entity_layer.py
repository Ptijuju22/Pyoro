import typing
import pyglet

from pyoro.banks.animation_bank import AnimationBank
from pyoro.banks.image_bank import ImageBank
from pyoro.configuration import Configuration
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entities.pyoros.pyoro_state import PyoroState
from pyoro.entity.entities.score import Score, ScoreValue
from pyoro.entity.entity_kind import EntityKind
from pyoro.entity.entity_orchestrator import EntityOrchestrator
from pyoro.graphics.layers.layer import Layer
from pyoro.graphics.layers.layer_level import LayerLevel


class EntityLayer(Layer):
    def __init__(self, entity_orchestrator: EntityOrchestrator) -> None:
        super().__init__(LayerLevel.ENTITY.value)

        self.entity_orchestrator = entity_orchestrator
        self.pyoro_group = pyglet.graphics.Group(order=LayerLevel.PYORO.value)
        self.sprites: dict[int, pyglet.sprite.Sprite] = {}

    @staticmethod
    def get_entity_image(
        entity: Entity,
    ) -> pyglet.image.AbstractImage | pyglet.image.Animation:
        image_bank = ImageBank()
        animation_bank = AnimationBank()

        match entity.kind:
            case EntityKind.CASE:
                return image_bank.get("case")
            case EntityKind.PYORO:
                pyoro = typing.cast(PyoroTongue, entity)
                match pyoro.state:
                    case PyoroState.NORMAL:
                        return image_bank.get("pyoro_normal")
                    case PyoroState.JUMPING:
                        return image_bank.get("pyoro_jump")
                    case PyoroState.EATING:
                        return image_bank.get("pyoro_eat")
                    case PyoroState.DYING:
                        return image_bank.get("pyoro_dead")
                    case PyoroState.TONGING:
                        return image_bank.get("pyoro_tongue")
                    case state:
                        raise ValueError(f"{state} is an unknown state for Pyoro")
            case EntityKind.TONGUE:
                return image_bank.get("tongue")
            case EntityKind.TONGUE_PIECE:
                return image_bank.get("tongue_piece")
            case EntityKind.BEAN_GREEN:
                return animation_bank.get("bean_green")
            case EntityKind.EXPLOSION:
                return animation_bank.get("explosion")
            case EntityKind.SCORE:
                score = typing.cast(Score, entity)
                match score.value:
                    case ScoreValue.SCORE_10:
                        return image_bank.get("score_10")
                    case ScoreValue.SCORE_50:
                        return image_bank.get("score_50")
                    case ScoreValue.SCORE_100:
                        return image_bank.get("score_100")
                    case ScoreValue.SCORE_300:
                        return animation_bank.get("score_300")
                    case ScoreValue.SCORE_1000:
                        return animation_bank.get("score_1000")
            case _:
                return image_bank.get_fallback()

    @staticmethod
    def convert_pos(pos: tuple[float, float]) -> tuple[int, int]:
        configuration = Configuration()
        return (int(pos[0] * configuration.zoom), int(pos[1] * configuration.zoom))

    @staticmethod
    def convert_size(size: tuple[float, float]) -> tuple[float, float]:
        configuration = Configuration()
        return (size[0] * configuration.zoom, size[1] * configuration.zoom)

    def get_entity_group(self, entity: Entity) -> pyglet.graphics.Group:
        match entity.kind:
            case EntityKind.PYORO:
                return self.pyoro_group
            case EntityKind.TONGUE:
                return self.pyoro_group
            case _:
                return self.group

    def get_sprite_image_size(self, sprite: pyglet.sprite.Sprite) -> tuple[int, int]:
        image = sprite.image  # type: ignore
        index = sprite.frame_index

        if isinstance(image, pyglet.image.Animation):  # type: ignore
            return (image.frames[index].image.width, image.frames[index].image.height)  # type: ignore
        return (image.width, image.height)  # type: ignore

    def add_missing_sprite(self, entity: Entity) -> None:
        real_pos = self.convert_pos(entity.pos)
        real_size = self.convert_size(entity.SIZE)

        image = self.get_entity_image(entity)
        sprite = pyglet.sprite.Sprite(
            img=image,
            group=self.get_entity_group(entity),
            batch=self.batch,
        )
        image_size = self.get_sprite_image_size(sprite)
        sprite.update(  # type: ignore
            x=real_pos[0]
            - (
                real_size[1] * (entity.direction.value - 1) // 2
            ),  # shift x if the sprite must be in the opposite direciton
            y=real_pos[1],
            scale_x=(real_size[0] / image_size[0]) * entity.direction.value,  # type: ignore
            scale_y=(real_size[1] / image_size[1]),  # type: ignore
        )
        self.sprites[entity.get_id()] = sprite

    def update_sprite(self, entity: Entity) -> None:
        real_pos = self.convert_pos(entity.pos)
        real_size = self.convert_size(entity.SIZE)

        sprite = self.sprites[entity.get_id()]
        new_image = self.get_entity_image(entity)

        if new_image != sprite.image:  # type: ignore
            sprite.image = new_image

        image_size = self.get_sprite_image_size(sprite)
        sprite.update(  # type: ignore
            x=real_pos[0]
            - (
                real_size[1] * (entity.direction.value - 1) // 2
            ),  # shift x if the sprite must be in the opposite direciton
            y=real_pos[1],
            scale_x=(real_size[0] / image_size[0]) * entity.direction.value,  # type: ignore
            scale_y=(real_size[1] / image_size[1]),  # type: ignore
        )

    def remove_excess_sprites(self) -> None:
        sprite_ids = set(self.sprites.keys())
        entity_ids = set(
            entity.get_id() for entity in self.entity_orchestrator.entities
        )
        excess_entity_ids = sprite_ids - entity_ids

        for entity_id in excess_entity_ids:
            self.sprites.pop(entity_id).delete()

    def draw(self) -> None:
        self.remove_excess_sprites()
        for entity in self.entity_orchestrator.entities:
            if entity.get_id() in self.sprites:
                self.update_sprite(entity)
            else:
                self.add_missing_sprite(entity)
        self.batch.draw()
        return super().draw()

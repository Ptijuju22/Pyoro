import pyglet

from pyoro.banks.image_bank import ImageBank
from pyoro.configuration import Configuration
from pyoro.game.game_state import GameState
from pyoro.graphics.layers.layer import Layer
from pyoro.graphics.layers.layer_level import LayerLevel


class BackgroundLayer(Layer):
    def __init__(self, game_state: GameState) -> None:
        super().__init__(LayerLevel.BACKGROUND.value)

        self.game_state = game_state

        image_bank = ImageBank()
        self.current_background = pyglet.sprite.Sprite(
            img=image_bank.get(
                f"background_{self.game_state.mode.value + 1}_{self.game_state.background_id}"
            ),
            batch=self.batch,
            group=self.group,
        )
        self.next_background: pyglet.sprite.Sprite | None = None

        self.setup_background(self.current_background, first_background=True)

    def setup_background(
        self, background_sprite: pyglet.sprite.Sprite, first_background: bool = False
    ) -> None:
        configuration = Configuration()
        background_sprite.update(  # type: ignore
            x=0,
            y=0,
            scale_x=(configuration.window_width / self.current_background.width),  # type: ignore
            scale_y=(configuration.window_height / self.current_background.height),  # type: ignore
        )
        background_sprite.opacity = 255 if first_background else 0

    def draw(self):
        self.batch.draw()

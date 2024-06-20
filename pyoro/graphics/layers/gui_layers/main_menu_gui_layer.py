import typing
from pyoro.game.game_state import GameMode
from pyoro.graphics.layers.gui_layers.gui_layer import GuiLayer
from pyoro.graphics.widgets.image import Image
from pyoro.graphics.widgets.image_button import ImageButton
from pyoro.graphics.widgets.anchor import AnchorX, AnchorY
from pyoro.graphics.widgets.text_button import TextButton
from pyoro.graphics.window import Window


class MainMenuGuiLayer(GuiLayer):
    def __init__(
        self,
        on_click_play: typing.Callable[[GameMode], None],
        on_click_settings: typing.Callable[[], None],
        on_click_quit: typing.Callable[[], None],
    ):
        super().__init__()

        window = Window()

        self.title = Image(
            self.batch,
            self.group,
            window.width // 2,
            window.height // 4 * 3,
            "gui_title",
            anchor_x=AnchorX.CENTER,
            anchor_y=AnchorY.CENTER,
        )
        self.play_tongue_button = ImageButton(  # type: ignore
            self.batch,
            self.group,
            window.width // 4,
            window.height // 2,
            lambda: on_click_play(GameMode.TONGUE),
            "gui_button_play_tongue",
            "gui_button_play_tongue_pressed",
            "gui_button_play_tongue_hovered",
            anchor_x=AnchorX.CENTER,
            anchor_y=AnchorY.CENTER,
        )
        self.play_seed_button = ImageButton(
            self.batch,
            self.group,
            window.width // 4 * 3,
            window.height // 2,
            lambda: on_click_play(GameMode.SHOOT),
            "gui_button_play_seed",
            "gui_button_play_seed_pressed",
            "gui_button_play_seed_hovered",
            anchor_x=AnchorX.CENTER,
            anchor_y=AnchorY.CENTER,
        )
        self.settings_button = TextButton(
            self.batch,
            self.group,
            window.width // 4,
            window.height // 4,
            on_click_settings,
            "Settings",
            anchor_x=AnchorX.CENTER,
            anchor_y=AnchorY.CENTER,
        )
        self.quit_button = TextButton(
            self.batch,
            self.group,
            window.width // 4 * 3,
            window.height // 4,
            on_click_quit,
            "Quit",
            anchor_x=AnchorX.CENTER,
            anchor_y=AnchorY.CENTER,
        )

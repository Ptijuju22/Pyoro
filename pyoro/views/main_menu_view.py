import typing
from pyoro.game.game_engine import GameEngine
from pyoro.game.game_mode import GameMode
from pyoro.graphics.layers.gui_layers.main_menu_gui_layer import MainMenuGuiLayer
from pyoro.views.view import View


class MainMenuView(View):
    def __init__(
        self,
        game_engine: GameEngine,
        on_play: typing.Callable[[GameMode], None],
        on_show_settings: typing.Callable[[], None],
        on_quit: typing.Callable[[], None],
    ) -> None:
        super().__init__()

        self.game_engine = game_engine
        self.gui_layer = MainMenuGuiLayer(
            on_click_play=on_play,
            on_click_settings=on_show_settings,
            on_click_quit=on_quit,
        )

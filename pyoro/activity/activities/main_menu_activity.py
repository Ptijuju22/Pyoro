import logging

from pyoro.activity.activities.activity import Activity
from pyoro.activity.activities.game_activity import GameActivity
from pyoro.activity.activities.settings_activity import SettingsActivity
from pyoro.activity.activity_manager import ActivityManager
from pyoro.game.game_engine import GameEngine
from pyoro.game.game_state import GameMode
from pyoro.views.main_menu_view import MainMenuView


class MainMenuActivity(Activity):
    def __init__(self):
        super().__init__()
        self.game_engine = GameEngine(GameMode.TONGUE)
        self.view = MainMenuView(
            self.game_engine, self.on_play, self.on_show_settings, self.on_quit
        )

    def start(self) -> None:
        logging.info("Starting")
        self.game_engine.run()
        return super().start()

    def on_play(self, mode: GameMode) -> None:
        activity_manager = ActivityManager()
        activity_manager.push_activity(GameActivity(mode))
        self.stop()

    def on_show_settings(self) -> None:
        activity_manager = ActivityManager()
        activity_manager.push_activity(SettingsActivity())
        self.stop()

    def on_quit(self) -> None:
        activity_manager = ActivityManager()
        activity_manager.stop()

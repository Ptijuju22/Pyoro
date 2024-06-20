import logging
import pyglet

from pyoro.activity.activities.activity import Activity
from pyoro.graphics.window import Window
from pyoro.utils.singleton import singleton


@singleton
class ActivityManager:
    def __init__(self):
        self._activities: list[Activity] = []
        self._current_activity: Activity | None = None

        window = Window()
        window.push_handlers(on_close=self.stop)  # type: ignore

    def push_activity(self, activity: Activity) -> None:
        logging.debug(
            f"New activity of type {activity.__class__.__name__} added to the stack"
        )
        self._activities.append(activity)

    def on_activity_stop(self) -> None:
        logging.info("Current activity stopped. Starting next activity")

        self._current_activity.pop_handlers()  # type: ignore

        if self._activities:
            self.set_current_activity(self._activities.pop(0))
        else:
            logging.info("No activity left on stack")
            self.stop()

    def set_current_activity(self, activity: Activity) -> None:
        self._current_activity = activity
        self._current_activity.push_handlers(on_stop=self.on_activity_stop)  # type: ignore
        self._current_activity.start()

    def start(self) -> None:
        logging.info("Starting")

        if not self._activities:
            logging.warn("No activity to start")
            return self.stop()
        self.set_current_activity(self._activities.pop(0))

        pyglet.app.run()

    def stop(self) -> None:
        logging.info("Stopping")
        pyglet.app.exit()

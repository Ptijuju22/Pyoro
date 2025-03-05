from pyglet import event, clock

from pyoro.views.view import View


class Activity(event.EventDispatcher):
    def __init__(self) -> None:
        self.running = False

        self.view: View | None = None

        self.register_event_type("on_start")  # type: ignore
        self.register_event_type("on_stop")  # type: ignore

    def start(self):
        self.running = True

        def update_view(_dt: float) -> None:
            if self.view:
                self.view.refresh()

        clock.schedule(update_view)  # type: ignore
        self.dispatch_event("on_start")  # type: ignore

    def stop(self):
        self.running = False
        self.dispatch_event("on_stop")  # type: ignore

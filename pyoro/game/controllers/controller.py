from pyglet import event


class Controller(event.EventDispatcher):
    def __init__(self) -> None:
        super().__init__()

        self.register_event_type("on_move_start")  # type: ignore
        self.register_event_type("on_move_end")  # type: ignore
        self.register_event_type("on_action_start")  # type: ignore
        self.register_event_type("on_action_end")  # type: ignore

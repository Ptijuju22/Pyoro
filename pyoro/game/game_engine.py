from pyoro.entity.entity_orchestrator import EntityOrchestrator
from pyoro.game.controllers.controller import Controller
from pyoro.game.game_loop import GameLoop
from pyoro.game.game_mode import GameMode
from pyoro.game.game_state import GameState


class GameEngine:
    def __init__(self, game_mode: GameMode, controller: Controller):
        self.state = GameState(game_mode)
        self.loop = GameLoop(on_tick=self.update)
        self.entity_orchestrator = EntityOrchestrator(
            game_mode, self.state.size, controller
        )

    def update(self, deltatime: float):
        self.entity_orchestrator.update(deltatime, self.state)
        self.state.speed_up(deltatime)

    def run(self):
        self.loop.start()

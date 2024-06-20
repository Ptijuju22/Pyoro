from pyoro.game.game_engine import GameEngine
from pyoro.graphics.layers.background_layer import BackgroundLayer
from pyoro.graphics.layers.entity_layer import EntityLayer
from pyoro.views.view import View


class GameView(View):
    def __init__(self, game_engine: GameEngine):
        super().__init__()
        self.game_engine = game_engine
        self.background_layer = BackgroundLayer(self.game_engine.state)
        self.entity_layer = EntityLayer(self.game_engine.entity_orchestrator)

    def refresh(self) -> None:
        self.background_layer.draw()
        self.entity_layer.draw()

        return super().refresh()

from pyoro.graphics.layers.layer import Layer
from pyoro.graphics.layers.layer_level import LayerLevel


class GuiLayer(Layer):
    def __init__(self) -> None:
        super().__init__(LayerLevel.GUI.value)

import pyglet


class Layer:
    def __init__(self, layer_level: int) -> None:
        self.batch = pyglet.graphics.Batch()
        self.group = pyglet.graphics.Group(order=layer_level)

    def draw(self) -> None:
        self.batch.draw()

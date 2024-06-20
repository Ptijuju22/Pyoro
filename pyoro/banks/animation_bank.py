import logging
import pyglet
from pyoro.banks.bank import Bank
from pyoro.banks.image_bank import ImageBank
from pyoro.utils.singleton import singleton

ANIMATION_IDS: dict[str, tuple[tuple[str, float], ...]] = {
    "bean_green": (
        ("bean_green_left", 0.4),
        ("bean_green_middle", 0.4),
        ("bean_green_right", 0.4),
        ("bean_green_middle", 0.4),
    ),
    "bean_pink": (
        ("bean_pink_left", 0.4),
        ("bean_pink_middle", 0.4),
        ("bean_pink_right", 0.4),
        ("bean_pink_middle", 0.4),
    ),
    "explosion": (
        ("explosion_0", 0.4),
        ("explosion_1", 0.4),
        ("explosion_2", 0.4),
    ),
    "score_300": (
        ("score_300_0", 0.05),
        ("score_300_1", 0.05),
        ("score_300_2", 0.05),
        ("score_300_3", 0.05),
        ("score_300_4", 0.05),
        ("score_300_5", 0.05),
    ),
    "score_1000": (
        ("score_1000_0", 0.05),
        ("score_1000_1", 0.05),
        ("score_1000_2", 0.05),
        ("score_1000_3", 0.05),
        ("score_1000_4", 0.05),
        ("score_1000_5", 0.05),
    ),
}


@singleton
class AnimationBank(Bank[pyglet.image.Animation]):
    def __init__(self):
        logging.info("Initializing")

        image_bank = ImageBank()
        self.fallback = pyglet.image.Animation(
            [pyglet.image.AnimationFrame(image_bank.get_fallback(), 1)]
        )
        super().__init__()

    def load(self):
        logging.info("Generating animations")

        image_bank = ImageBank()

        for key, value in ANIMATION_IDS.items():
            self.data[key] = pyglet.image.Animation(
                [
                    pyglet.image.AnimationFrame(
                        image_bank.get(image_id), frame_duration
                    )
                    for (image_id, frame_duration) in value
                ]
            )

        return super().load()

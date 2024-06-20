import logging
import pyglet

from pyoro.banks.bank import Bank
from pyoro.utils.singleton import singleton

IMAGE_IDS = {
    # Angels
    "angel_normal": "angels/angel_normal.png",
    "angel_fly": "angels/angel_fly.png",
    # Backgrounds 1
    "background_1_0": "backgrounds_1/background_1_0.png",
    "background_1_1": "backgrounds_1/background_1_1.png",
    "background_1_2": "backgrounds_1/background_1_2.png",
    "background_1_3": "backgrounds_1/background_1_3.png",
    "background_1_4": "backgrounds_1/background_1_4.png",
    "background_1_5": "backgrounds_1/background_1_5.png",
    "background_1_6": "backgrounds_1/background_1_6.png",
    "background_1_7": "backgrounds_1/background_1_7.png",
    "background_1_8": "backgrounds_1/background_1_8.png",
    "background_1_9": "backgrounds_1/background_1_9.png",
    "background_1_10": "backgrounds_1/background_1_10.png",
    "background_1_11": "backgrounds_1/background_1_11.png",
    "background_1_12": "backgrounds_1/background_1_12.png",
    "background_1_13": "backgrounds_1/background_1_13.png",
    "background_1_14": "backgrounds_1/background_1_14.png",
    "background_1_15": "backgrounds_1/background_1_15.png",
    "background_1_16": "backgrounds_1/background_1_16.png",
    "background_1_17": "backgrounds_1/background_1_17.png",
    "background_1_18": "backgrounds_1/background_1_18.png",
    "background_1_19": "backgrounds_1/background_1_19.png",
    "background_1_20": "backgrounds_1/background_1_20.png",
    # Backgrounds 2
    "background_2_1": "backgrounds_2/background_2_1.png",
    "background_2_2": "backgrounds_2/background_2_2.png",
    "background_2_3": "backgrounds_2/background_2_3.png",
    "background_2_4": "backgrounds_2/background_2_4.png",
    "background_2_5": "backgrounds_2/background_2_5.png",
    "background_2_6": "backgrounds_2/background_2_6.png",
    "background_2_7": "backgrounds_2/background_2_7.png",
    "background_2_8": "backgrounds_2/background_2_8.png",
    "background_2_9": "backgrounds_2/background_2_9.png",
    "background_2_10": "backgrounds_2/background_2_10.png",
    "background_2_11": "backgrounds_2/background_2_11.png",
    "background_2_12": "backgrounds_2/background_2_12.png",
    "background_2_13": "backgrounds_2/background_2_13.png",
    "background_2_14": "backgrounds_2/background_2_14.png",
    "background_2_15": "backgrounds_2/background_2_15.png",
    "background_2_16": "backgrounds_2/background_2_16.png",
    "background_2_17": "backgrounds_2/background_2_17.png",
    "background_2_18": "backgrounds_2/background_2_18.png",
    "background_2_19": "backgrounds_2/background_2_19.png",
    "background_2_20": "backgrounds_2/background_2_20.png",
    # Green Beans
    "bean_green_left": "beans_green/bean_green_left.png",
    "bean_green_middle": "beans_green/bean_green_middle.png",
    "bean_green_right": "beans_green/bean_green_right.png",
    # GUI
    "gui_button_background": "gui/button/base.png",
    "gui_button_background_hovered": "gui/button/hovered.png",
    "gui_button_background_pressed": "gui/button/pressed.png",
    "gui_button_play_seed": "gui/button_play_seed/base.png",
    "gui_button_play_seed_hovered": "gui/button_play_seed/hovered.png",
    "gui_button_play_seed_pressed": "gui/button_play_seed/pressed.png",
    "gui_button_play_tongue": "gui/button_play_tongue/base.png",
    "gui_button_play_tongue_hovered": "gui/button_play_tongue/hovered.png",
    "gui_button_play_tongue_pressed": "gui/button_play_tongue/pressed.png",
    "gui_title": "gui/title.png",
    # Pink Beans
    "bean_pink_left": "beans_pink/bean_pink_left.png",
    "bean_pink_middle": "beans_pink/bean_pink_middle.png",
    "bean_pink_right": "beans_pink/bean_pink_right.png",
    # Cases
    "case": "cases/case.png",
    # Explosions
    "explosion_0": "explosions/explosion_0.png",
    "explosion_1": "explosions/explosion_1.png",
    "explosion_2": "explosions/explosion_2.png",
    # Pyoro
    "pyoro_normal": "pyoros/pyoro_normal.png",
    "pyoro_dead": "pyoros/pyoro_dead.png",
    "pyoro_tongue": "pyoros/pyoro_tongue.png",
    "pyoro_eat": "pyoros/pyoro_eat.png",
    "pyoro_jump": "pyoros/pyoro_jump.png",
    # Pyoro 2
    "pyoro_2_normal": "pyoros_2/pyoro_2_normal.png",
    "pyoro_2_dead": "pyoros_2/pyoro_2_dead.png",
    "pyoro_2_shoot_1": "pyoros_2/pyoro_2_shoot_1.png",
    "pyoro_2_shoot_2": "pyoros_2/pyoro_2_shoot_2.png",
    "pyoro_2_shoot_3": "pyoros_2/pyoro_2_shoot_3.png",
    "pyoro_2_shoot_4": "pyoros_2/pyoro_2_shoot_4.png",
    "pyoro_2_jump": "pyoros_2/pyoro_2_jump.png",
    # Scores
    "score_10": "scores/score_10.png",
    "score_50": "scores/score_50.png",
    "score_100": "scores/score_100.png",
    "score_300_0": "scores/score_300_0.png",
    "score_300_1": "scores/score_300_1.png",
    "score_300_2": "scores/score_300_2.png",
    "score_300_3": "scores/score_300_3.png",
    "score_300_4": "scores/score_300_4.png",
    "score_300_5": "scores/score_300_5.png",
    "score_1000_0": "scores/score_1000_0.png",
    "score_1000_1": "scores/score_1000_1.png",
    "score_1000_2": "scores/score_1000_2.png",
    "score_1000_3": "scores/score_1000_3.png",
    "score_1000_4": "scores/score_1000_4.png",
    "score_1000_5": "scores/score_1000_5.png",
    # Tongue
    "tongue": "tongues/tongue.png",
    "tongue_piece": "tongues/tongue_piece.png",
}


@singleton
class ImageBank(Bank[pyglet.image.ImageData]):
    def __init__(self):
        logging.info("Initializing")
        super().__init__()

        self.fallback = pyglet.image.create(  # type: ignore
            32, 32, pyglet.image.SolidColorImagePattern(color=(0, 0, 0, 255))
        )

    def load(self) -> None:
        logging.info("Loading images")
        loader = pyglet.resource.Loader("../res/images")

        for key, value in IMAGE_IDS.items():
            try:
                self.data[key] = loader.image(value)  # type: ignore
            except pyglet.resource.ResourceNotFoundException:
                logging.warn(
                    f"Image '{value}' not found. Using a fake transparent image instead"
                )
                self.data[key] = pyglet.image.create(32, 32, pyglet.image.SolidColorImagePattern(color=(0, 0, 0, 255)))  # type: ignore
        return super().load()

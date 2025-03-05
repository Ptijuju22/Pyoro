import logging

from pyoro.activity.activities.game_activity import GameActivity
from pyoro.activity.activity_manager import ActivityManager
from pyoro.banks.animation_bank import AnimationBank
from pyoro.banks.image_bank import ImageBank
from pyoro.configuration import Configuration
from pyoro.game.game_mode import GameMode
from pyoro.graphics.window import Window

LOG_FORMAT = "%(asctime)s %(levelname)s [%(module)s] %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)


def main():
    logging.info("Initializing singletons")
    Window()  # Create a window
    configuration = Configuration()  # Create a default configuration
    image_bank = ImageBank()  # Create an empty image bank
    animation_bank = AnimationBank()

    logging.info("Loading resources")
    configuration.load()
    image_bank.load()
    animation_bank.load()

    logging.info("Starting activities")
    activity_manager = ActivityManager()
    activity_manager.push_activity(GameActivity(GameMode.TONGUE))
    activity_manager.start()

    logging.info("Nothing to do. Bye!")


if __name__ == "__main__":
    main()

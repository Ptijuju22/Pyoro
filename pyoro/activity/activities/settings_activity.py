import logging
from pyoro.activity.activities.activity import Activity


class SettingsActivity(Activity):
    def start(self):
        logging.info("Starting")

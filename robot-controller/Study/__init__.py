from General import General
from Tedium import Tedium
from MentalChallenge import MentalChallenge
from Empathy import Empathy


class Study(object):
    TASKS = []
    TASK_WIDGET = 0
    TASK_NAME = 1

    @staticmethod
    def setup():
        Study.TASKS.append([General(), "General"])
        Study.TASKS.append([Tedium(), "Tedium"])
        Study.TASKS.append([MentalChallenge(), "Mental Challenge"])
        Study.TASKS.append([Empathy(), "Empathy"])
    #END setup
#END class

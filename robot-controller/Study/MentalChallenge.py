from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action import Speech
from UI.ActionPushButton import ActionPushButton


class MentalChallenge(BaseStudy):
    def __init__(self):
        super(MentalChallenge, self).__init__()
        self._widgets = []
        self._buttons = []

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Find Cube", Speech("Please look behind your monitor and take out the Rubik's cube.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Explanation",
                Speech("Currently, computers are not very good at solving Rubik's Cubes. Computers can brute force the problem "
                       "or use simple tricks, but humans are able to solve the problem much more organically. Because we can "
                       "not represent the complex neurological processes of a human brain in a computer, we can use some "
                       "algorithms to learn from peoples' actions. The web cam on the laptop is going to record your movements"
                       " and learn from your experience. It does not matter whether or not you can solve the cube because all"
                       " data, successes and failures, is useful to the algorithm. Please do not feel pressured: most people"
                       " are not able to solve these puzzles. Approach this as a game and simply enjoy the puzzle, but do try "
                       "your best to solve it.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Turn On The Camera", Speech("I will now turn on the camera.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Turn Towards Camera", Speech("Please turn towards the blue light, and keep your hands in the general direction of the light.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Move Hands Up", Speech("Please move your hands up a bit.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Move Hands Down", Speech("Please move your hands down a bit.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Position Hands Infront Of The Camera", Speech("Please position your hands more in the direction of the camera.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Solve Cube", Speech("Now, please try solving the cube.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Data", Speech("It is important to get as much data as we can for the machine learning system. "
                                                                                   "We will do this as long as you can, but, let me know when you're done.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Mix Up And Try Again", Speech("Good. Now, please mix up the cube and solve it again. Continue to do so each time you solve it.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Done", Speech("Thank you, that should be good for now.")),
        ])

        self._setupUi(True)
    #END __init__()
#END class

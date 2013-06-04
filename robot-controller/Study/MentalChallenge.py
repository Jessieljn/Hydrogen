from PyQt4 import QtGui
from Action.Speech import Speech
from UI.SpeechPushButton import SpeechPushButton


class MentalChallenge(QtGui.QWidget):
    def __init__(self, parent, actionQueue):
        super(MentalChallenge, self).__init__(parent)
        self._actionQueue = actionQueue

        self.findCube = SpeechPushButton(self, "Find Cube", "Please look behind your monitor and take out the Rubik's cube.")
        self.findCube.execute.connect(self.on__SpeechButton_clicked)

        self.explanation = SpeechPushButton(self, "Explanation", "Currently, computers are not very good at solving "
                                                                "Rubik's Cubes. Computers can brute force the problem "
                                                                "or use simple tricks, but humans are able to solve "
                                                                "the problem much more organically. Because we can "
                                                                "not represent the complex neurological processes of "
                                                                "a human brain in a computer, we can use some "
                                                                "algorithms to learn from peoples' actions. The web "
                                                                "cam on the laptop is going to record your movements"
                                                                " and learn from your experience. It does not matter"
                                                                " whether or not you can solve the cube because all"
                                                                " data, successes and failures, is useful to the "
                                                                "algorithm. Please do not feel pressured: most people"
                                                                " are not able to solve these puzzles. Approach this "
                                                                "as a game and simply enjoy the puzzle, but do try "
                                                                "your best to solve it.")
        self.explanation.execute.connect(self.on__SpeechButton_clicked)

        self.camera = SpeechPushButton(self, "Turn On The Camera", "I will now turn on the camera.")
        self.camera.execute.connect(self.on__SpeechButton_clicked)

        self.turn = SpeechPushButton(self, "Turn Towards Camera", "Please turn towards the blue light, and keep your"
                                                                 " hands in the general direction of the light.")
        self.turn.execute.connect(self.on__SpeechButton_clicked)

        self.handsUp = SpeechPushButton(self, "Move Hands Up", "Please move your hands up a bit.")
        self.handsUp.execute.connect(self.on__SpeechButton_clicked)

        self.handsDown = SpeechPushButton(self, "Move Hands Down", "Please move your hands down a bit.")
        self.handsDown.execute.connect(self.on__SpeechButton_clicked)

        self.positionHands = SpeechPushButton(self, "Position Hands Infront Of The Camera", "Please position your hands"
                                                    " more in the direction of the camera.")
        self.positionHands.execute.connect(self.on__SpeechButton_clicked)

        self.solve = SpeechPushButton(self, "Solve Cube", "Now, please try solving the cube.")
        self.solve.execute.connect(self.on__SpeechButton_clicked)

        self.data = SpeechPushButton(self, "Data", "It is important to get as much data as we can for the machine "
                                                  "learning system. We will do this as long as you can, but, let me "
                                                  "know when you're done.")
        self.data.execute.connect(self.on__SpeechButton_clicked)

        self.mixUp = SpeechPushButton(self, "Mix Up And Try Again", "Good. Now, please mix up the cube and solve it "
                                                                   "again. Continue to do so each time you solve it.")
        self.mixUp.execute.connect(self.on__SpeechButton_clicked)

        self.done = SpeechPushButton(self, "Done", "Thank you, that should be good for now.")
        self.done.execute.connect(self.on__SpeechButton_clicked)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.findCube)
        layout.addWidget(self.explanation)
        layout.addWidget(self.camera)
        layout.addWidget(self.turn)
        layout.addWidget(self.handsUp)
        layout.addWidget(self.handsDown)
        layout.addWidget(self.positionHands)
        layout.addWidget(self.solve)
        layout.addWidget(self.data)
        layout.addWidget(self.mixUp)
        layout.addWidget(self.done)
    #END __init__()

    def on__SpeechButton_clicked(self, speech):
        self._actionQueue.enqueue(Speech(speech))
    #END on__SpeechButton_clicked()
#END class

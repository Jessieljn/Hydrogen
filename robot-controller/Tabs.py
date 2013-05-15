from PyQt4 import QtGui
import TaskTabs

##
# Tasks.py
#
# Different Tabs for TaskTabs.py
##


class General (QtGui.QWidget):
    def __init__(self, nao, parent):
        super(General, self).__init__()

        self.nao = nao
        self.parent = parent

        self.welcome = TaskTabs.SpeechButton("You're Welcome", "You are welcome", nao)

        self.nod = QtGui.QPushButton("Head Nodding")
        self.nod.clicked.connect(self.nao.nod)

        self.scratch = QtGui.QPushButton("Scratch Head")
        self.scratch.clicked.connect(self.nao.scratchHead)

        self.intro = TaskTabs.SpeechButton("Introduction", "Thanks for coming in. Please remember that you can leave at"
                                                           " any time. If you have any specific questions about the "
                                                           "tasks, please hold them until after the experiment is "
                                                           "complete; I will be happy to answer any of your questions "
                                                           "afterwards. If you are uncomfortable with this, please "
                                                           "remember that you can leave at any time. The cash "
                                                           "honorarium is yours to keep even if you choose not to "
                                                           "continue to the end.", nao)

        self.demographics = TaskTabs.SpeechButton("Demographics", "Before we begin, please open the blue folder in "
                                                                  "front of you. Inside, you will find a demographics "
                                                                  "questionnaire. Please fill it out and let me know "
                                                                  "when you are finished.", nao)

        self.sitDown = TaskTabs.SpeechButton("Sit Down", "Thank you. Please take a seat at the computer to my "
                                                         "right.", nao)

        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.intro)
        layout.addWidget(self.demographics)
        layout.addWidget(self.sitDown)
        layout.addWidget(self.welcome)
        layout.addWidget(self.nod)
        layout.addWidget(self.scratch)

        self.setLayout(layout)
    #END init()
#END General


class Tedium (QtGui.QWidget):
    def __init__(self, nao, parent):
        super(Tedium, self).__init__()
        self.nao = nao
        self.parent = parent

        self.explanation = TaskTabs.SpeechButton("Explanation", "Currently, the process of renaming files in a "
                                                                "graphical user interface is not very efficient. We "
                                                                "are trying to make this more efficient for users, so "
                                                                "we are collecting data on how people do this and are "
                                                                "feeding the data into a machine learning algorithm. "
                                                                "This laptop will record your exact mouse movements, "
                                                                "keyboard strokes, and precise timing to create a model"
                                                                " of the work you need to do to rename files. How "
                                                                "quickly you can do this is not important, so do not "
                                                                "worry about performance. Machine learning algorithms "
                                                                "require a great deal of data, hence the need to do "
                                                                "this repeatedly.", nao)

        self.knowHow = TaskTabs.SpeechButton("Know How?", "Do you know how to rename a file?", nao)
        self.great = TaskTabs.SpeechButton("Great", "Great!", nao)
        self.thatsOkay = TaskTabs.SpeechButton("That's Okay.", "That is okay, I will explain.", nao)

        self.openFolder = TaskTabs.SpeechButton("Open Folder", "Please open the folder called Experiment on the "
                                                               "desktop.", nao)

        self.rightClick = TaskTabs.SpeechButton("Right click", "Right click on the first file and press: re-name", nao)

        self.change = TaskTabs.SpeechButton("Change", "Change the last part of the file name that says: dot, jay"
                                                      " pee gee, to dot, pee n gee. For example: A file called robot,"
                                                      " dot, jay pee g, should be renamed to robot, dot, pee n "
                                                      "gee.", nao)

        self.enter = TaskTabs.SpeechButton("Enter", "Then, press enter or click somewhere else in the folder.", nao)

        self.good = TaskTabs.SpeechButton("Good", "Good. Please continue to do this for each file in the folder, and"
                                                  " let me know when you are done.", nao)

        self.shortcuts = TaskTabs.SpeechButton("Shortcuts.", "Because we are measuring precise keystrokes and mouse "
                                                             "movements, please do not use shortcuts such as copy and "
                                                             "paste, as this may confuse the machine learning "
                                                             "system.", nao)

        self.a = TaskTabs.SpeechButton("I'll Add Next", "Good. I will now add the next set of files.", nao)
        self.b = TaskTabs.SpeechButton("Are You Finished?", "Are you finished renaming the files?", nao)
        self.c = TaskTabs.SpeechButton("Do You See The Files?", "Do you see the files?", nao)
        self.d = TaskTabs.SpeechButton("Try F5", "Try pressing F5 on the keyboard.", nao)

        self.data = TaskTabs.SpeechButton("Data", "It is important to get as much data as we can for the machine "
                                                  "learning system. As you can see on the white board to my right, "
                                                  "there are four tasks in total in this experiment. For each one, we "
                                                  "can go as long as you want before moving on to the next task. You "
                                                  "can quit whenever you'd like. It is up to you how much data you give"
                                                  " us. You, are in control. Let us know when you think you are done,"
                                                  " and would like to move on to the next task.", nao)

        self.fifty = TaskTabs.SpeechButton("This Set Has 50, Next Has 100", "This set contains 50 files. The next set"
                                                                            " will contain 100 files.", nao)

        self.hundred = TaskTabs.SpeechButton("This Set Has 100, Next Has 500", "This set contains 100 files. The next "
                                                                               "set will contain 500 files.", nao)

        self.fiveHundred = TaskTabs.SpeechButton("This Set Has 500, Next Has 1000", "This set contains 500 files. "
                                                                                    "The next set will contain 1000 "
                                                                                    "files.", nao)

        self.thousand = TaskTabs.SpeechButton("This Set Has 1000, Next Has 5000 ", "This set contains 1000 files. The "
                                                                                   "next set will contain 5000 "
                                                                                   "files.", nao)

        self.tryClose = TaskTabs.SpeechButton("Try Closing Folder", "Try closing the folder and opening it up "
                                                                    "again.", nao)

        self.done = TaskTabs.SpeechButton("Done", "Thank you, that should be good for now.", nao)
        self.nextTask = TaskTabs.SpeechButton("Next Task", "We will now move onto the next task.", nao)

        layout = QtGui.QHBoxLayout()

        hbox1 = QtGui.QVBoxLayout()
        hbox2 = QtGui.QVBoxLayout()

        hbox1.addWidget(self.explanation)
        hbox1.addWidget(self.knowHow)
        hbox1.addWidget(self.great)
        hbox1.addWidget(self.thatsOkay)
        hbox1.addWidget(self.openFolder)
        hbox1.addWidget(self.rightClick)
        hbox1.addWidget(self.change)
        hbox1.addWidget(self.enter)
        hbox1.addWidget(self.good)
        hbox1.addWidget(self.data)
        hbox1.addWidget(self.shortcuts)

        hbox2.addWidget(self.a)
        hbox2.addWidget(self.fifty)
        hbox2.addWidget(self.hundred)
        hbox2.addWidget(self.fiveHundred)
        hbox2.addWidget(self.thousand)
        hbox2.addWidget(self.tryClose)
        hbox2.addWidget(self.b)
        hbox2.addWidget(self.c)
        hbox2.addWidget(self.d)
        hbox2.addWidget(self.done)
        hbox2.addWidget(self.nextTask)

        layout.addLayout(hbox1)
        layout.addLayout(hbox2)

        self.setLayout(layout)
    #END __init__()
#END Tedium


class MentalChallenge (QtGui.QWidget):
    def __init__(self, nao, parent):
        super(MentalChallenge, self).__init__()
        self.nao = nao
        self.parent = parent

        self.findCube = TaskTabs.SpeechButton("Find Cube", "Please look behind your monitor and take out the Rubik's "
                                                           "cube.", nao)

        self.explanation = TaskTabs.SpeechButton("Explanation", "Currently, computers are not very good at solving "
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
                                                                "your best to solve it.", nao)

        self.camera = TaskTabs.SpeechButton("Turn On The Camera", "I will now turn on the camera.", nao)

        self.turn = TaskTabs.SpeechButton("Turn Towards Camera", "Please turn towards the blue light, and keep your"
                                                                 " hands in the general direction of the light.", nao)

        self.handsUp = TaskTabs.SpeechButton("Move Hands Up", "Please move your hands up a bit.", nao)

        self.handsDown = TaskTabs.SpeechButton("Move Hands Down", "Please move your hands down a bit.", nao)

        self.positionHands = TaskTabs.SpeechButton("Position Hands Infront Of The Camera", "Please position your hands"
                                                                                           " more in the direction "
                                                                                           "of the camera.", nao)

        self.solve = TaskTabs.SpeechButton("Solve Cube", "Now, please try solving the cube.", nao)

        self.data = TaskTabs.SpeechButton("Data", "It is important to get as much data as we can for the machine "
                                                  "learning system. We will do this as long as you can, but, let me "
                                                  "know when you're done.", nao)

        self.mixUp = TaskTabs.SpeechButton("Mix Up And Try Again", "Good. Now, please mix up the cube and solve it "
                                                                   "again. Continue to do so each time you solve "
                                                                   "it.", nao)

        self.done = TaskTabs.SpeechButton("Done", "Thank you, that should be good for now.", nao)

        layout = QtGui.QVBoxLayout()

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

        self.setLayout(layout)
    #END init()
#END MentalChallenge


class Empathy(QtGui.QWidget):
    def __init__(self, nao, parent):
        super(Empathy, self).__init__()
        self.nao = nao
        self.parent = parent

        self.chinScratch = QtGui.QPushButton("Scratch Chin")
        self.chinScratch.clicked.connect(self.nao.chinScratch)

        self.pointLeft = QtGui.QPushButton("Left Hand Point")
        self.pointLeft.clicked.connect(self.nao.pointLeft)

        self.pointRight = QtGui.QPushButton("Right Hand Point")
        self.pointRight.clicked.connect(self.nao.pointRight)

        self.scratchHead = QtGui.QPushButton("Scratch Head")
        self.scratchHead.clicked.connect(self.nao.scratchHead)

        self.jitter = QtGui.QPushButton("Jitter Test")
        self.jitter.clicked.connect(self.nao.jitter)

        layout = QtGui.QHBoxLayout()

        hbox1 = QtGui.QVBoxLayout()
        hbox2 = QtGui.QVBoxLayout()

        hbox1.addWidget(self.chinScratch)
        hbox1.addWidget(self.scratchHead)
        hbox1.addWidget(self.pointRight)
        hbox1.addWidget(self.pointLeft)
        hbox1.addWidget(self.jitter)

        layout.addLayout(hbox1)
        layout.addLayout(hbox2)

        self.setLayout(layout)
    #END __init__()
#END Empathy
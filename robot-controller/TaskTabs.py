from PyQt4 import QtGui, QtNetwork, QtCore

#TabbedWid holds all *Tab classes


class SpeechButton(QtGui.QPushButton):
    def __init__(self, title, speech, nao):
        super(SpeechButton, self).__init__(speech)
        self.nao = nao
        self.speech = speech

        if len(speech) > 60:
            self.setText(speech[0:60] + "...")
        #END if

        self.clicked.connect(self.say)
    #END __init__()

    def say(self):
        self.nao.say(self.speech)
    #END say


class General (QtGui.QWidget):
    def __init__(self, nao, parent):
        super(General, self).__init__()

        self.nao = nao
        self.parent = parent

        self.intro = SpeechButton("Intro", "Thanks for coming in. Please remember that you can leave at any time. "
                                           "If you have any specific questions about the tasks, please hold them until "
                                           "after the experiment is complete; I will be happy to answer any of your "
                                           "questions afterwards. If you are uncomfortable with this, please remember "
                                           "that you can leave at any time. The cash honorarium is yours to keep even "
                                           "if you choose not to continue to the end.", nao)

        self.demographics = SpeechButton("Demographics", "Before wee begin, please open the blue folder in front of "
                                                         "you. Inside, you will find a demographics questionnaire. "
                                                         "Please fill it out and let me know when you are finished.", nao)

        self.sitDown = SpeechButton("Sit Down", "Thank you. Please take a seat at the computer to my right.", nao)

        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.intro)
        layout.addWidget(self.demographics)
        layout.addWidget(self.sitDown)

        self.setLayout(layout)
    #END init()
#END General


class Tedium (QtGui.QWidget):

    def __init__(self, nao, parent):
        super(Tedium, self).__init__()
        self.nao = nao
        self.parent = parent

        self.explanation = SpeechButton("Explanation", "Currently, the process of renaming files in a graphical user "
                                                       "interface is not very efficient. We are trying to make this "
                                                       "more efficient for users, so we are collecting data on how "
                                                       "people do this and are feeding the data into a machine learning"
                                                       " algorithm. This laptop will record your exact mouse movements,"
                                                       " keyboard strokes, and precise timing to create a model of the"
                                                       " work you need to do to rename files. How quickly you can do"
                                                       " this is not important, so do not worry about performance. "
                                                       "Machine learning algorithms require a great deal of data, hence"
                                                       " the need to do this repeatedly.", nao)

        self.knowHow = SpeechButton("KnowHow?", "Do you know how to rename a file?", nao)
        self.great = SpeechButton("Great", "Great!", nao)
        self.thatsOkay = SpeechButton("That's okay.", "That is okay, I will explain.", nao)
        self.openFolder = SpeechButton("Open Folder", "Please open the folder called Experiment on the desktop.", nao)
        self.rightClick = SpeechButton("Right click", "Right click on the first file and press: re-name", nao)

        self.change = SpeechButton("Change", "Change the last part of the file name that says: dot, jay pee gee, to "
                                             "dot, pee n gee. For example: A file called robot, dot, jay pee g, should"
                                             " be renamed to robot, dot, pee n gee.", nao)

        self.enter = SpeechButton("Enter", "Then, press enter or click somewhere else in the folder.", nao)
        self.understand = SpeechButton("Understand?", "Do you understand how to rename a file?", nao)

        self.good = SpeechButton("Good", "Good. Please continue to do this for each file in the folder, and let me know"
                                         " when you are done.", nao)

        self.shortcuts = SpeechButton("Shortcuts.", "Because we are measuring precise keystrokes and mouse movements,"
                                                    " please do not use shortcuts such as copy and paste, as this may"
                                                    " confuse the machine learning system.", nao)

        self.a = SpeechButton("I'll add next", "Good. I will now add the next set of files.", nao)
        self.b = SpeechButton("Are you finished?", "Are you finished renaming the files?", nao)
        self.c = SpeechButton("Do you see the files?", "Do you see the files?", nao)
        self.d = SpeechButton("Try F5", "Try pressing F5 on the keyboard.", nao)

        self.data = SpeechButton("Data", "It is important to get as much data as we can for the machine learning"
                                         " system. As you can see on the white board to my right, there are four tasks"
                                         " in total in this experiment. For each one, we can go as long as you want"
                                         " before moving on to the next task. You can quit whenever you'd like. It is"
                                         " up to you how much data you give us. You, are in control. Let us know when"
                                         " you think you are done, and would like to move on to the next task.", nao)

        self.fifty = SpeechButton("50-100", "This set contains 50 files. The next set will contain 100 files.", nao)
        self.hundred = SpeechButton("100-500", "This set contains 100 files. The next set will contain 500 files.", nao) 
        self.fiveHundred = SpeechButton("500-1000", "This set contains 500 files. The next set will contain 1000 files.", nao) 
        self.thousand = SpeechButton("1000-5000", "This set contains 1000 files. The next set will contain 5000 files.", nao) 
        self.tryClose = SpeechButton("Try closing folder", "Try closing the folder and opening it up again.", nao)
        self.done = SpeechButton("Done", "Thank you, that should be good for now.", nao)
        self.nextTask = SpeechButton("nextTask", "We will now move onto the next task.", nao)

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
        hbox1.addWidget(self.understand)
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
    #END Tedium()


class MentalChallenge (QtGui.QWidget):
    def __init__(self, nao, parent):
        super(MentalChallenge, self).__init__()
        self.nao = nao
        self.parent = parent

        self.findCube = SpeechButton("Find Cube", "Please look behind your monitor and take out the Rubik's cube.", nao)

        self.explanation = SpeechButton("Explanation", "Currently, computers are not very good at solving Rubik's "
                                                       "Cubes. Computers can brute force the problem or use simple "
                                                       "tricks, but humans are able to solve the problem much more "
                                                       "organically. Because we can not represent the complex "
                                                       "neurological processes of a human brain in a computer, we can "
                                                       "use some algorithms to learn from peoples' actions. The web cam"
                                                       " on the laptop is going to record your movements and learn from"
                                                       " your experience. It does not matter whether or not you can "
                                                       "solve the cube because all data, successes and failures, is "
                                                       "useful to the algorithm. Please do not feel pressured: most "
                                                       "people are not able to solve these puzzles. Approach this as a"
                                                       " game and simply enjoy the puzzle, but do try your best to "
                                                       "solve it." , nao)

        self.camera = SpeechButton("Turn on camera", "I will now turn on the camera.", nao)

        self.turn = SpeechButton("Turn towards camera", "Please turn towards the blue light, and keep your hands in the"
                                                        " general direction of the light.", nao)

        self.good = SpeechButton("Good", "Good.", nao)
        self.handsUp = SpeechButton("Move hands up", "Please move your hands up a bit.", nao)
        self.handsDown = SpeechButton("Move hands down", "Please move your hands down a bit.", nao)

        self.positionHands = SpeechButton("Position hands", "Please position your hands more in the direction of "
                                                            "the camera.", nao)

        self.solve = SpeechButton("Solve cube.", "Now, please try solving the cube.", nao)

        self.data = SpeechButton("Data", "It is important to get as much data as we can for the machine learning "
                                         "system. We will do this as long as you can, but, let me know when you're "
                                         "done.", nao)

        self.mixUp = SpeechButton("Mix up and try again.", "Good. Now, please mix up the cube and solve it again. "
                                                           "Continue to do so each time you solve it.", nao)

        self.done = SpeechButton("Done", "Thank you, that should be good for now.", nao)

        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.findCube)
        layout.addWidget(self.explanation)
        layout.addWidget(self.camera)
        layout.addWidget(self.turn)
        layout.addWidget(self.good)
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


class TaskTabs (QtGui.QTabWidget):
    def __init__(self, nao, parent):
        self.parent = parent
        self.nao = nao
        super(TaskTabs, self).__init__()
        self.init()
    #END __init__()

    def init(self):
        self.setWindowTitle('Buttons')
        
        self.addTab(General(self.nao, self.parent), 'Pre-Experiment')
        self.addTab(Tedium(self.nao, self.parent), 'Tedium')
        self.addTab(MentalChallenge(self.nao, self.parent), 'Mental Challenge')
    #END init()
#END TaskTabs

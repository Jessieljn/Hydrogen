from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Speech
from UI.ActionPushButton import ActionPushButton


class Tedium(QtGui.QWidget):
    def __init__(self):
        super(Tedium, self).__init__()
        self._actionQueue = None
        self._nao = None
        self._widgets = None
        self._buttons = None
        self._btnLeft = []
        self._btnRight = []

        self._btnLeft.append([
            ActionPushButton(None, "Prod1", Speech("Please, continue. We need more data.", 100)),
            ActionPushButton(None, "Prod2", Speech("We hahvent collected enough data yet.", 100)),
            ActionPushButton(None, "Prod3", Speech("Its essential that you continue.", 100)),
            ActionPushButton(None, "Prod4", Speech("The experiment requires that you continue.", 100)),
            None,
            ActionPushButton(None, "I'll add next", Speech("I will now add the next set of files.", 90)),
            ActionPushButton(None, "This 50, next 100", Speech("This set contains 50 files. The next set will contain 100 files.", 90)),
            ActionPushButton(None, "This 100, next 500", Speech("This set contains 100 files. The next set will contain 500 files.", 90)),
            ActionPushButton(None, "This 500, next 1000", Speech("This set contains 500 files. The next set will contain 1000 files.", 90)),
            ActionPushButton(None, "This 1000, next 5000", Speech("This set contains 1000 files. The next set will contain 5000 files.", 90)),
        ])
        self._btnLeft.append([
            ActionPushButton(None, "Thank you", Speech("Thank you.", 100)),
            ActionPushButton(None, "Sorry", Speech("Sorry.", 100)),
            ActionPushButton(None, "Okay", Speech("Okay.", 100)),
            ActionPushButton(None, "Yes", Speech("Yes.", 100)),
            ActionPushButton(None, "No", Speech("No.", 100)),
            None,
            ActionPushButton(None, "Questions", Speech("Please hold all questions until the end of the experiment", 90)),
            ActionPushButton(None, "Say Again?", Speech("Can you say that one more time?", 100)),
            ActionPushButton(None, "Repeat?", Speech("Would you like me to repeat that?", 100)),
            ActionPushButton(None, "Understand?", Speech("Do you understand?.", 100)),
            ActionPushButton(None, "Didn't Understand", Speech("I did not understand.", 100)),
            None,
            ActionPushButton(None, "Louder", Speech("Can you please speak louder?", 100)),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
        ])
        self._btnLeft.append([
            ActionPushButton(None, "Try Closing Folder", Speech("Try closing the folder and opening it up again.", 90)),
            ActionPushButton(None, "Try F5", Speech("Try pressing F5 on the keyboard.", 100)),
            ActionPushButton(None, "See Files?", Speech("Do you see the files?", 100)),
            ActionPushButton(None, "Finished?", Speech("Are you finished renaming the files?", 100)),
        ])

        self._btnRight.append([
            ActionPushButton(None, "Greeting", Speech("Hello", 100)),
            ActionPushButton(None, "Hello", Speech("Hello. Thank you for coming. Please remember that you can leave at any time. If you have any specific questions not related to the tasks, please hold them until after the experiment is complete; I will be happy to answer any of your questions afterwards. If you are uncomfortable with this, please remember that you can leave at any time. The cash honorarium is yours to keep, even if you choose not to continue to the end.", 90)),
            ActionPushButton(None, "Demographics", Speech("Before we begin, please take a seat at the computer and open the blue folder in front of you. Inside you will find a demographics questionnaire. Please fill it out and let me know when you are finished.", 90)),
            ActionPushButton(None, "Data", Speech("It is important to get as much data as we can for the machine learning system. As you can see on the white board to my right, there are four tasks in total in this experiment. For each one, we can go as long as you want before moving on to the next task. You can quit whenever you'd like. It is up to you how much data you give us. You, are in control. Let me know when you think you are done, and would like to move on to the next task.", 90)),
            ActionPushButton(None, "Intro", Speech("Currently, the process of renaming files in a graphical user interface is not very efficient. We are trying to make this more efficient for users, so we are collecting data on how people do this and are feeding the data into a machine learning algorithm. This computer will record your exact mouse movements, keyboard strokes, and precise timing to create a model of the work you need to do to rename files. How quickly you can do this, is not important, so do not worry about performance. Machine learning algorithms require a great deal of data, hence the need to do this repeatedly.", 90)),
            ActionPushButton(None, "Know How?", Speech("Do you know how to rename a file?", 90)),
            ActionPushButton(None, "Open Folder", Speech("Please open the folder called Experiment on the desktop.", 90)),
            ActionPushButton(None, "Right Click", Speech("Right click on the first file and press: re-name", 90)),
            ActionPushButton(None, "Change", Speech("Change the last part of the file name that says: dot, jay pee gee, to dot, pee n gee. For example: A file called robot, dot, jay pee gee, should be renamed to robot, dot, pee n gee.", 90)),
            ActionPushButton(None, "Enter", Speech("Then, press enter or click somewhere else in the folder.", 90)),
            ActionPushButton(None, "Good", Speech("Good. Please continue to do this for each file in the folder, and let me know when you are done.", 90)),
            ActionPushButton(None, "Shortcuts", Speech("Because we are measuring precise keystrokes and mouse movements, please do not use shortcuts such as copy and paste, as this may confuse the machine learning system.", 90)),
            ActionPushButton(None, "Over", Speech("We will end the experiment now. Please wait a moment while I notify the research assistant that you are done.", 90)),
            ActionPushButton(None, "On The Way", Speech("The research assistant is on her way. Please wait for her to get here.", 90)),
            None,
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            ActionPushButton(None, "Great!", Speech("Great!", 100)),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            None,
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            ActionPushButton(None, "That's Okay", Speech("That's okay, I will explain.", 90)),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
            QtGui.QLabel(""),
        ])

        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)

        wgtLeft = QtGui.QWidget(splitter)
        layoutLeft = QtGui.QVBoxLayout(wgtLeft)
        layoutLeft.setMargin(6)
        layoutLeft.addSpacing(3)
        for buttons in self._btnLeft:
            layoutLeft.addSpacerItem(QtGui.QSpacerItem(100, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))
            widget = QtGui.QWidget(wgtLeft)
            layout = QtGui.QHBoxLayout(widget)
            layout.setMargin(0)
            layout.addSpacing(6)
            for item in buttons:
                if item is None:
                    layoutLeft.addWidget(widget)
                    widget = QtGui.QWidget(wgtLeft)
                    layout = QtGui.QHBoxLayout(widget)
                    layout.setMargin(0)
                    layout.addSpacing(6)
                else:
                    item.setParent(widget)
                    if isinstance(item, QtGui.QPushButton):
                        item.clicked.connect(self.on_button_clicked)
                    #END if
                    layout.addWidget(item)
                #END if
            #END for
            layoutLeft.addWidget(widget)
            layoutLeft.addSpacerItem(QtGui.QSpacerItem(100, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))
        #END for

        wgtRight = QtGui.QWidget(splitter)
        layoutRight = QtGui.QHBoxLayout(wgtRight)
        layoutRight.setMargin(6)
        layoutRight.addSpacing(3)
        for buttons in self._btnRight:
            layoutLeft.addSpacerItem(QtGui.QSpacerItem(100, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))
            widget = QtGui.QWidget(wgtRight)
            layout = QtGui.QVBoxLayout(widget)
            layout.setMargin(0)
            layout.addSpacing(6)
            for item in buttons:
                if item is None:
                    layoutRight.addWidget(widget)
                    widget = QtGui.QWidget(wgtRight)
                    layout = QtGui.QVBoxLayout(widget)
                    layout.setMargin(0)
                    layout.addSpacing(6)
                else:
                    item.setParent(widget)
                    if isinstance(item, QtGui.QPushButton):
                        item.clicked.connect(self.on_button_clicked)
                    #END if
                    layout.addWidget(item)
                #END if
            #END for
            layoutRight.addWidget(widget)
            layoutLeft.addSpacerItem(QtGui.QSpacerItem(100, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))
        #END for
    #END __init__()
<<<<<<< HEAD
#END Tedium.py
=======

    def LEDActive(self):
        if self._nao is not None:
            self._nao.LEDrandomEyes(1.0, True)
        #END if
    #END LEDActive()

    def LEDNormal(self):
        if self._nao is not None:
            self._nao.LEDNormal()
        #END if
    #END LEDNormal()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self.on_nao_connected)
            self._nao.disconnected.disconnect(self.on_nao_disconnected)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self.on_nao_connected)
            self._nao.disconnected.connect(self.on_nao_disconnected)
        #END if
    #END setNao()

    def speech(self, txt, speed, shaping):
        return None
    #END speech()

    def on_button_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_button_clicked()

    def on_nao_connected(self):
        pass
    #END on_nao_connected()

    def on_nao_disconnected(self):
        pass
    #END on_nao_disconnected()
#END class
>>>>>>> c539eda38437b33d39c4b7b378e3dfec66508a5c

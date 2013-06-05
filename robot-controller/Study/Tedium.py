from PyQt4 import QtGui
from Action.Speech import Speech
from UI.ActionPushButton import ActionPushButton


class Tedium(QtGui.QWidget):
    def __init__(self):
        super(Tedium, self).__init__()
        self._actionQueue = None

        self.explanation = ActionPushButton(self, "Explanation", Speech("Currently, the process of renaming files in a "
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
                                                                "this repeatedly."))
        self.explanation.execute.connect(self.on_actionReceived)

        self.knowHow = ActionPushButton(self, "Know How?", Speech("Do you know how to rename a file?"))
        self.knowHow.execute.connect(self.on_actionReceived)

        self.great = ActionPushButton(self, "Great", Speech("Great!"))
        self.great.execute.connect(self.on_actionReceived)

        self.thatsOkay = ActionPushButton(self, "That's Okay.", Speech("That is okay, I will explain."))
        self.thatsOkay.execute.connect(self.on_actionReceived)

        self.openFolder = ActionPushButton(self, "Open Folder", Speech("Please open the folder called Experiment on the desktop."))
        self.openFolder.execute.connect(self.on_actionReceived)

        self.rightClick = ActionPushButton(self, "Right click", Speech("Right click on the first file and press: re-name"))
        self.rightClick.execute.connect(self.on_actionReceived)

        self.change = ActionPushButton(self, "Change", Speech("Change the last part of the file name that says: dot, jay"
                                                      " pee gee, to dot, pee n gee. For example: A file called robot,"
                                                      " dot, jay pee g, should be renamed to robot, dot, pee n gee."))
        self.change.execute.connect(self.on_actionReceived)

        self.enter = ActionPushButton(self, "Enter", Speech("Then, press enter or click somewhere else in the folder."))
        self.enter.execute.connect(self.on_actionReceived)

        self.good = ActionPushButton(self, "Good", Speech("Good. Please continue to do this for each file in the folder, and"
                                                  " let me know when you are done."))
        self.good.execute.connect(self.on_actionReceived)

        self.shortcuts = ActionPushButton(self, "Shortcuts.", Speech("Because we are measuring precise keystrokes and mouse "
                                                             "movements, please do not use shortcuts such as copy and "
                                                             "paste, as this may confuse the machine learning system."))
        self.shortcuts.execute.connect(self.on_actionReceived)

        self.a = ActionPushButton(self, "I'll Add Next", Speech("Good. I will now add the next set of files."))
        self.a.execute.connect(self.on_actionReceived)
        self.b = ActionPushButton(self, "Are You Finished?", Speech("Are you finished renaming the files?"))
        self.b.execute.connect(self.on_actionReceived)
        self.c = ActionPushButton(self, "Do You See The Files?", Speech("Do you see the files?"))
        self.c.execute.connect(self.on_actionReceived)
        self.d = ActionPushButton(self, "Try F5", Speech("Try pressing F5 on the keyboard."))
        self.d.execute.connect(self.on_actionReceived)

        self.data = ActionPushButton(self, "Data", Speech("It is important to get as much data as we can for the machine "
                                                  "learning system. As you can see on the white board to my right, "
                                                  "there are four tasks in total in this experiment. For each one, we "
                                                  "can go as long as you want before moving on to the next task. You "
                                                  "can quit whenever you'd like. It is up to you how much data you give"
                                                  " us. You, are in control. Let us know when you think you are done,"
                                                  " and would like to move on to the next task."))
        self.data.execute.connect(self.on_actionReceived)

        self.fifty = ActionPushButton(self, "This Set Has 50, Next Has 100", Speech("This set contains 50 files. The next set"
                                                                            " will contain 100 files."))
        self.fifty.execute.connect(self.on_actionReceived)

        self.hundred = ActionPushButton(self, "This Set Has 100, Next Has 500", Speech("This set contains 100 files. The next "
                                                                               "set will contain 500 files."))
        self.hundred.execute.connect(self.on_actionReceived)

        self.fiveHundred = ActionPushButton(self, "This Set Has 500, Next Has 1000", Speech("This set contains 500 files. "
                                                                                    "The next set will contain 1000 files."))
        self.fiveHundred.execute.connect(self.on_actionReceived)

        self.thousand = ActionPushButton(self, "This Set Has 1000, Next Has 5000 ", Speech("This set contains 1000 files. The "
                                                                                   "next set will contain 5000 files."))
        self.thousand.execute.connect(self.on_actionReceived)

        self.tryClose = ActionPushButton(self, "Try Closing Folder", Speech("Try closing the folder and opening it up again."))
        self.tryClose.execute.connect(self.on_actionReceived)

        self.done = ActionPushButton(self, "Done", Speech("Thank you, that should be good for now."))
        self.done.execute.connect(self.on_actionReceived)

        self.nextTask = ActionPushButton(self, "Next Task", Speech("We will now move onto the next task."))
        self.nextTask.execute.connect(self.on_actionReceived)

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

        layout = QtGui.QHBoxLayout(self)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
    #END __init__()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    #END on_actionReceived()
#END class

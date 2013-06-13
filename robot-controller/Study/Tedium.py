from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action import Speech
from UI.ActionPushButton import ActionPushButton


class Tedium(BaseStudy):
    def __init__(self):
        super(Tedium, self).__init__()
        self._widgets = []
        self._buttons = []

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Explanation",
                    Speech("Currently, the process of renaming files in a graphical user interface is not very efficient."
                           "We are trying to make this more efficient for users, so "
                           "we are collecting data on how people do this and are "
                           "feeding the data into a machine learning algorithm. "
                           "This laptop will record your exact mouse movements, "
                           "keyboard strokes, and precise timing to create a model"
                           " of the work you need to do to rename files. How "
                           "quickly you can do this is not important, so do not "
                           "worry about performance. Machine learning algorithms "
                           "require a great deal of data, hence the need to do this repeatedly.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Know How?", Speech("Do you know how to rename a file?")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Great", Speech("Great!")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "That's Okay.", Speech("That is okay, I will explain.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Open Folder", Speech("Please open the folder called Experiment on the desktop.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Right click", Speech("Right click on the first file and press: re-name")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Change",
                     Speech("Change the last part of the file name that says: dot, jay"
                            " pee gee, to dot, pee n gee. For example: A file called robot,"
                            " dot, jay pee g, should be renamed to robot, dot, pee n gee.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Enter", Speech("Then, press enter or click somewhere else in the folder.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Good", Speech("Good. Please continue to do this for each file in the folder, and let me know when you are done.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Data",
                     Speech("It is important to get as much data as we can for the machine "
                            "learning system. As you can see on the white board to my right, "
                            "there are four tasks in total in this experiment. For each one, we "
                            "can go as long as you want before moving on to the next task. You "
                            "can quit whenever you'd like. It is up to you how much data you give"
                            " us. You, are in control. Let us know when you think you are done,"
                            " and would like to move on to the next task.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Shortcuts",
                     Speech("Because we are measuring precise keystrokes and mouse "
                            "movements, please do not use shortcuts such as copy and "
                            "paste, as this may confuse the machine learning system.")),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I'll Add Next", Speech("Good. I will now add the next set of files.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "This Set Has 50, Next Has 100", Speech("This set contains 50 files. The next set will contain 100 files.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "This Set Has 100, Next Has 500", Speech("This set contains 100 files. The next set will contain 500 files.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "This Set Has 500, Next Has 1000", Speech("This set contains 500 files. The next set will contain 1000 files.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "This Set Has 1000, Next Has 5000 ", Speech("This set contains 1000 files. The next set will contain 5000 files.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Try Closing Folder", Speech("Try closing the folder and opening it up again.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Are You Finished?", Speech("Are you finished renaming the files?")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Do You See The Files?", Speech("Do you see the files?")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Try F5", Speech("Try pressing F5 on the keyboard.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Done", Speech("Thank you, that should be good for now.")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Next Task", Speech("We will now move onto the next task.")),
        ])

        self._setupUi(True)
    #END __init__()
#END class

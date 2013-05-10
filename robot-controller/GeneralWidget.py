from PyQt4 import QtGui
import TaskTabs


##
# GeneralWidget.py
#
# Creates the General Widget in the GUI, used for speech.
##
class GeneralWidget (QtGui.QGroupBox):
    def __init__(self, nao, parent):
        super(GeneralWidget, self).__init__()
        self.setTitle("General Speech")
        self.nao = nao
        self.parent = parent

        # Create different speech buttons.
        self.hello = TaskTabs.SpeechButton("Hello", "Hello", nao)
        self.louder = TaskTabs.SpeechButton("Louder", "Please speak louder", nao)
        self.thanks = TaskTabs.SpeechButton("Thanks", "Thank you", nao)
        self.good = TaskTabs.SpeechButton("Good", "Good", nao)
        self.okay = TaskTabs.SpeechButton("Okay", "Okay", nao)
        self.repeat = TaskTabs.SpeechButton("Repeat", "Would you like me to repeat that?", nao)
        self.understand = TaskTabs.SpeechButton("Understand", "Do you understand", nao)
        self.greeting = TaskTabs.SpeechButton("Greeting", "Hello, my name is NAO, nice to meet you", nao)
        self.end = TaskTabs.SpeechButton("End Experiment", "Thank you for participating in our experiment", nao)
        self.sound = TaskTabs.SpeechButton("Hmmm", "Hmmm", nao)

        # Maximum Widths
        self.hello.setMaximumWidth(150)
        self.louder.setMaximumWidth(150)
        self.thanks.setMaximumWidth(150)
        self.good.setMaximumWidth(150)
        self.okay.setMaximumWidth(150)
        self.repeat.setMaximumWidth(150)
        self.understand.setMaximumWidth(150)
        self.greeting.setMaximumWidth(150)
        self.end.setMaximumWidth(150)
        self.sound.setMaximumWidth(150)

        layout = QtGui.QVBoxLayout()

        # Adding widgets to the horizontal box 1.
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.hello)
        hbox.addWidget(self.thanks)
        hbox.addWidget(self.okay)
        hbox.addWidget(self.understand)
        hbox.addWidget(self.greeting)

        # Adding widgets to horizontal box 2.
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.louder)
        hbox2.addWidget(self.good)
        hbox2.addWidget(self.repeat)
        hbox2.addWidget(self.end)
        hbox2.addWidget(self.sound)

        # Adding boxes to the layout.
        layout.addLayout(hbox)
        layout.addLayout(hbox2)

        # Setting the layout.
        self.setLayout(layout)
    #END __init__()

    def sayProd(self):
        self.nao.say(str(self.sender().text()))
    #END sayProd()

    def say_nextTask(self):
        self.nao.say("Why don't we move onto the next task?")
    #END say_nextTask()

    def say_endExperiment(self):
        self.nao.say("In that case, we will end the experiment now. Please wait a moment while I notify the "
                     "lead researcher that we are done.")
    #END say_endExperiment()

    def say_researcherComing(self):
        self.nao.say("The researcher is on his way to give you the debriefing. Please wait a moment.")
    #END say_researcherComing()

    def say_repeat(self):
        self.nao.say("I didn't quite hear you. Can you please say that again?")
    #END say_repeat()

    def say_speakLouder(self):
        self.nao.say("Please speak louder.")
    #END say_speakLouder()
#END GeneralWidget
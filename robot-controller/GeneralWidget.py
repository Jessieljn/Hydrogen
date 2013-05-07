from PyQt4 import QtGui


##
# GeneralWidget.py
#
# Creates the general layout of the GUI.
##
class GeneralWidget (QtGui.QGroupBox):
    def __init__(self, nao, parent):
        super(GeneralWidget, self).__init__()
        self.setTitle("General")

        self.nao = nao

        self.prod1 = QtGui.QPushButton("Prod 1")
        self.prod2 = QtGui.QPushButton("Prod 2")
        self.prod3 = QtGui.QPushButton("Prod 3")
        self.prod4 = QtGui.QPushButton("Prod 4")
        self.introduce = QtGui.QPushButton("Introduce")
        self.nextTask = QtGui.QPushButton("Next Task?")
        self.endExperiment = QtGui.QPushButton("End Experiment")
        self.debrief = QtGui.QPushButton("Debrief")
        self.repeat = QtGui.QPushButton("Please Repeat")
        self.louder = QtGui.QPushButton("Speak Louder")
        self.yes = QtGui.QPushButton("Yes")
        self.no = QtGui.QPushButton("No")
        self.good = QtGui.QPushButton("Good")
        self.processing = QtGui.QPushButton("Processing Response")
        self.saveQuestions = QtGui.QPushButton("Please save your questions for later.")

        self.prod1.clicked.connect(self.nao.prod1)
        self.prod2.clicked.connect(self.nao.prod2)
        self.prod3.clicked.connect(self.nao.prod3)
        self.prod4.clicked.connect(self.nao.prod4)
        self.nextTask.clicked.connect(self.say_nextTask)
        self.endExperiment.clicked.connect(self.say_endExperiment)
        self.debrief.clicked.connect(self.say_researcherComing)
        self.repeat.clicked.connect(self.say_repeat)
        self.introduce.clicked.connect(self.nao.introduce)
        self.louder.clicked.connect(self.say_speakLouder)
        self.yes.clicked.connect(self.sayProd)
        self.no.clicked.connect(self.sayProd)
        self.good.clicked.connect(self.sayProd)
        self.processing.clicked.connect(self.sayProd)
        self.saveQuestions.clicked.connect(self.sayProd)

        self.prod1.setMaximumWidth(150)
        self.prod2.setMaximumWidth(150)
        self.prod3.setMaximumWidth(150)
        self.prod4.setMaximumWidth(150)
        self.introduce.setMaximumWidth(150)
        self.nextTask.setMaximumWidth(150)
        self.endExperiment.setMaximumWidth(150)
        self.debrief.setMaximumWidth(150)
        self.repeat.setMaximumWidth(150)
        self.louder.setMaximumWidth(150)
        self.yes.setMaximumWidth(150)
        self.no.setMaximumWidth(150)
        self.good.setMaximumWidth(150)
        self.processing.setMaximumWidth(150)

        #Uncomment to set a maximum width for the buttons.
        #self.saveQuestions.setMaximumWidth(150)

        layout = QtGui.QVBoxLayout()

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.prod1)
        hbox.addWidget(self.prod2)
        hbox.addWidget(self.prod3)
        hbox.addWidget(self.prod4)
        hbox.addWidget(self.introduce)
        hbox.addWidget(self.nextTask)
        hbox.addWidget(self.endExperiment)
        hbox.addWidget(self.debrief)

        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.repeat)
        hbox2.addWidget(self.louder)
        hbox2.addWidget(self.good)
        hbox2.addWidget(self.yes)
        hbox2.addWidget(self.no)
        hbox2.addWidget(self.processing)
        hbox2.addWidget(self.saveQuestions)

        layout.addLayout(hbox)
        layout.addLayout(hbox2)

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
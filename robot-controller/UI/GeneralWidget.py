from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Action
from Action import Behavior
from Action import Speech
from ActionPushButton import ActionPushButton


##
# GeneralWidget.py
#
# Creates the General Widget in the GUI
##
class GeneralWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(GeneralWidget, self).__init__(parent)

        ##################################################
        # General Speech
        ##################################################
        self.hello = ActionPushButton(self, "Hello", Speech("Hello"))
        self.hello.setMaximumWidth(150)
        self.hello.clicked.connect(self.on_button_clicked)
        self.louder = ActionPushButton(self, "Louder", Speech("Please speak louder"))
        self.louder.setMaximumWidth(150)
        self.louder.clicked.connect(self.on_button_clicked)
        self.thanks = ActionPushButton(self, "Thanks", Speech("Thank you"))
        self.thanks.setMaximumWidth(150)
        self.thanks.clicked.connect(self.on_button_clicked)
        self.good = ActionPushButton(self, "Good", Speech("Good"))
        self.good.setMaximumWidth(150)
        self.good.clicked.connect(self.on_button_clicked)
        self.okay = ActionPushButton(self, "Okay", Speech("Okay"))
        self.okay.setMaximumWidth(150)
        self.okay.clicked.connect(self.on_button_clicked)
        self.repeat = ActionPushButton(self, "Repeat", Speech("Would you like me to repeat that?"))
        self.repeat.setMaximumWidth(150)
        self.repeat.clicked.connect(self.on_button_clicked)
        self.understand = ActionPushButton(self, "Understand", Speech("Do you understand"))
        self.understand.setMaximumWidth(150)
        self.understand.clicked.connect(self.on_button_clicked)
        self.greeting = ActionPushButton(self, "Greeting", Speech("Hello, my name is NAO, nice to meet you"))
        self.greeting.setMaximumWidth(150)
        self.greeting.clicked.connect(self.on_button_clicked)
        self.end = ActionPushButton(self, "End Experiment", Speech("Thank you for participating in our experiment"))
        self.end.setMaximumWidth(150)
        self.end.clicked.connect(self.on_button_clicked)
        self.sound = ActionPushButton(self, "Hmmm", Speech("Hmmm"))
        self.sound.setMaximumWidth(150)
        self.sound.clicked.connect(self.on_button_clicked)

        speechHBox = QtGui.QHBoxLayout()
        speechHBox.addWidget(self.hello)
        speechHBox.addWidget(self.thanks)
        speechHBox.addWidget(self.okay)
        speechHBox.addWidget(self.understand)
        speechHBox.addWidget(self.greeting)

        speechHBox2 = QtGui.QHBoxLayout()
        speechHBox2.addWidget(self.louder)
        speechHBox2.addWidget(self.good)
        speechHBox2.addWidget(self.repeat)
        speechHBox2.addWidget(self.end)
        speechHBox2.addWidget(self.sound)

        self._grpSpeech = QtGui.QGroupBox()
        self._grpSpeech.setTitle("General Speech")
        layoutSpeech = QtGui.QVBoxLayout(self._grpSpeech)
        layoutSpeech.addLayout(speechHBox)
        layoutSpeech.addLayout(speechHBox2)

        ##################################################
        # General Motions
        ##################################################
        self.stand = ActionPushButton(self, "Stand Up", Behavior("StandUp"))
        self.stand.clicked.connect(self.on_button_clicked)
        self.sit = ActionPushButton(self, "Sit Down", Behavior("SitDown"))
        self.sit.clicked.connect(self.on_button_clicked)
        self.taiChi = ActionPushButton(self, "Tai Chi", Behavior("TaiChi"))
        self.taiChi.clicked.connect(self.on_button_clicked)
        self.handShake = ActionPushButton(self, "Hand Shake", Behavior("ShakeHand"))
        self.handShake.clicked.connect(self.on_button_clicked)
        self.thriller = ActionPushButton(self, "Thriller", Behavior("thriller"))
        self.thriller.clicked.connect(self.on_button_clicked)
        self.wave = ActionPushButton(self, "Wave", Behavior("wave"))
        self.wave.clicked.connect(self.on_button_clicked)
        self.introduce = ActionPushButton(self, "Introduce", Behavior("introduce"))
        self.introduce.clicked.connect(self.on_button_clicked)

        behaviorHBox = QtGui.QHBoxLayout()
        behaviorHBox.addSpacing(10)
        behaviorHBox.addWidget(self.stand, 0, QtCore.Qt.AlignCenter)
        behaviorHBox.addWidget(self.sit, 0, QtCore.Qt.AlignCenter)
        behaviorHBox.addWidget(self.taiChi, 0, QtCore.Qt.AlignCenter)
        behaviorHBox.addWidget(self.handShake, 0, QtCore.Qt.AlignCenter)
        behaviorHBox.addWidget(self.thriller, 0, QtCore.Qt.AlignCenter)

        behaviorHBox2 = QtGui.QHBoxLayout()
        behaviorHBox2.addWidget(self.wave, 0, QtCore.Qt.AlignCenter)
        behaviorHBox2.addWidget(self.introduce, 0, QtCore.Qt.AlignCenter)

        self._grpBehaviors = QtGui.QGroupBox()
        self._grpBehaviors.setTitle("General Behaviors")
        layoutBehavior = QtGui.QVBoxLayout(self._grpBehaviors)
        layoutBehavior.addLayout(behaviorHBox)
        layoutBehavior.addLayout(behaviorHBox2)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._grpSpeech)
        layoutMain.addWidget(self._grpBehaviors)
    #END __init__()

    playAction = QtCore.pyqtSignal(Action)

    def on_button_clicked(self):
        for action in self.sender().getRobotActions():
            self.playAction.emit(action)
        #END for
    #END on_button_clicked()
#END GeneralWidget

from PyQt4 import QtCore, QtGui
from Action.Action import Action
from Action.Behavior import Behavior
from Action.Speech import Speech
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
        self.hello.execute.connect(self.on_actionReceived)
        self.louder = ActionPushButton(self, "Louder", Speech("Please speak louder"))
        self.louder.setMaximumWidth(150)
        self.louder.execute.connect(self.on_actionReceived)
        self.thanks = ActionPushButton(self, "Thanks", Speech("Thank you"))
        self.thanks.setMaximumWidth(150)
        self.thanks.execute.connect(self.on_actionReceived)
        self.good = ActionPushButton(self, "Good", Speech("Good"))
        self.good.setMaximumWidth(150)
        self.good.execute.connect(self.on_actionReceived)
        self.okay = ActionPushButton(self, "Okay", Speech("Okay"))
        self.okay.setMaximumWidth(150)
        self.okay.execute.connect(self.on_actionReceived)
        self.repeat = ActionPushButton(self, "Repeat", Speech("Would you like me to repeat that?"))
        self.repeat.setMaximumWidth(150)
        self.repeat.execute.connect(self.on_actionReceived)
        self.understand = ActionPushButton(self, "Understand", Speech("Do you understand"))
        self.understand.setMaximumWidth(150)
        self.understand.execute.connect(self.on_actionReceived)
        self.greeting = ActionPushButton(self, "Greeting", Speech("Hello, my name is NAO, nice to meet you"))
        self.greeting.setMaximumWidth(150)
        self.greeting.execute.connect(self.on_actionReceived)
        self.end = ActionPushButton(self, "End Experiment", Speech("Thank you for participating in our experiment"))
        self.end.setMaximumWidth(150)
        self.end.execute.connect(self.on_actionReceived)
        self.sound = ActionPushButton(self, "Hmmm", Speech("Hmmm"))
        self.sound.setMaximumWidth(150)
        self.sound.execute.connect(self.on_actionReceived)

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
        self.stand.execute.connect(self.on_actionReceived)
        self.sit = ActionPushButton(self, "Sit Down", Behavior("SitDown"))
        self.sit.execute.connect(self.on_actionReceived)
        self.taiChi = ActionPushButton(self, "Tai Chi", Behavior("TaiChi"))
        self.taiChi.execute.connect(self.on_actionReceived)
        self.handShake = ActionPushButton(self, "Hand Shake", Behavior("shakeHand"))
        self.handShake.execute.connect(self.on_actionReceived)
        self.thriller = ActionPushButton(self, "Thriller", Behavior("thriller"))
        self.thriller.execute.connect(self.on_actionReceived)
        self.wave = ActionPushButton(self, "Wave", Behavior("wave"))
        self.wave.execute.connect(self.on_actionReceived)
        self.introduce = ActionPushButton(self, "Introduce", Behavior("introduce"))
        self.introduce.execute.connect(self.on_actionReceived)

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

    def on_actionReceived(self, action):
        self.playAction.emit(action)
    #END on_actionReceived()
#END GeneralWidget

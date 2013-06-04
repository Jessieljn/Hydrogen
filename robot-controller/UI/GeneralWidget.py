from PyQt4 import QtCore, QtGui
from BehaviorPushButton import BehaviorPushButton
from SpeechPushButton import SpeechPushButton


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
        self.hello = SpeechPushButton(self, "Hello", "Hello")
        self.hello.setMaximumWidth(150)
        self.hello.execute.connect(self.on__SpeechButton_clicked)
        self.louder = SpeechPushButton(self, "Louder", "Please speak louder")
        self.louder.setMaximumWidth(150)
        self.louder.execute.connect(self.on__SpeechButton_clicked)
        self.thanks = SpeechPushButton(self, "Thanks", "Thank you")
        self.thanks.setMaximumWidth(150)
        self.thanks.execute.connect(self.on__SpeechButton_clicked)
        self.good = SpeechPushButton(self, "Good", "Good")
        self.good.setMaximumWidth(150)
        self.good.execute.connect(self.on__SpeechButton_clicked)
        self.okay = SpeechPushButton(self, "Okay", "Okay")
        self.okay.setMaximumWidth(150)
        self.okay.execute.connect(self.on__SpeechButton_clicked)
        self.repeat = SpeechPushButton(self, "Repeat", "Would you like me to repeat that?")
        self.repeat.setMaximumWidth(150)
        self.repeat.execute.connect(self.on__SpeechButton_clicked)
        self.understand = SpeechPushButton(self, "Understand", "Do you understand")
        self.understand.setMaximumWidth(150)
        self.understand.execute.connect(self.on__SpeechButton_clicked)
        self.greeting = SpeechPushButton(self, "Greeting", "Hello, my name is NAO, nice to meet you")
        self.greeting.setMaximumWidth(150)
        self.greeting.execute.connect(self.on__SpeechButton_clicked)
        self.end = SpeechPushButton(self, "End Experiment", "Thank you for participating in our experiment")
        self.end.setMaximumWidth(150)
        self.end.execute.connect(self.on__SpeechButton_clicked)
        self.sound = SpeechPushButton(self, "Hmmm", "Hmmm")
        self.sound.setMaximumWidth(150)
        self.sound.execute.connect(self.on__SpeechButton_clicked)

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
        self.stand = BehaviorPushButton(self, "Stand Up", "StandUp")
        self.stand.execute.connect(self.on__BehaviorButton_clicked)
        self.sit = BehaviorPushButton(self, "Sit Down", "SitDown")
        self.sit.execute.connect(self.on__BehaviorButton_clicked)
        self.taiChi = BehaviorPushButton(self, "Tai Chi", "TaiChi")
        self.taiChi.execute.connect(self.on__BehaviorButton_clicked)
        self.handShake = BehaviorPushButton(self, "Hand Shake", "shakeHand")
        self.handShake.execute.connect(self.on__BehaviorButton_clicked)
        self.thriller = BehaviorPushButton(self, "Thriller", "thriller")
        self.thriller.execute.connect(self.on__BehaviorButton_clicked)
        self.wave = BehaviorPushButton(self, "Wave", "wave")
        self.wave.execute.connect(self.on__BehaviorButton_clicked)
        self.introduce = BehaviorPushButton(self, "Introduce", "introduce")
        self.introduce.execute.connect(self.on__BehaviorButton_clicked)

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

    playBehavior = QtCore.pyqtSignal(str)
    speechSynthesis = QtCore.pyqtSignal(str)

    def on__BehaviorButton_clicked(self, motion):
        self.playBehavior.emit(motion)
    #END on__BehaviorButton_clicked()

    def on__SpeechButton_clicked(self, speech):
        self.speechSynthesis.emit(speech)
    #END on__SpeechButton_clicked()
#END GeneralWidget

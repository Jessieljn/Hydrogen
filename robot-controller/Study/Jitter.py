from PyQt4 import QtCore, QtGui
from BaseStudy import BaseStudy


class Jitter(BaseStudy):
    def __init__(self):
        super(Jitter, self).__init__()
        self.setWindowTitle("Jitter Function")

        widget = QtGui.QWidget()
        self.vbox = QtGui.QVBoxLayout(widget)   # General Box
        self.hbox1 = QtGui.QHBoxLayout()  # Start Frame Box
        self.hbox2 = QtGui.QHBoxLayout()  # End Frame Box

        self.motions = QtGui.QComboBox()
        self.behaviors = QtGui.QComboBox()
        self.motionLabel = QtGui.QLabel("HeadYaw")  # Add to vbox
        self.behaviorLabel = QtGui.QLabel("chinScratch")

        motionList = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw',
                      'LHand', 'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',
                      'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll',
                      'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']

        behaviorList = ['chinScratch', 'dance', 'hand', 'headNod']

        # - LHipYawPitch uses the same more as RHipYawPitch, they move simultaneously and symmetrically. In case of
        # conflicting orders, LHipYawPitch takes priority.

        # - LWristYaw, LHand, RWristYaw, RHand, do no exist in model "H21".
        self.motions.addItems(motionList)
        self.behaviors.addItems(behaviorList)

        # noinspection PyCallingNonCallable
        #self.nao = Nao()

        self._startFrame = QtGui.QLineEdit(widget)
        self._startFrame.setText('0')

        self._endFrame = QtGui.QLineEdit(widget)
        self._endFrame.setText('0')

        self._startLabel = QtGui.QLabel("Start Frame: ")
        self._endLabel = QtGui.QLabel("End Frame: ")

        self._addButton = QtGui.QPushButton('Add', widget)

        self.vbox.addWidget(self.behaviors)
        self.vbox.addWidget(self.motions)
        self.hbox1.addWidget(self._startLabel)
        self.hbox1.addWidget(self._startFrame)
        self.hbox2.addWidget(self._endLabel)
        self.hbox2.addWidget(self._endFrame)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self._addButton)

        self.connect(self.motions, QtCore.SIGNAL('activated(QString)'), self.motion_chosen)
        self.connect(self.behaviors, QtCore.SIGNAL('activated(QString)'), self.behavior_chosen)

        self.joints = [self.motionLabel.text(), self._startFrame.text(), self._endFrame.text()]

        # self._addButton.clicked.connect(self.nao.makeJitter(self.behaviorLabel.text(), self.behaviorLabel.text(),
        # self._startFrame.text(), self._endFrame.text(), self.joints))

        #self._addButton.clicked.connect(self.on__btnConnect_triggered(self.behaviorLabel.text(),
        #                                                           self.behaviorLabel.text(),
        #                                                          self._startFrame.text(),
        #                                                           self._endFrame.text(),
        #                                                          self.joints))

        self._setupUi(True, widget)
    # END __init__()

    def on__btnConnect_triggered(self, bhvName, boxName, startFrame, endFrame, joint):
        self.nao.makeJitter(bhvName, boxName, startFrame, endFrame, joint)
    # END on__btnConnect_triggered()

    def motion_chosen(self, text):
        self.motionLabel.setText(text)
    # END motion_chosen()

    def behavior_chosen(self, text):
        self.behaviorLabel.setText(text)

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    # END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    # END on_actionReceived()
# END Jitter

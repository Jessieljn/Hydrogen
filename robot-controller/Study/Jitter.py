from PyQt4 import QtCore, QtGui
from UI.FocusableLineEdit import FocusableLineEdit


class Jitter(QtGui.QWidget):
    def __init__(self):
        super(Jitter, self).__init__()
        self._actionQueue = None

        self.setWindowTitle("Jitter Function")
        self.vbox = QtGui.QVBoxLayout()   # General Box
        self.hbox1 = QtGui.QHBoxLayout()  # Start Frame Box
        self.hbox2 = QtGui.QHBoxLayout()  # End Frame Box
        self.setLayout(self.vbox)

        self.combo = QtGui.QComboBox()
        self.label = QtGui.QLabel("HeadYaw")  # Add to vbox

        motionList = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw',
                      'LHand', 'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',
                      'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll',
                      'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']

        # - LHipYawPitch uses the same more as RHipYawPitch, they move simultaneously and symmetrically. In case of
        # conflicting orders, LHipYawPitch takes priority.

        # - LWristYaw, LHand, RWristYaw, RHand, do no exist in model "H21".
        self.combo.addItems(motionList)

        self._startFrame = FocusableLineEdit(self)
        self._startFrame.setText('0')

        self._endFrame = FocusableLineEdit(self)
        self._endFrame.setText('0')

        self._startLabel = QtGui.QLabel("Start Frame: ")
        self._endLabel = QtGui.QLabel("End Frame: ")

        self._addButton = QtGui.QPushButton('Add', self)

        self.vbox.addWidget(self.combo)
        self.hbox1.addWidget(self._startLabel)
        self.hbox1.addWidget(self._startFrame)
        self.hbox2.addWidget(self._endLabel)
        self.hbox2.addWidget(self._endFrame)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self._addButton)

        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
    # END __init__()

    def combo_chosen(self, text):
        self.label.setText(text)
    # END combo_chosen()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    # END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    # END on_actionReceived()
# END Jitter
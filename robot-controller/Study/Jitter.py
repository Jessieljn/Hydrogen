from PyQt4 import QtCore, QtGui
from Action.Speech import Speech
from UI.ActionPushButton import ActionPushButton


class Jitter(QtGui.QWidget):
    def __init__(self):
        super(Jitter, self).__init__()
        self._actionQueue = None

        self.setWindowTitle("Jitter Function")
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        self.combo = QtGui.QComboBox()
        self.vbox.addWidget(self.combo)

        self.label = QtGui.QLabel("HeadYaw")

        motionList = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw',
                      'LHand', 'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll',
                      'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll',
                      'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']

        # 1) LHipYawPitch uses the same more as RHipYawPitch, they move simultaneously and symmetrically. In case of
        # conflicting orders, LHipYawPitch takes priority.

        # 2) LWristYaw, LHand, RWristYaw, RHand, do no exist in model "H21".
        self.combo.addItems(motionList)

        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
    #END __init__()

    def combo_chosen(self, text):
        """
        Handler called when a distro is chosen from the combo box
        """
        self.label.setText(text)
    #END combo_chosen()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    #END on_actionReceived()
#END class
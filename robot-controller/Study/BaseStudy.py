from PyQt4 import QtCore
from PyQt4 import QtGui
from UI.ActionPushButton import ActionPushButton


class BaseStudy(QtGui.QWidget):
    def __init__(self):
        super(BaseStudy, self).__init__()
        self._actionQueue = None
    #END __init__()

    def _setupBegin(self):
        self._widgets = []
        self._buttons = []
    #END _setupBegin()

    def _setupEnd(self):
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        for i in range(len(self._widgets)):
            layoutButtons = QtGui.QVBoxLayout(self._widgets[i])
            layoutButtons.setMargin(0)
            for button in self._buttons[i]:
                if isinstance(button, ActionPushButton):
                    button.clicked.connect(self.on_button_clicked)
                #END if
                layoutButtons.addWidget(button)
            #END for
            scroll = QtGui.QScrollArea()
            scroll.setAlignment(QtCore.Qt.AlignCenter)
            scroll.setWidget(self._widgets[i])
            layoutScroll = QtGui.QHBoxLayout()
            layoutScroll.setMargin(0)
            layoutScroll.addWidget(scroll)
            layout.addLayout(layoutScroll)
        #END for
    #END _setupEnd()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def on_button_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_button_clicked()
#END BaseStudy
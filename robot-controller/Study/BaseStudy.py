from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Speech
from UI.ActionPushButton import ActionPushButton


class BaseStudy(QtGui.QWidget):
    def __init__(self):
        super(BaseStudy, self).__init__()
        self._actionQueue = None
        self._nao = None
        self._widgets = None
        self._buttons = None
    #END __init__()

    def _setupUi(self, general_panel = True, custom_widget = None):
        wgtGeneral = None
        if general_panel:
            wgtGeneral = QtGui.QWidget()
            wgtGeneral.setMaximumHeight(80)
            wgtGeneral.setMinimumHeight(80)

            ##################################################
            # General Speech
            ##################################################
            self._speechs = [
                ActionPushButton(None, "Hello", Speech("Hello")),
                ActionPushButton(None, "Thanks", Speech("Thank you")),
                ActionPushButton(None, "Sorry", Speech("I'm sorry")),
                ActionPushButton(None, "Good", Speech("Good!")),
                ActionPushButton(None, "Okay", Speech("Okay")),
                ActionPushButton(None, "Yes", Speech("Yes")),
                ActionPushButton(None, "No", Speech("No")),
                ActionPushButton(None, "Hmmm", Speech("Heum,")),
                None,
                ActionPushButton(None, "Louder", Speech("Please speak louder")),
                ActionPushButton(None, "Say again?", Speech("Can you say one more time?")),
                ActionPushButton(None, "Repeat?", Speech("Would you like me to repeat that?")),
                ActionPushButton(None, "Understood?", Speech("Do you understand?")),
                ActionPushButton(None, "Don't Understand", Speech("I don't understand")),
                ActionPushButton(None, "Greeting", Speech("Hello, my name is NAO, nice to meet you")),
                ActionPushButton(None, "End Experiment", Speech("Thank you for participating in our experiment")),
            ]

            self._grpSpeech = QtGui.QGroupBox(wgtGeneral)
            self._grpSpeech.setTitle("General Speech")
            layoutSpeech = QtGui.QVBoxLayout(self._grpSpeech)
            layoutSpeech.setMargin(6)
            layoutSpeech.addSpacing(3)
            widget = QtGui.QWidget(self._grpSpeech)
            layout = QtGui.QHBoxLayout(widget)
            layout.setMargin(0)
            for item in self._speechs:
                if item is None:
                    layoutSpeech.addWidget(widget)
                    widget = QtGui.QWidget(self._grpSpeech)
                    layout = QtGui.QHBoxLayout(widget)
                    layout.setMargin(0)
                else:
                    item.setParent(widget)
                    item.clicked.connect(self.on_runSpeech_clicked)
                    layout.addWidget(item)
                #END if
            #END for
            layoutSpeech.addWidget(widget)
        #END if

        wgtButtons = None
        if self._widgets is not None and self._buttons is not None:
            wgtButtons = QtGui.QWidget()
            layout = QtGui.QHBoxLayout(wgtButtons)
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
        #END if

        if wgtGeneral is not None or wgtButtons is not None or custom_widget is not None:
            splitter = QtGui.QSplitter(self)
            splitter.setOrientation(QtCore.Qt.Vertical)
            layout = QtGui.QHBoxLayout(self)
            layout.setMargin(0)
            layout.addWidget(splitter)
            if wgtGeneral is not None:
                wgtGeneral.setParent(splitter)
            #END if
            if wgtButtons is not None:
                wgtButtons.setParent(splitter)
            #END if
            if custom_widget is not None:
                custom_widget.setParent(splitter)
            #END if
        #END if
    #END _setupUi()

    def LEDActive(self):
        if self._nao is not None:
            self._nao.LEDrandomEyes(1.0, True)
        #END if
    #END LEDActive()

    def LEDNormal(self):
        if self._nao is not None:
            self._nao.LEDNormal()
        #END if
    #END LEDNormal()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self.on_nao_connected)
            self._nao.disconnected.disconnect(self.on_nao_disconnected)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self.on_nao_connected)
            self._nao.disconnected.connect(self.on_nao_disconnected)
        #END if
    #END setNao()

    def speech(self, txt):
        return None
    #END speech()

    def on_button_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_button_clicked()

    def on_nao_connected(self):
        pass
    #END on_nao_connected()

    def on_nao_disconnected(self):
        pass
    #END on_nao_disconnected()

    def on_runSpeech_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_runSpeech_clicked()
#END BaseStudy

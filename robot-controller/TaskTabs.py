from PyQt4 import QtGui
import Tabs

#TabbedWid holds all *Tab classes


##
# TaskTabs.py
#
# Creates tabs for different commands.
# General, Tedium, and Mental Challenge Tabs
##
class SpeechButton(QtGui.QPushButton):
    def __init__(self, title, speech, nao):
        super(SpeechButton, self).__init__(speech)
        self.nao = nao
        self.speech = speech

        self.setText(title)

        self.clicked.connect(self.say)
    #END __init__()

    def say(self):
        self.nao.say(self.speech)
    #END say
#END SpeechButton


class TaskTabs(QtGui.QTabWidget):
    def __init__(self, nao, parent):
        self.parent = parent
        self.nao = nao
        super(TaskTabs, self).__init__()
        self.init()
    #END __init__()

    def init(self):
        self.setWindowTitle('Buttons')
        
        self.addTab(Tabs.General(self.nao, self.parent), 'General')
        #self.addTab(Tabs.Tedium(self.nao, self.parent), 'Tedium')
        #self.addTab(Tabs.MentalChallenge(self.nao, self.parent), 'Mental Challenge')
        #self.addTab(Tabs.Empathy(self.nao, self.parent), 'Empathy')
        #self.removeTab(3) Removes Empathy
    #END init()

    def remove(self, name):
        self.removeTab(0)

        if name == "General":
            self.addTab(Tabs.General(self.nao, self.parent), "General")
        elif name == "Tedium":
            self.addTab(Tabs.Tedium(self.nao, self.parent), 'Tedium')
        elif name == "Challenge":
            self.addTab(Tabs.MentalChallenge(self.nao, self.parent), 'Mental Challenge')
        elif name == "Empathy":
            self.addTab(Tabs.Empathy(self.nao, self.parent), 'Empathy')
    #END remove
#END TaskTabs
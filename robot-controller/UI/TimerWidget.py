# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui


class TimerWidget(QtGui.QGroupBox):
    def __init__(self, parent = None):
        super(TimerWidget, self).__init__(parent)
        self.setTitle("Timer")

        self._currTime = QtCore.QTime(0, 0, 0, 0)
        self._paused = False
        self._timer = QtCore.QTime(0, 0, 0, 0)
        self._timerID = None

        self._lcdClock = QtGui.QLCDNumber(self)
        self._lcdClock.setDigitCount(12)
        self._lcdClock.display(self._currTime.toString("hh:mm:ss.zzz"))

        btnStart = QtGui.QPushButton(u"⏯", self)
        btnStart.setMaximumSize(25, 25)
        btnStart.clicked.connect(self._on_btnStart_clicked)

        btnStop = QtGui.QPushButton(u"◼", self)
        btnStop.setMaximumSize(25, 25)
        btnStop.clicked.connect(self._on_btnStop_clicked)

        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(3)
        layout.addWidget(self._lcdClock)
        layout.addWidget(btnStart)
        layout.addWidget(btnStop)
    #END __init__()

    def _on_btnStart_clicked(self):
        if self._timerID is None:
            self._currTime.setHMS(0, 0, 0, 0)
            self._paused = False
            self._timer = QtCore.QTime(0, 0, 0, 0)
            self._timer.start()
            self._timerID = self.startTimer(7)
        else:
            self._timer.start()
            self._paused = not self._paused
        #END if
    #END _on_btnStart_clicked()

    def _on_btnStop_clicked(self):
        self.killTimer(self._timerID)
        self._timerID = None
    #END _on_btnStop_clicked()

    def timerEvent(self, event):
        if not self._paused:
            elapsed = self._timer.restart()
            self._currTime = self._currTime.addMSecs(elapsed)
            self._lcdClock.display(self._currTime.toString("hh:mm:ss.zzz"))
        #END if
    #END timerEvent()
#END class

from PyQt4 import QtCore
from Speech import Speech


class ReplaceableSpeech(Speech):
    def __init__(self, text, speed = 90, shaping = 100, blocking = True):
        super(ReplaceableSpeech, self).__init__(text, speed, shaping, blocking)
        self._orgText = text
    #END __init__()

    def replace(self, arg0, arg1 = None, arg2 = None, arg3 = None, arg4 = None, arg5 = None, arg6 = None, arg7 = None, arg8 = None, arg9 = None):
        self._text = QtCore.QString(self._orgText).arg(arg0)
        if arg1 is not None:
            self._text = self._text.arg(arg1)
        #END if
        if arg2 is not None:
            self._text = self._text.arg(arg2)
        #END if
        if arg3 is not None:
            self._text = self._text.arg(arg3)
        #END if
        if arg4 is not None:
            self._text = self._text.arg(arg4)
        #END if
        if arg5 is not None:
            self._text = self._text.arg(arg5)
        #END if
        if arg6 is not None:
            self._text = self._text.arg(arg6)
        #END if
        if arg7 is not None:
            self._text = self._text.arg(arg7)
        #END if
        if arg8 is not None:
            self._text = self._text.arg(arg8)
        #END if
        if arg9 is not None:
            self._text = self._text.arg(arg9)
        #END if
        self._text = str(self._text)
    #END replace()
#END class
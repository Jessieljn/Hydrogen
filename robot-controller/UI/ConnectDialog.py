from Definitions import DEFAULT_IP
from Definitions import DEFAULT_PORT
from PyQt4 import QtCore
from PyQt4 import QtGui


##
# ConnectDialog.py
#
# Creates the connection widget in the GUI, for input IP address and port.
# Default IP Address: 140.193.228.26
# Default Port: 9559
##
class ConnectDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(ConnectDialog, self).__init__(parent)
        self.ipAddress = str(DEFAULT_IP)
        self.port = str(DEFAULT_PORT)

        wgtRobot, self._leIPAddr, self._lePort = ConnectDialog._createIPInputBox(self, "Robot", self.ipAddress, self.port)
        wgtCamera, self._leCamIPAddr, self._leCamPort = ConnectDialog._createIPInputBox(self, "Camera", self.ipAddress, self.port)
        wgtSpeech, self._leTTSIPAddr, self._leTTSPort = ConnectDialog._createIPInputBox(self, "Speech", self.ipAddress, self.port)

        self._btnConnect = QtGui.QPushButton('Connect (&C)', self)
        self._btnConnect.clicked.connect(self.on__btnConnect_triggered)
        self._btnCancel = QtGui.QPushButton('Cancel (&X)', self)
        self._btnCancel.clicked.connect(self.on__btnCancel_triggered)

        self._layoutGrid = QtGui.QGridLayout(self)
        self._layoutGrid.setContentsMargins(10, 10, 10, 10)
        self._layoutGrid.setSpacing(6)
        self._layoutGrid.addWidget(wgtRobot, 0, 0, 1, 2)
        self._layoutGrid.addWidget(wgtCamera, 1, 0, 1, 2)
        self._layoutGrid.addWidget(wgtSpeech, 2, 0, 1, 2)
        self._layoutGrid.addWidget(self._btnConnect, 3, 0, 1, 1)
        self._layoutGrid.addWidget(self._btnCancel, 3, 1, 1, 1)

        self.setFixedSize(260, 300)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Connection to NAO')
    # END __init__()

    def on__btnConnect_triggered(self):
        self.ipAddress = self._leIPAddr.text()
        self.port = self._lePort.text()
        self.camIpAddr = self._leCamIPAddr.text()
        self.camPort = self._leCamPort.text()
        self.ttsIpAddr = self._leTTSIPAddr.text()
        self.ttsPort = self._leTTSPort.text()
        self.setResult(QtGui.QDialog.Accepted)
        self.accept()
        self.close()
    # END on__btnConnect_triggered()

    def on__btnCancel_triggered(self):
        self.setResult(QtGui.QDialog.Rejected)
        self.reject()
        self.close()
    # END on__btnCancel_triggered()

    @staticmethod
    def _createIPInputBox(parent, title, ipAddr = "127.0.0.1", port = "8888"):
        groupBox = QtGui.QGroupBox(parent)
        groupBox.setTitle(title)

        label_IPAddr = QtGui.QLabel('IP address:', groupBox)
        label_IPAddr.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        lineEdit_IPAddr = QtGui.QLineEdit(groupBox)
        lineEdit_IPAddr.setText(ipAddr)
        lineEdit_IPAddr.setFocusPolicy(QtCore.Qt.StrongFocus)

        label_Port = QtGui.QLabel('Port number:', groupBox)
        label_Port.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        line_editPort = QtGui.QLineEdit(groupBox)
        line_editPort.setText(port)
        line_editPort.setFocusPolicy(QtCore.Qt.StrongFocus)

        layoutGrid = QtGui.QGridLayout(groupBox)
        layoutGrid.setContentsMargins(5, 5, 5, 5)
        layoutGrid.setSpacing(3)
        layoutGrid.addWidget(label_IPAddr, 0, 0, 1, 1)
        layoutGrid.addWidget(lineEdit_IPAddr, 0, 1, 1, 2)
        layoutGrid.addWidget(label_Port, 1, 0, 1, 1)
        layoutGrid.addWidget(line_editPort, 1, 1, 1, 2)

        return groupBox, lineEdit_IPAddr, line_editPort
    #END _createIPInputBox()
# END ConnectDialog.py
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

        self._lIPAddr = QtGui.QLabel('IP address:', self)
        self._leIPAddr = QtGui.QLineEdit(self)
        self._leIPAddr.setText(self.ipAddress)
        self._leIPAddr.setFocusPolicy(QtCore.Qt.StrongFocus)

        self._lPort = QtGui.QLabel('Port number:', self)
        self._lePort = QtGui.QLineEdit(self)
        self._lePort.setText(self.port)
        self._lePort.setFocusPolicy(QtCore.Qt.StrongFocus)

        self._btnConnect = QtGui.QPushButton('Connect (&C)', self)
        self._btnConnect.clicked.connect(self.on__btnConnect_triggered)

        self._btnCancel = QtGui.QPushButton('Cancel (&X)', self)
        self._btnCancel.clicked.connect(self.on__btnCancel_triggered)

        self._layoutGrid = QtGui.QGridLayout(self)
        self._layoutGrid.setContentsMargins(10, 10, 10, 10)
        self._layoutGrid.setSpacing(6)
        self._layoutGrid.addWidget(self._lIPAddr, 0, 0, 1, 1)
        self._layoutGrid.addWidget(self._leIPAddr, 0, 1, 1, 2)
        self._layoutGrid.addWidget(self._lPort, 1, 0, 1, 1)
        self._layoutGrid.addWidget(self._lePort, 1, 1, 1, 2)
        self._layoutGrid.addWidget(self._btnConnect, 2, 1, 1, 1)
        self._layoutGrid.addWidget(self._btnCancel, 2, 2, 1, 1)

        self.setFixedSize(260, 120)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Connection to NAO')
    # END __init__()

    def on__btnConnect_triggered(self):
        self.ipAddress = self._leIPAddr.text()
        self.port = self._lePort.text()
        self.setResult(QtGui.QDialog.Accepted)
        self.accept()
        self.close()
    # END on__btnConnect_triggered()

    def on__btnCancel_triggered(self):
        self.setResult(QtGui.QDialog.Rejected)
        self.reject()
        self.close()
    # END on__btnCancel_triggered()
# END PanelConnect

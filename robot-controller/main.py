import sys
from PyQt4 import QtGui, QtNetwork, QtCore
from MainWindow import MainWindow


def main():
    app = QtGui.QApplication(sys.argv)   
    window = MainWindow()
    sys.exit(app.exec_())
#END main()

if __name__ == '__main__':
    main()
#END if
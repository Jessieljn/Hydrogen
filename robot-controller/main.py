import sys
from PyQt4 import QtGui
from UI import MainWindow


##
# main.py
#
# Executes the application.
##
def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
#END main()

if __name__ == '__main__':
    main()
#END if
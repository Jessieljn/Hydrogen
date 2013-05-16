from PyQt4 import QtGui

app = QtGui.QApplication([])
menu = QtGui.QMenu()
sub_menu = QtGui.QMenu("Sub_Menu")

for i in ["a", "b", "c"]:
    sub_menu.addAction(i)

menu.addMenu(sub_menu)
menu.show()
app.exec_()
from PyQt4 import QtGui, QtCore
import Nao


##
# CameraWidget.py
#
# Creates a camera widget in the GUI.
# Allows for switching between the top and bottom camera, as well as rotation of the camera.
##
class CameraWidget (QtGui.QGroupBox):

    def __init__(self, parent):
        super(CameraWidget, self).__init__()
        self.init()
        self.setParent(parent)
    #END __init__()

    def init(self):
        self.setTitle("Camera")

        self.camera = QtGui.QLabel()
        self.camera.setFixedSize(500, 500)

        self.camera.setScaledContents(True)

        self.camera.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        self.camera.setFrameStyle(QtGui.QFrame.Panel)
        self.setImage(QtGui.QImage('image1.jpg'))

        # Creates symbols for the buttons.
        self.up = QtGui.QPushButton("^")
        self.down = QtGui.QPushButton("v")
        self.left = QtGui.QPushButton("<")
        self.right = QtGui.QPushButton(">")

        # Sets the size fo the buttons.
        self.up.setFixedSize(50, 40)
        self.left.setFixedSize(50, 40)
        self.right.setFixedSize(50, 40)
        self.down.setFixedSize(50, 40)

        # Radio buttons for the two camera views, top is the default.
        self.topCamera = QtGui.QRadioButton("Top")
        self.topCamera.setChecked(True)
        self.bottomCamera = QtGui.QRadioButton("Bottom")

        # Adds the radio buttons to the source.
        self.cameraSource = QtGui.QButtonGroup()
        self.cameraSource.addButton(self.topCamera)
        self.cameraSource.addButton(self.bottomCamera)

        # Adds radio buttons to the layout.
        cameraSourceLayout = QtGui.QHBoxLayout()
        cameraSourceLayout.addWidget(self.topCamera, 0, QtCore.Qt.AlignCenter)
        cameraSourceLayout.addWidget(self.bottomCamera, 0, QtCore.Qt.AlignCenter)

        # Adds camera buttons to the layout.
        btnLayout = QtGui.QGridLayout()
        btnLayout.addWidget(self.up, 0, 1, QtCore.Qt.AlignVCenter)
        btnLayout.addWidget(self.left, 1, 0, QtCore.Qt.AlignVCenter)
        btnLayout.addWidget(self.right, 1, 2, QtCore.Qt.AlignVCenter)
        btnLayout.addWidget(self.down, 2, 1, QtCore.Qt.AlignVCenter)

        # Adds all the elements to the layout.
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.camera)
        layout.addLayout(btnLayout)
        layout.addLayout(cameraSourceLayout)

        # Set the layout.
        self.setLayout(layout)
    #END init()

    # Ability to rotate the NAO's head.
    def setNao(self, nao):
        self.nao = nao
        self.left.clicked.connect(self.nao.turnHeadLeft)
        self.right.clicked.connect(self.nao.turnHeadRight)
        self.up.clicked.connect(self.nao.tiltHeadUp)
        self.down.clicked.connect(self.nao.tiltHeadDown)
    #END setNao()

    def setImage(self, image):
        self.camera.setPixmap(QtGui.QPixmap.fromImage(image.scaled(self.camera.size(), QtCore.Qt.KeepAspectRatio)))
    #END setImage()

    # Retrieves the camera source.
    def getCameraSource(self):
        checked = self.cameraSource.checkedButton()

        if checked == self.topCamera:
            return Nao.TOP_CAMERA
        #END if
        elif checked == self.bottomCamera:
            return Nao.BOTTOM_CAMERA
        #END elif
    #END getCameraSource()
#END CameraWidget
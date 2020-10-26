#Coded By Kral4, BBOD | https://github.com/rootkral4 | https://github.com/1nnr3d
#Educational Purposes Only
#https://github.com/rootkral4/fileencrypt/blob/main/LICENSE

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://github.com/rootkral4/fileencrypt/blob/main/LICENSE>.

import sys
import codecs
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets, QtCore, QtGui, QtTest
from modules.back_btn import BackPushButton
from modules.btn import PushButton
from modules.encrypt_mod import encrypT
from modules.decrypt_mod import decrypT

titleFont = QtGui.QFont("Orbitron", 10)
titleFont2 = QtGui.QFont("Orbitron", 14)


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 130)

        self.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowMinimizeButtonHint
        )
        self.setWindowTitle("F E A D")
        self.setWindowIcon(QtGui.QIcon("images/faed.png"))

        main = QtWidgets.QWidget()

        self.title = QtWidgets.QLabel("File Encryption And Decryption")
        self.title.setFont(titleFont)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.eButton = PushButton()
        self.eButton.setText("Encryption")
        self.eButton.clicked.connect(self.eWindow)
        self.dButton = PushButton()
        self.dButton.setText("Decryption")
        self.dButton.clicked.connect(self.dWindow)

        oImage = QtGui.QImage("images/faed_background0.jpg")
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(300, 130))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        vertical.addStretch()
        vertical.addWidget(self.title)
        vertical.addStretch()
        vertical.addWidget(self.eButton)
        vertical.addWidget(self.dButton)

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()

        self.setCentralWidget(main)
        main.setLayout(horizontal)
        self.setPalette(palette)
        self.show()

    def eWindow(self):
        self.ewindow = encryptWindow()
        self.ewindow.show()
        self.setHidden(True)

    def dWindow(self):
        self.dwindow = decryptWindow()
        self.dwindow.show()
        self.setHidden(True)


class encryptWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Encryption")
        self.setWindowIcon(QtGui.QIcon("images/faed.png"))

        self.setFixedSize(400, 400)

        self.backBtn = BackPushButton(self)
        self.backBtn.setGeometry(30, 30, 30, 30)
        self.backBtn.setText("<")
        self.backBtn.clicked.connect(self.back)

        self.title = QtWidgets.QLabel("Encryption")
        self.title.setFont(titleFont2)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.encFile = PushButton()
        self.encFile.setText("File to Encrypt")
        self.encFile.clicked.connect(self.encfile)

        self.encFileout = PushButton()
        self.encFileout.setText("File Output")
        self.encFileout.clicked.connect(self.encoutfile)

        self.encKey = PushButton()
        self.encKey.setText("Key")
        self.encKey.clicked.connect(self.enckeyfile)

        self.fileName = QtWidgets.QLabel("File: ")
        self.outfileName = QtWidgets.QLabel("Output File Path: ")
        self.keyfileName = QtWidgets.QLabel("Key: ")

        self.encBtn = PushButton()
        self.encBtn.setText("Encrypt")
        self.encBtn.clicked.connect(self.encrypt)

        oImage = QtGui.QImage("images/faed_background1.jpg")
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(400, 400))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        vertical.addStretch()
        vertical.addWidget(self.title)
        vertical.addStretch()
        vertical.addWidget(self.encFile)
        vertical.addWidget(self.encFileout)
        vertical.addWidget(self.encKey)
        vertical.addStretch()
        vertical.addWidget(self.fileName)
        vertical.addWidget(self.outfileName)
        vertical.addWidget(self.keyfileName)
        vertical.addStretch()
        vertical.addWidget(self.encBtn)
        vertical.addStretch()

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()

        self.setPalette(palette)
        self.setLayout(horizontal)
        self.show()

    def encfile(self):
        self.fileUrl = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose a file to be encrypted..")
        self.filePath = str(self.fileUrl[0])
        lst = self.filePath.split("/")
        self.fileName.setText("File: " + lst[-1])
        self.file = str(self.filePath)
        with open(self.file, "rb") as f:
            self.getdata = f.read()

    def encoutfile(self):
        self.fileUrl1 = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save the output of the file to be encrypted..")
        self.outfilePath = str(self.fileUrl1[0])
        self.outfileName.setText("Output File Path: \n" + self.outfilePath)

    def enckeyfile(self):
        self.keyUrl = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Key..")
        self.keyPath = str(self.keyUrl[0])
        lst = self.keyPath.split("/")
        self.keyfileName.setText("Key: " + lst[-1])

    def encrypt(self):
        encrypT(self.outfilePath, self.getdata, self.keyPath)

    def back(self):
        self.main = mainWindow()
        self.main.show()
        self.setHidden(True)


class decryptWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Decryption")
        self.setWindowIcon(QtGui.QIcon("images/faed.png"))

        self.setFixedSize(400, 400)

        self.backBtn = BackPushButton(self)
        self.backBtn.setGeometry(30, 30, 30, 30)
        self.backBtn.setText("<")
        self.backBtn.clicked.connect(self.back)

        self.title = QtWidgets.QLabel("Decryption")
        self.title.setFont(titleFont2)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.decFile = PushButton()
        self.decFile.setText("File to Decrypt")
        self.decFile.clicked.connect(self.decfile)

        self.decFileout = PushButton()
        self.decFileout.setText("File Output")
        self.decFileout.clicked.connect(self.decoutfile)

        self.decKey = PushButton()
        self.decKey.setText("Key")
        self.decKey.clicked.connect(self.deckeyfile)

        self.fileName = QtWidgets.QLabel("File: ")
        self.outfileName = QtWidgets.QLabel("Output File Path: ")
        self.keyfileName = QtWidgets.QLabel("Key: ")

        self.decBtn = PushButton()
        self.decBtn.setText("Decrypt")
        self.decBtn.clicked.connect(self.decrypt)

        oImage = QtGui.QImage("images/faed_background1.jpg")
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(400, 400))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        vertical.addStretch()
        vertical.addWidget(self.title)
        vertical.addStretch()
        vertical.addWidget(self.decFile)
        vertical.addWidget(self.decFileout)
        vertical.addWidget(self.decKey)
        vertical.addStretch()
        vertical.addWidget(self.fileName)
        vertical.addWidget(self.outfileName)
        vertical.addWidget(self.keyfileName)
        vertical.addStretch()
        vertical.addWidget(self.decBtn)
        vertical.addStretch()

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()

        self.setPalette(palette)
        self.setLayout(horizontal)
        self.show()

    def decfile(self):
        self.fileUrl0 = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose a file to be decrypted..")
        self.filePath = str(self.fileUrl0[0])
        lst = self.filePath.split("/")
        self.fileName.setText("File: " + lst[-1])

    def decoutfile(self):
        self.fileUrl1 = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save the output of the file to be decrypted..")
        self.outfilePath = str(self.fileUrl1[0])
        self.outfileName.setText("Output File Path: \n" + self.filePath)

    def deckeyfile(self):
        self.keyUrl = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Key..")
        self.keyPath = str(self.keyUrl[0])
        lst = self.keyPath.split("/")
        self.keyfileName.setText("Key: " + lst[-1])

    def decrypt(self):
        decrypT(self.outfilePath, self.filePath, self.keyPath)

    def back(self):
        self.main = mainWindow()
        self.main.show()
        self.setHidden(True)


stylesheet = """
QPushButton{
    border: 2px solid transparent;
    border-radius: 5px;
    background-color: white;
}
QLabel{
    color: white;
}
"""

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(stylesheet)
main = mainWindow()
sys.exit(app.exec_())

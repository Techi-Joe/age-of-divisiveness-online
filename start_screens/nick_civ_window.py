import socket
from time import sleep

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox


class CivCombo(QMainWindow):
    """
    This class is for choosing civ from available delivered from server_utils and typing your nick.
    Server should send list of available civilizations before running constructor of this class.
    Available civilizations should be passed via constructor.
    """

    def __init__(self, civ_list, parent=None):
        super(CivCombo, self).__init__(parent)
        # it's for going back to window which called this window and more importantly for
        # setting up value of chosen_nick and chosen_civ in parent class
        self.parent = parent

        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Choose nickname and your civilization")
        self.setFixedSize(560, 200)

        """In case we would like background image in this window.
        choose_civ_background.png is a fine png. One does not simply find good png."""
        # self.image_label = QLabel(self)  # background label
        # pixmap = QPixmap('images/choose_civ_background.png')
        # self.image_label.setPixmap(pixmap)
        # self.image_label.setScaledContents(True)
        # self.setCentralWidget(self.image_label)
        # self.resize(int(pixmap.width() * 1.5), int(pixmap.height() * 1.5))

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(civ_list)
        self.combo_box.setGeometry(QRect(10, 40, 421, 41))

        self.nickname_line = QLineEdit(self)
        self.nickname_line.setText("Type your nickname")
        self.nickname_line.setGeometry(QRect(10, 90, 550, 41))

        self.ok_button = QPushButton(self)
        self.ok_button.setText("Choose")
        self.ok_button.setGeometry(QRect(450, 40, 101, 41))
        self.ok_button.clicked.connect(self.choose_civ)

        self.center()
        self.show()

    def choose_civ(self):
        """
         By calling this method, you set up chosen_civ field in parent class
         (in our case ConnectWindow or MapGeneratorWindow)
         """
        civilization = self.combo_box.currentText()  # this how you get value from combo box
        nickname = self.nickname_line.text()
        self.parent.set_player_info(civilization, nickname)
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

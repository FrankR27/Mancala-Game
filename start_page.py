from PyQt5 import QtCore, QtGui, QtWidgets
import showings

class Ui_Start_Window(object):
    def setupUi(self, Start_Window):
        self.Start_Window=Start_Window
        Start_Window.setObjectName("Start_Window")
        Start_Window.resize(882, 568)
        Start_Window.setMaximumSize(QtCore.QSize(882, 568))
        Start_Window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Mancala-fun-entertainment-game-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Start_Window.setWindowIcon(icon)
        Start_Window.setStyleSheet("background:#1b2533    ;\n"
"border-radius:12px;")
        self.centralwidget = QtWidgets.QWidget(Start_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(350, 60, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(70)
        font.setStrikeOut(False)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color:White;\n"
"")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_one = QtWidgets.QPushButton(self.centralwidget)
        self.btn_one.setGeometry(QtCore.QRect(280, 300, 281, 81))
        self.btn_one.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#f5e6ca;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_one.setObjectName("btn_one")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -10, 301, 241))
        self.label.setObjectName("label")
        self.label.raise_()
        self.lbl_title.raise_()
        self.btn_one.raise_()
        Start_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Start_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 26))
        self.menubar.setObjectName("menubar")
        Start_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Start_Window)
        self.statusbar.setObjectName("statusbar")
        Start_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Start_Window)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

        self.btn_one.clicked.connect(lambda : self.btn_click(1))

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "Mancala"))
        self.lbl_title.setText(_translate("Start_Window", "MANCALA"))
        self.btn_one.setText(_translate("Start_Window", "Nuevo Juego"))
        self.label.setText(_translate("Start_Window", "<html><head/><body><p><img src=\"Mancala-fun-entertainment-game-512.png\" width=\"150\"/></p></body></html>"))

    def btn_click(self,no):
        self.no = 1
        s = True
        self.Start_Window.close()
        self.new_window, self.ui=showings.show_level_page(self.no,s)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Start_Window = QtWidgets.QMainWindow()
    ui = Ui_Start_Window()
    ui.setupUi(Start_Window)
    Start_Window.show()
    sys.exit(app.exec_())

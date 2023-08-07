from PyQt5 import QtCore, QtGui, QtWidgets
import showings

class Ui_Level_Window(object):
    def __init__(self,mode,stealing):
        self.mode=mode
        self.stealing = stealing

    def setupUi(self, Level_Window):
        self.Level_Window=Level_Window
        Level_Window.setObjectName("Level_Window")
        Level_Window.resize(882, 568)
        Level_Window.setMaximumSize(QtCore.QSize(882, 568))
        Level_Window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Mancala-fun-entertainment-game-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Level_Window.setWindowIcon(icon)
        Level_Window.setStyleSheet("background:#1b2533    ;\n"
"border-radius:12px;")
        self.centralwidget = QtWidgets.QWidget(Level_Window)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -10, 301, 241))
        self.label.setObjectName("label")
        self.btn_hard = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hard.setGeometry(QtCore.QRect(290, 435, 281, 81))
        self.btn_hard.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#f5e6ca;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_hard.setObjectName("btn_hard")
        self.btn_medium = QtWidgets.QPushButton(self.centralwidget)
        self.btn_medium.setGeometry(QtCore.QRect(290, 325, 281, 81))
        self.btn_medium.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#f5e6ca;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_medium.setObjectName("btn_medium")
        self.btn_easy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_easy.setGeometry(QtCore.QRect(290, 215, 281, 81))
        self.btn_easy.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#f5e6ca;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_easy.setObjectName("btn_easy")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(50, 420, 120, 81))
        self.btn_back.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#f5e6ca;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_back.setObjectName("btn_back")
        self.label.raise_()
        self.lbl_title.raise_()
        self.btn_hard.raise_()
        self.btn_medium.raise_()
        self.btn_easy.raise_()
        self.btn_back.raise_()
        Level_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Level_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 26))
        self.menubar.setObjectName("menubar")
        Level_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Level_Window)
        self.statusbar.setObjectName("statusbar")
        Level_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Level_Window)
        QtCore.QMetaObject.connectSlotsByName(Level_Window)

        self.btn_easy.clicked.connect(lambda : self.btn_click(2))
        self.btn_medium.clicked.connect(lambda : self.btn_click(5))
        self.btn_hard.clicked.connect(lambda : self.btn_click(7))
        self.btn_back.clicked.connect(self.btn_click_back)

    def retranslateUi(self, Level_Window):
        _translate = QtCore.QCoreApplication.translate
        Level_Window.setWindowTitle(_translate("Level_Window", "Selector de Dificultad"))
        self.lbl_title.setText(_translate("Level_Window", "MANCALA"))
        self.label.setText(_translate("Level_Window", "<html><head/><body><p><img src=\"Mancala-fun-entertainment-game-512.png\" width=\"150\"/></p></body></html>"))
        self.btn_hard.setText(_translate("Level_Window", "Modo Dificil"))
        self.btn_medium.setText(_translate("Level_Window", "Modo Normal"))
        self.btn_easy.setText(_translate("Level_Window", "Modo facil"))
        self.btn_back.setText(_translate("Level_Window", "Regresar"))

    def btn_click(self,no):
        s = 1
        self.no = no
        self.Level_Window.close()
        self.new_window, self.ui=showings.show_game_page(self.mode,self.stealing,self.no,s)

    def btn_click_back(self):
        self.Level_Window.close()
        self.back_window, self.back_ui = showings.show_start_page()


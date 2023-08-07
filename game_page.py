from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from tkinter import messagebox
import showings
import time

# to remove tkinter window
import tkinter
root= tkinter.Tk()
root.withdraw()
###


class Ui_Game_Window(object):
                
    def __init__(self,mode=2,stealing=True,level=5,p1_first=1):
                self.current_state=np.array([4,4,4,4,4,4,0,4,4,4,4,4,4,0],dtype='int')
                self.action =-1
                self.turn= p1_first
                self.stealing= stealing
                self.level=level
                self.mode = mode
                self.player1= "Jugador 1"
                self.player2= "AI"

  

    def setupUi(self, Game_Window):
        self.Game_Window= Game_Window
        Game_Window.setObjectName("Game_Window")
        Game_Window.resize(1302, 900)
        Game_Window.setMinimumSize(QtCore.QSize(1302, 653))
        Game_Window.setMaximumSize(QtCore.QSize(1302, 900))
        Game_Window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Mancala-fun-entertainment-game-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Game_Window.setWindowIcon(icon)
        Game_Window.setStyleSheet("background:#1b2533    ;\n"
"border-radius:12px;")
        self.centralwidget = QtWidgets.QWidget(Game_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_p11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p11.setGeometry(QtCore.QRect(290, 510, 101, 81))
        self.btn_p11.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p11.setObjectName("btn_p11")
        self.btn_p12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p12.setGeometry(QtCore.QRect(410, 510, 101, 81))
        self.btn_p12.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p12.setObjectName("btn_p12")
        self.btn_p13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p13.setGeometry(QtCore.QRect(530, 510, 101, 81))
        self.btn_p13.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p13.setObjectName("btn_p13")
        self.btn_p14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p14.setGeometry(QtCore.QRect(650, 510, 101, 81))
        self.btn_p14.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p14.setObjectName("btn_p14")
        self.btn_p15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p15.setGeometry(QtCore.QRect(770, 510, 101, 81))
        self.btn_p15.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p15.setObjectName("btn_p15")
        self.btn_p16 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p16.setGeometry(QtCore.QRect(890, 510, 101, 81))
        self.btn_p16.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p16.setObjectName("btn_p16")
        self.btn_p24 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p24.setGeometry(QtCore.QRect(530, 360, 101, 81))
        self.btn_p24.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p24.setObjectName("btn_p24")
        self.btn_p25 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p25.setGeometry(QtCore.QRect(410, 360, 101, 81))
        self.btn_p25.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p25.setObjectName("btn_p25")
        self.btn_p23 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p23.setGeometry(QtCore.QRect(650, 360, 101, 81))
        self.btn_p23.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p23.setObjectName("btn_p23")
        self.btn_p22 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p22.setGeometry(QtCore.QRect(770, 360, 101, 81))
        self.btn_p22.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p22.setObjectName("btn_p22")
        self.btn_p26 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p26.setGeometry(QtCore.QRect(290, 360, 101, 81))
        self.btn_p26.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p26.setObjectName("btn_p26")
        self.btn_p21 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p21.setGeometry(QtCore.QRect(890, 360, 101, 81))
        self.btn_p21.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_p21.setObjectName("btn_p21")
        self.txt_player2_score = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_player2_score.setEnabled(True)
        self.txt_player2_score.setGeometry(QtCore.QRect(40, 270, 231, 361))
        self.txt_player2_score.setStyleSheet("font: 40pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.txt_player2_score.setInputMask("")
        self.txt_player2_score.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_player2_score.setReadOnly(True)
        self.txt_player2_score.setObjectName("txt_player2_score")
        self.txt_player1_score = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_player1_score.setEnabled(True)
        self.txt_player1_score.setGeometry(QtCore.QRect(1010, 280, 231, 361))
        self.txt_player1_score.setStyleSheet("font: 40pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.txt_player1_score.setInputMask("")
        self.txt_player1_score.setMaxLength(32767)
        self.txt_player1_score.setFrame(True)
        self.txt_player1_score.setCursorPosition(1)
        self.txt_player1_score.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_player1_score.setReadOnly(True)
        self.txt_player1_score.setObjectName("txt_player1_score")
        self.lbl_turn = QtWidgets.QLabel(self.centralwidget)
        self.lbl_turn.setGeometry(QtCore.QRect(70, 720, 281, 61))
        self.lbl_turn.setStyleSheet("font: 25pt \\\"MV Boli\\\";\n"
"color:White;\n"
"")
        self.lbl_turn.setText("")
        self.lbl_turn.setObjectName("lbl_turn")
        self.lbl_level = QtWidgets.QLabel(self.centralwidget)
        self.lbl_level.setGeometry(QtCore.QRect(620, 720, 281, 61))
        self.lbl_level.setStyleSheet("font: 25pt \\\"MV Boli\\\";\n"
"color:White;\n"
"")
        self.lbl_level.setText("")
        self.lbl_level.setObjectName("lbl_level")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(442, 84, 401, 101))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(70)
        font.setStrikeOut(False)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color:White;\n"
"")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(1080, 710, 101, 81))
        self.btn_exit.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ffe054;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_exit.setObjectName("btn_exit")
        ###
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(570, 620, 211, 81))
        self.btn_next.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ffe054;\n"
"color:#222831;\n"
"border-radius:12px;")
        self.btn_next.setObjectName("btn_next")
        self.btn_next.hide()
        self.btn_p11.raise_()
        self.btn_p12.raise_()
        self.btn_p13.raise_()
        self.btn_p14.raise_()
        self.btn_p15.raise_()
        self.btn_p16.raise_()
        self.btn_p24.raise_()
        self.btn_p25.raise_()
        self.btn_p23.raise_()
        self.btn_p22.raise_()
        self.btn_p26.raise_()
        self.btn_p21.raise_()
        self.txt_player2_score.raise_()
        self.txt_player1_score.raise_()
        self.lbl_turn.raise_()
        self.lbl_level.raise_()
        self.lbl_title.raise_()
        self.btn_exit.raise_()
        Game_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 26))
        self.menubar.setObjectName("menubar")
        Game_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Game_Window)
        self.statusbar.setObjectName("statusbar")
        Game_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Game_Window)
        QtCore.QMetaObject.connectSlotsByName(Game_Window)
        #############################################################
        ## draw initial state
        self.draw_state()

        if self.turn==1:
                self.lbl_turn.setText(self.player1)
                self.border_p1()
                self.disable_p2()

        elif self.turn==-1:
                self.lbl_turn.setText(self.player2)
                self.border_p2()
                self.disable_p1()
                while self.turn ==-1:
                        _,action= self.alpha_beta_pruning(self.current_state,self.level,float('-inf'),float('inf'),self.turn)
                        self.action= action
                        self.turn*=-1 #reverse the turn
                        self.change_state()
                        self.draw_state()
                        self.check_turns()
                        time.sleep(1)

        ## buttons connections
        self.btn_p11.clicked.connect(lambda : self.btn_click(0))
        self.btn_p12.clicked.connect(lambda : self.btn_click(1))
        self.btn_p13.clicked.connect(lambda : self.btn_click(2))
        self.btn_p14.clicked.connect(lambda : self.btn_click(3))
        self.btn_p15.clicked.connect(lambda : self.btn_click(4))
        self.btn_p16.clicked.connect(lambda : self.btn_click(5))
        self.btn_p21.clicked.connect(lambda : self.btn_click(7))
        self.btn_p22.clicked.connect(lambda : self.btn_click(8))
        self.btn_p23.clicked.connect(lambda : self.btn_click(9))
        self.btn_p24.clicked.connect(lambda : self.btn_click(10))
        self.btn_p25.clicked.connect(lambda : self.btn_click(11))
        self.btn_p26.clicked.connect(lambda : self.btn_click(12))

        self.btn_exit.clicked.connect(lambda: self.btn_exit_click())

        self.btn_next.clicked.connect(self.btn_next_click)
        ######################################################################
    def retranslateUi(self, Game_Window): ##HAMIED CODE ###
        l=[0,0,'Modo Facil',0,0, 'Modo Normal',0,'Modo Dificil']
        _translate = QtCore.QCoreApplication.translate
        Game_Window.setWindowTitle(_translate("Game_Window", "Mancala"))
        self.btn_p11.setText(_translate("Game_Window", "4"))
        self.btn_p12.setText(_translate("Game_Window", "4"))
        self.btn_p13.setText(_translate("Game_Window", "4"))
        self.btn_p14.setText(_translate("Game_Window", "4"))
        self.btn_p15.setText(_translate("Game_Window", "4"))
        self.btn_p16.setText(_translate("Game_Window", "4"))
        self.btn_p24.setText(_translate("Game_Window", "4"))
        self.btn_p25.setText(_translate("Game_Window", "4"))
        self.btn_p23.setText(_translate("Game_Window", "4"))
        self.btn_p22.setText(_translate("Game_Window", "4"))
        self.btn_p26.setText(_translate("Game_Window", "4"))
        self.btn_p21.setText(_translate("Game_Window", "4"))
        self.txt_player2_score.setText(_translate("Game_Window", "0"))
        self.txt_player1_score.setText(_translate("Game_Window", "0"))
        self.lbl_title.setText(_translate("Game_Window", "MANCALA"))
        if self.mode ==1:
                self.lbl_level.setText(_translate("Game_Window", l[self.level]))
        self.btn_exit.setText(_translate("Game_Window", "Salir"))
        self.btn_next.setText(_translate("Game_Window", "Siguiente Movimiento"))
    ###
    def btn_next_click(self):
        if self.turn==1:
                # ai 1
                while self.turn ==1:
                        _,action= self.alpha_beta_pruning(self.current_state,self.level,float('-inf'),float('inf'),self.turn)
                        self.action= action
                        self.turn*=-1 #reverse the turn
                        self.change_state()
                        self.draw_state()
                        self.check_turns()
                self.lbl_turn.setText(self.player2)
                self.border_p2()
                self.disable_p1()
        
        elif self.turn==-1:
                # ai 2
                while self.turn ==-1:
                        _,action= self.alpha_beta_pruning(self.current_state,self.level,float('-inf'),float('inf'),self.turn)
                        self.action= action
                        self.turn*=-1 #reverse the turn
                        self.change_state()
                        self.draw_state()
                        self.check_turns()
                        # time.sleep(3)
                self.lbl_turn.setText(self.player1)
                self.border_p1()
                self.disable_p2()
        
        ## check winner
        if self.check_if_winner():
            self.btn_next.setEnabled(False)
            p1 = self.current_state[6]
            p2 = self.current_state[13]
            if p1> p2:
                self.lbl_turn.setText("{} Wins!".format(self.player1))
            elif p1< p2:
                self.lbl_turn.setText("{} Wins!".format(self.player2))
            else:
                self.lbl_turn.setText("Empate!")  
        
        # print(self.current_state)
        self.draw_state()

### button functions#########################################################
    def btn_exit_click(self):
        v=messagebox.askyesno("Mancala","Estas seguro es que quieres salir?")
        
        if v:
                self.current_state=np.array([4,4,4,4,4,4,0,4,4,4,4,4,4,0],dtype='int')
                self.draw_state()
                self.Game_Window.close()
                self.back_window, self.back_ui = showings.show_start_page()

    def disable_p2(self):
        # disable player 2
        self.btn_p21.setEnabled(False)
        self.btn_p22.setEnabled(False)
        self.btn_p23.setEnabled(False)
        self.btn_p24.setEnabled(False)
        self.btn_p25.setEnabled(False)
        self.btn_p26.setEnabled(False)
    
    def enable_p2(self):
        # enable player 2
        self.btn_p21.setEnabled(True)
        self.btn_p22.setEnabled(True)
        self.btn_p23.setEnabled(True)
        self.btn_p24.setEnabled(True)
        self.btn_p25.setEnabled(True)
        self.btn_p26.setEnabled(True)
    
    def enable_p1(self):
        # enable player 1
        self.btn_p11.setEnabled(True)
        self.btn_p12.setEnabled(True)
        self.btn_p13.setEnabled(True)
        self.btn_p14.setEnabled(True)
        self.btn_p15.setEnabled(True)
        self.btn_p16.setEnabled(True)
    
    def disable_p1(self):
        # disable player 1
        self.btn_p11.setEnabled(False)
        self.btn_p12.setEnabled(False)
        self.btn_p13.setEnabled(False)
        self.btn_p14.setEnabled(False)
        self.btn_p15.setEnabled(False)
        self.btn_p16.setEnabled(False)


    def border_p1(self):
        # draw p1
        self.btn_p11.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p12.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p13.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p14.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p15.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        self.btn_p16.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        # clear p2 #############################################
        self.btn_p21.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p22.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p23.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p24.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p25.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        self.btn_p26.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
    def border_p2(self):
        # draw p2
        self.btn_p21.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p22.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p23.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p24.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        self.btn_p25.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        self.btn_p26.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#ff7b54;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : #00ead3; "
                             "border-left-color :#00ead3;"
                             "border-right-color :#00ead3;"
                             "border-bottom-color : #00ead3")
        
        # clear p1 #############################################
        self.btn_p11.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p12.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p13.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p14.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        
        self.btn_p15.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")
        self.btn_p16.setStyleSheet("font: 20pt \\\"MV Boli\\\";\n"
"background:#e8e8e8;\n"
"color:#222831;\n"
"border-radius:12px;"
"border :4px solid ;"
                             "border-top-color : None; "
                             "border-left-color :None;"
                             "border-right-color :None;"
                             "border-bottom-color : None")


    def btn_click(self,no):
        self.action =no
        
        self.turn*=-1 #reverse the turn
        self.change_state()
        self.draw_state()
        self.check_turns()
        # time.sleep(0.5)

        while self.turn ==-1:
                _,action= self.alpha_beta_pruning(self.current_state,self.level,float('-inf'),float('inf'),self.turn)
                self.action= action
                self.turn*=-1 #reverse the turn
                self.change_state()
                self.draw_state()
                self.check_turns()
                # time.sleep(1)

        ## check winner
        if self.check_if_winner():
            p1 = self.current_state[6]
            p2 = self.current_state[13]
            if p1> p2:
                self.lbl_turn.setText("El {} ha ganado!".format(self.player1))
            elif p1<p2:
                self.lbl_turn.setText("La {} ha ganado!".format(self.player2))
            else:
                self.lbl_turn.setText("Empate!")
        
        # print(self.current_state)
        self.draw_state()

    def check_turns(self):
        if self.turn == 1:
            # enable player 1
            self.enable_p1()
            self.border_p1()
            self.lbl_turn.setText(self.player1)

            # disable player 2
            self.disable_p2()
        else:
            # enable player 2
            self.enable_p2()
            self.border_p2()
            self.lbl_turn.setText(self.player2)

            # disable player 1
            self.disable_p1()

    ###
    def draw_state(self):
        widgets= [self.btn_p11,
                  self.btn_p12,
                  self.btn_p13,
                  self.btn_p14,
                  self.btn_p15,
                  self.btn_p16,
                  self.txt_player1_score,
                  self.btn_p21,
                  self.btn_p22,
                  self.btn_p23,
                  self.btn_p24,
                  self.btn_p25,
                  self.btn_p26,
                  self.txt_player2_score]
        
        for i in range(len(self.current_state)):
            widgets[i].setText(str(self.current_state[i]))


    def change_state(self):
        '''
        algo:
            change the current state depending on the action
        '''
        try:
                if self.current_state[self.action] !=0:
                        clicked_stone= self.current_state[self.action]
                        self.current_state[self.action]=0
                        

                        ## check which player plays
                        if self.action >=0 and self.action <6:
                                skipped= 13
                                required= 6
                        elif self.action >=7 and self.action <13:
                                skipped=6
                                required= 13


                        i = self.action
                        while clicked_stone:
                                i=(i+1) % 14
                                if i != skipped: #don't increase oponnent's score
                                        self.current_state[i]+=1
                                        clicked_stone-=1

                                
                        ## reverse turn
                        if (i) == required:
                                self.turn*=-1 #reverse the turn 
                        
                        # stealing
                        if self.current_state[i] ==1 and self.current_state[12-(i)] and self.stealing and (i)>=0 and (i)<6 and self.turn==-1: #player 1 , turn is reversed
                                #steal from the oponent
                                self.current_state[required] += (self.current_state[12-(i)] +1)
                                self.current_state[i]=0
                                self.current_state[12-(i)]=0
                        
                        if self.current_state[i] ==1 and self.current_state[12-(i)] and self.stealing and (i)>=7 and (i)<13 and self.turn ==1: #player 2 , turn is reversed
                                #steal from the oponent
                                self.current_state[required] += (self.current_state[12-(i)] +1)
                                self.current_state[i]=0
                                self.current_state[12-(i)]=0
                else:
                        self.turn*=-1
                        messagebox.showerror("404","Movimiento invalido, no puedes elegir un cuenco con 0 fichas!")
        except Exception as e: 
                print(self.current_state)

    def check_if_winner(self):
        if np.sum(self.current_state[:6]) == 0:
            self.current_state[13] += np.sum(self.current_state[7:13])
            self.current_state[7:13] = 0
            self.disable_p1()
            self.disable_p2()
            return 1
            

        elif np.sum(self.current_state[7:13]) == 0:
            self.current_state[6] += np.sum(self.current_state[:6])
            self.current_state[:6]=0
            self.disable_p1()
            self.disable_p2()
            return 1
        
        return 0
##########################################################################
    # AI Functions
    def get_state(self,org_state,action,turn,stealing=True):
        '''
        algo:
            change the current state depending on the action
        '''
        state= org_state.copy()
        if state[action] !=0:
                clicked_stone= state[action]
                state[action]=0
                

                ## check which player plays
                if action >=0 and action <6:
                        skipped= 13
                        required= 6
                elif action >=7 and action <13:
                        skipped=6
                        required= 13


                i = action
                while clicked_stone:
                        i=(i+1) % 14
                        if i != skipped: #don't increase oponnent's score
                                state[i]+=1
                                clicked_stone-=1

                        
                ## reverse turn
                if (i) != required:
                        turn*=-1 #reverse the turn 
                
                # stealing
                if state[i] ==1 and state[12-(i)] and stealing and (i)>=0 and (i)<6 and turn: #player 1 , turn is reversed
                        #steal from the oponent
                        state[required] += (state[12-(i)] +1)
                        state[i]=0
                        state[12-(i)]=0
                
                if state[i] ==1 and state[12-(i)] and stealing and (i)>=7 and (i)<13 and turn ==1: #player 2 , turn is reversed
                        #steal from the oponent
                        state[required] += (state[12-(i)] +1)
                        state[i]=0
                        state[12-(i)]=0
                
                return state,action,turn
                
        else:
                return state,None,turn
        

    def possible_states(self,state,turn,stealing=True):
        if turn == 1:
                actions = np.array([0,1,2,3,4,5],dtype='int')
        elif turn ==-1:
                actions = np.array([7,8,9,10,11,12],dtype='int')
        
        org_state = state.copy()
        orig_turn = turn
        states=[]
        for action in actions:
                state,action,turn = self.get_state(org_state,action,orig_turn,stealing)
                if action is not None:
                        states.append((state,action,turn))
        
        return np.array(states, dtype=object)

    def if_ended(self,state):
        state = state.copy()
        if np.sum(state[:6]) == 0:
            state[13] += np.sum(state[7:13])
            state[7:13] = 0
            return 1,state
            

        elif np.sum(state[7:13]) == 0:
            state[6] += np.sum(state[:6])
            state[:6]=0
            return 1,state
        
        return 0,state

    def alpha_beta_pruning(self,state,depth,alpha,beta,turn): 

        if_win,r_state= self.if_ended(state)
        if depth==0 or if_win:
                return r_state[6]-r_state[13],None #evalutation function value
        
        # maximizer
        if turn ==1:
                value = float('-inf') 
                childs= self.possible_states(state,turn,self.stealing)
                a=None
                for child in childs:
                        c_state=child[0]
                        c_action= child[1]
                        c_turn= child[2]

                        n_value,_= self.alpha_beta_pruning(c_state,depth-1,alpha,beta,c_turn)
                        if n_value> value:
                                value= n_value
                                a= c_action
                        
                        if value>= beta: #pruning
                                break

                        alpha= max(alpha,value)
                return value,a
        
        # minimizer
        elif turn ==-1:
                value = float('inf') 
                childs= self.possible_states(state,turn,self.stealing)
                a=None
                for child in childs:
                        c_state=child[0]
                        c_action= child[1]
                        c_turn= child[2]

                        n_value,_= self.alpha_beta_pruning(c_state,depth-1,alpha,beta,c_turn)
                        if n_value< value:
                                value= n_value
                                a= c_action
                        
                        if value<= alpha: #pruning
                                break

                        beta= min(beta,value)
                return value,a

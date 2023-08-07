from PyQt5 import QtWidgets
from level_page import Ui_Level_Window
from game_page import Ui_Game_Window
from start_page import Ui_Start_Window
import time

def show_start_page():
    new_window= QtWidgets.QMainWindow()
    ui =Ui_Start_Window()
    ui.setupUi(new_window)
    new_window.show()
    return new_window,ui

def show_level_page(no,s):
    new_window= QtWidgets.QMainWindow()
    ui =Ui_Level_Window(no,s)
    ui.setupUi(new_window)
    new_window.show()
    return new_window,ui

def show_game_page(mode,stealing,level=1,turn=1):
    new_window= QtWidgets.QMainWindow()
    ui =Ui_Game_Window(mode,stealing,level,turn)
    ui.setupUi(new_window)
    new_window.show()
    return new_window,ui
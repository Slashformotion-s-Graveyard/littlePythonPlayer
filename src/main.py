import Library
import Player
import pathlib
import time
from PySide2 import QtWidgets
from ui import window

class App(QtWidgets.QMainWindow, window.Ui_Window):
    def __init__(self):
        super().__init__()
        self.ui = window.Ui_Window()
        self.ui.setupUi(self)
        path = pathlib.Path("/home/slash/Documents/Programmation/littlePythonPlayer/music") # DEBUG: not for prod
        self.library = Library.Library(path)
        self.player = Player.Player(self.library)
        self.setup_connections()
        self.player.launch()

        #self.ui = None

    def setup_connections(self):
        self.ui.btn_playpause.clicked.connect(self.player.pause_resume)
        self.ui.btn_next.clicked.connect(self.player.next_track)
        self.ui.btn_previous.clicked.connect(self.player.previous_track)

    

if __name__ == "__main__":
    qt_app = QtWidgets.QApplication()
    app = App()
    app.show()
    qt_app.exec_() 



    """app.player.play()
    while 1:
        try:
            time.sleep(0.001)
            app.player.boucle()

        except KeyboardInterrupt:
            app.player.stop()
            print("end")
            break"""
             

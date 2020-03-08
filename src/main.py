import Library
import Player
import pathlib
import time
class App():
    def __init__(self):
        path = pathlib.Path("/home/slash/Documents/Programmation/littlePythonPlayer/music") # DEBUG: not for prod
        self.library = Library.Library(path)
        self.player = Player.Player(self.library)
        self.ui = None

    

if __name__ == "__main__":
    app = App()
    app.player.play()
    while 1:
        try:
            time.sleep(0.001)
            app.player.boucle()

        except KeyboardInterrupt:
            print("end")
            break
             

import os
import pygame.mixer as pm
import Library
import Track


class Player():
    def __init__(self, library):
        pm.init()
        self.library = library
        self.index = 2
        self.sound = None
        self.paused = True
        self.initialise()
        
    
    def initialise(self):
        self._load()

        
    def next_track(self):
        print("next")
        self.index +=1
        self._load()
        self._play()

    def previous_track(self):
        print("previous")
        self.index += -1
        self._load()
        self._play()


    def _load(self):
        track = self.library.get_track_number(self.index)
        self.sound = pm.Sound(track.get_abs_path())
        
    def launch(self):
        self._play()
        self.paused = False



    def _get_state(self):
        return pm.get_busy() # NOTE: return bool

    def _play(self):
        if not self._get_state():
            self.sound.play()
            
        else:
            self.stop()
            self.sound.play()
            
    def pause_resume(self):
        if self.paused:
            self.unpause()
        else:
            self.pause()


    def boucle(self):
        if not self._get_state():
            self.next_track()

    def pause(self):
        pm.pause()
        self.paused = True

    def unpause(self):
        pm.unpause()
        self.paused = False
    
    
    def stop(self):
        pm.stop()

    

if __name__ == "__main__":
    import pathlib
    path = pathlib.Path("/home/slash/Documents/Programmation/littlePythonPlayer/music") # DEBUG: not for prod
    library = Library.Library(path)
    p = Player(library)
    p.launch()


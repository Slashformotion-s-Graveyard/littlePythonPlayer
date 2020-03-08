import os
import pygame.mixer as pm
import Library
import Track


class Player():
    def __init__(self, library):
        pm.init()
        self.library = library
        self.index = 1
        self.sound = None
        self.initialise()
        
    
    def initialise(self):
        self._load()

        
    def next_track(self):
        self.index +=1
        self._load()
        self.play()

    def previous_song(self):
        self.index += -1
        self._load()
        self.play()


    def _load(self):
        track = self.library.get_track_number(self.index)
        self.sound = pm.Sound(track.get_abs_path())
        



    def _get_state(self):
        return pm.get_busy() # NOTE: return bool

    def play(self):
        if not self._get_state():
            self.sound.play()
        else:
            self.stop()
            self.sound.play()

    def boucle(self):
        if not self._get_state():
            self.next_track()

    def pause(self):
        pm.pause()

    def unpause(self):
        pm.unpause()
    
    
    
    def stop(self):
        pm.stop()

    
import json
import pathlib
import Track
import os
class Library():

    


    def __init__(self, path):
        self.path = path
        self.description = ''
        self.name = None # NOTE: by default it is the name of the folder
        self.tracks = []
        self.patterns = ["ogg" ,"flv", "wma", ".wav", ".flac", "aac", "mp3" ]  # NOTE: not  production possibility, this list of file type supported is not exaustive
        self.build()
        
    def build(self):
        
        for elem in sorted(self.path.rglob('*')): # NOTE: <sorted(self.path.glob("**/*"))> gives every file and folder in self.path
            print(type(elem), elem)
            if elem.is_file() and elem.suffix in self.patterns:
                
                self.tracks.append(Track.Track(elem))
        
    def sanity_check(self):
        
        if not self.path.exists():
            raise FileNotFoundError
        for track in self.tracks:
            if not track.sanity_check():
                raise FileNotFoundError
        
    ###### guetteur
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_library_size(self):
        return len(self.tracks)
    
    def get_track_number(self, number):
        assert type(number) is int
        return self.tracks[number%self.get_library_size()]
        




if __name__ == "__main__":
    l_path  = pathlib.Path("/home/slash/Documents/Programmation/littlePythonPlayer/tests")
    l = Library(l_path)
    print(l.build())

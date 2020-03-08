import os
import pathlib

class Track():

   

    def __init__(self, path):
        
        self.path = path
        self.name = self.get_name()

    
    def unpack(self, raw_track):
        self.path  = pathlib.Path(raw_track['path'])
        self.nom  = raw_track['nom']
   
    def pack(self):
        raw_track = {}
        raw_track['path'] = os._fspath(self.path)
        raw_track['nom'] = self.nom 
        raw_track['__track__'] = True
        return raw_track

    def get_ext(self):
        return self.path.suffix

    def get_path(self):
        return self.path
    
    def get_abs_path(self):
        return str(self.path.resolve())
    
    def get_name(self):
        return self.path.stem

    def sanity_check(self):
        return self.path.exists()
        

if __name__ == '__main__':
    pass

    

    

        
    
        
        

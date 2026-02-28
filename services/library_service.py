
class LibraryService:
    def __init__(self, cache_data):
        self.cache_data = cache_data
        
    def get_local_musics_path(self):
        local = self.cache_data.get_local_path()
        return str(local)
    
    def get_musics(self):
        musics = self.cache_data.get_music_list()
        return musics
    
    def set_local_path_musics(self, path):
        self.cache_data.set_local_path(path)
        
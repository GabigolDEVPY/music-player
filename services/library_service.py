
class LibraryService:
    def __init__(self, cache_data):
        self.cache_data = cache_data
        
    def get_local_musics_path(self):
        json = self.cache_data.get_json_data()
        return str(json["path"])
    
    def get_json(self):
        return self.cache_data.get_json_data()

    def get_musics(self):
        musics = self.cache_data.get_music_list()
        return musics
    
    def set_json(self, json_data):
        self.cache_data.set_json(json_data)
        
    def reload_data(self):
        self.cache_data.init_data()
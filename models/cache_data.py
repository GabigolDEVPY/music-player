from PySide6.QtCore import Signal, QObject
from services.storage_service import StorageService
from services.playlist_service import PlaylistService
from services.music_service import MusicService
from typing import Any

class CacheData(QObject):
    
    reload_data = Signal(Any)
    
    def __init__(self):
        super().__init__()
        self.playlists = PlaylistService.get_playlists()
        self.json_data = []
        self.songs = []
        
    def get_playlists(self):
        return self.playlists
    
    def get_music_list(self):
        return self.songs
    
    def get_json_data(self):
        return self.json_data
    
    def set_playlists(self, playlists):
        self.playlists = playlists
        
    def set_json(self, data=None):
        if data:
            self.json_data = data
            StorageService.save_json(data)
            self.init_data()
            return
        self.json_data = StorageService.load_json()
        
    def set_songs(self, songs):
        self.songs = songs
        
    def init_data(self):
            self.set_json()
            print("local musics cache data",self.json_data)

            songs = MusicService.load_folder_musics(self.json_data)
            playlists = PlaylistService.get_playlists()

            self.set_songs(songs)
            self.set_playlists(playlists)
            self.reload_data.emit(self.json_data)

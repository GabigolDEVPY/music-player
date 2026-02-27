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
        self.local_path = StorageService.load_path_musics()
        self.songs = MusicService.load_folder_musics(self.local_path)
        self.cards = []
    
    def get_cards(self):
        return self.cards
        
    def get_playlists(self):
        return self.playlists
    
    def get_music_list(self):
        return self.songs
    
    def get_local_path(self):
        return self.local_path
    
    def set_playlists(self, playlists):
        self.playlists = playlists
        
    def set_local_path(self, path):
        self.local_path = path
        self.init_data()
        
    def set_songs(self, songs):
        self.songs = songs
        
    def set_cards(self, cards):
        self.cards = cards
        
    def init_data(self):
        songs = MusicService.load_folder_musics(self.local_path)
        playlists = PlaylistService.get_playlists()

        self.set_songs(songs)
        self.set_playlists(playlists)
        
        self.reload_data.emit(self.local_path)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QObject
import qtawesome as qta
from services.storage_service import StorageService
from services.playlist_service import PlaylistService
from services.music_service import MusicService


class CacheData(QObject):
    def __init__(self):
        super().__init__()
        self.playlists = PlaylistService.get_playlists()
        self.local_path = StorageService.load_path_musics()
        self.songs = MusicService.load_folder_musics(self.local_path)
    
    def get_playlists(self):
        return self.playlists
    
    def get_music_list(self):
        return self.songs
    
    def get_local_path(self):
        return self.local_path
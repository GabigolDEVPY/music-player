from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QObject
import qtawesome as qta
from models.playlist import Playlist

class Playlist(QObject):
    def __init__(self):
        super().__init__()
        self.playlists = []
        self.current_playlist = None
    
    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
    
    def delete_music_playlist(self, position):
        for music in self.current_playlist.musics:
            if music.position == position:
                self.current_playlist.musics.remove(music)
    
    def add_music_in_playlist(self, music):
        self.current_playlist.musics.append(music)
        
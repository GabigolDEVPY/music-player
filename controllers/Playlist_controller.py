from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QObject
import qtawesome as qta
from models.playlist import Playlist

class Playlist(QObject):
    def __init__(self):
        super().__init__()
        self.playlists = []
    
    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        
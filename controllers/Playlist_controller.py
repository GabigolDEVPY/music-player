from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QObject
import qtawesome as qta
from components.playlist_card import PlaylistCard
from models.playlist import Playlist


class Playlist(QObject):
    def __init__(self, cache_data, local_panel):
        super().__init__()
        self.cache_data = cache_data
        self.local_panel = local_panel
        self.playlists = cache_data.get_playlists()
        self.current_playlist = None
        self.populate_panel_playlists()
        self._connect_signals()

    def _connect_signals(self):
        self.local_panel

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
    

    def delete_music_playlist(self, position):
        for music in self.current_playlist.musics:
            if music.position == position:
                self.current_playlist.musics.remove(music)
    

    def add_music_in_playlist(self, music):
        self.current_playlist.musics.append(music)
        
    def populate_panel_playlists(self):
        for playlist in self.playlists:
            card = PlaylistCard(
                title=playlist.title,
                description=playlist.description,
                music_count=playlist.music_count,
                playlist_id=playlist.playlist_id
            )
            self.local_panel.playlist_layout.addWidget(card)
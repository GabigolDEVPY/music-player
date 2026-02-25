from PySide6.QtCore import QObject
from components.playlist_card import PlaylistCard
from models.playlist import Playlist


class Playlist(QObject):
    def __init__(self, cache_data, local_panel):
        super().__init__()
        self.cache_data = cache_data
        self.local_panel = local_panel
        self.current_playlist = None
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
        
    def populate_panel_playlists(self, playlists):
        self.clear_layout_and_cards()
        for playlist in playlists:
            card = PlaylistCard(
                title=playlist.title,
                description=playlist.description,
                music_count=playlist.music_count,
                playlist_id=playlist.playlist_id
            )
            self.local_panel.playlist_layout.addWidget(card)
            
    def clear_layout_and_cards(self):
        while self.local_panel.playlist_layout.count():
            item = self.local_panel.playlist_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
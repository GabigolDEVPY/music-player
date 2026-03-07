from PySide6.QtCore import QObject
from components.playlist.playlist_card import PlaylistCard
from models.playlist import Playlist
from PySide6.QtWidgets import QFileDialog
from components.playlist.playlist_cards_musics import MusicCard
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QSize, QRect
from styles.set_cover_playlist import set_default_cover, set_cover_photo



class PlaylistController(QObject):
    def __init__(self, local_panel, playlist_dialog_create, playlist_service):
        super().__init__()
        self.playlist_service = playlist_service
        self.local_panel = local_panel
        self.playlist_dialog_create = playlist_dialog_create
        self.current_playlist = None
        self._connect_signals()

    def _connect_signals(self):
        self.local_panel
        self.local_panel.btn_new_playlist.clicked.connect(self._open_new_playlist)
        self.playlist_dialog_create.btn_cover.clicked.connect(self.select_cover_photo)
        self.playlist_dialog_create.btn_create.clicked.connect(self.create_playlist)
        
    def _open_new_playlist(self):
        self.populate_playlist_new_modal_with_musics()
        self.playlist_dialog_create.btn_cancel.clicked.connect(self.playlist_dialog_create.reject)
        self.playlist_dialog_create.btn_close.clicked.connect(self.playlist_dialog_create.reject)
        self.playlist_dialog_create.btn_create.clicked.connect(self.playlist_dialog_create.accept)
        self.playlist_dialog_create.exec()
    
    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        


    def select_cover_photo(self):
        path, _ = QFileDialog.getOpenFileName(self.local_panel,"Select cover photo","","Images (*.png *.jpg *.jpeg *.webp)")
        if not path:
            return
        
        self.playlist_service.select_cover_photo(path)
        btn = self.playlist_dialog_create.btn_cover
        set_cover_photo(btn, path)


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
                playlist_id=playlist.playlist_id,
                cover_path=playlist.cover_path
            )
            self.local_panel.playlist_layout.addWidget(card)
            
    def clear_layout_and_cards(self):
        while self.local_panel.playlist_layout.count():
            item = self.local_panel.playlist_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
    def clear_layout_musics(self):
        while self.playlist_dialog_create.songs_layout.count():
            item = self.playlist_dialog_create.songs_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    
    def populate_playlist_new_modal_with_musics(self):
        self.clear_layout_musics()
        musics = self.playlist_service.get_musics()
        for index, music in enumerate(musics):
            music.position = index
            card = MusicCard(
                        music.title,
                        music.artist,
                        music.duration,
                        music.path,
                        music.icon,
                        music.position
                    )
            self.playlist_dialog_create.songs_layout.addWidget(card)
    

    def get_selected_musics(self):
        selected = []

        for i in range(self.playlist_dialog_create.songs_layout.count()):
            item = self.playlist_dialog_create.songs_layout.itemAt(i)
            widget = item.widget()

            if widget and hasattr(widget, "checkbox"):
                if widget.checkbox.isChecked():
                    selected.append(widget.music_data)

        return selected
    
    def create_playlist(self):
        musics_selected = self.get_selected_musics()
        playlist_name = self.playlist_dialog_create.input_name.text()
        playlist_desc = self.playlist_dialog_create.input_desc.text()
        self.playlist_service.create_playlist(playlist_name, playlist_desc, musics_selected)

        # set default atributes styles
        self.playlist_dialog_create.input_name.clear()
        self.playlist_dialog_create.input_desc.clear()
        set_default_cover(self.playlist_dialog_create.btn_cover)

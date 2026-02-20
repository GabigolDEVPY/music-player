from PySide6.QtWidgets import QFileDialog
from pathlib import Path
from components.music_card import MusicCard
from services.music_service import MusicService
from services.storage_service import StorageService


class LibraryController:
    def __init__(self, local_panel, youtube_panel, player_control):
        self.local_panel = local_panel #mesmo que library panel
        self.youtube_panel = youtube_panel
        self.player = player_control
        self.path_folder_musics = StorageService.load_path_musics()
        self._connect_signals()
        self.cards = []
        
        
    
    def _connect_signals(self):
        self.local_panel.button_local.clicked.connect(self.change_local_path)


    def load_musics(self):
        self.clear_layout_and_cards()
        if not self.path_folder_musics:
            return
        self.local_panel.path_label.setText(str(self.path_folder_musics))
        musics = MusicService.load_folder_musics(self.path_folder_musics)
        cards = []
        
        for index, music in enumerate(musics):
            music.position = index
        self.player.set_playlist(musics)
        for music in musics:
            card = MusicCard(
                        music.title,
                        music.artist,
                        music.duration,
                        music.path,
                        music.icon,
                        music.position
                    )
            card.clicked.connect(self.player.handle_music_selected)
            self.local_panel.music_layout.addWidget(card)
            cards.append(card)
        self.set_cards(cards)

                
    def change_local_path(self):
        path = QFileDialog.getExistingDirectory(self.local_panel, "Select paste")
        if path:
            self.path_folder_musics = Path(path)
            StorageService.save_path_musics(path)
            self.load_musics()
            
    def clear_layout_and_cards(self):
        self.player.clear_music_lists()
        self.cards.clear()
        while self.local_panel.music_layout.count():
            item = self.local_panel.music_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
    def set_cards(self, cards):
        self.cards = cards
    
    def select_card_by_position(self, music_data):
        position = music_data.position
        for i, card in enumerate(self.cards):
            if i == position:
                card.setFocus()
                # Garante que o scroll acompanhe a música se ela pular sozinha
                self.local_panel.scroll.ensureWidgetVisible(card)
            else:
                card.clearFocus()
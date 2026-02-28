from PySide6.QtWidgets import QFileDialog
from pathlib import Path
from components.music_card import MusicCard
from services.storage_service import StorageService


class LibraryController:
    def __init__(self, local_panel, player_control, library_service):
        self.local_panel = local_panel # mesmo que library panel
        self.player = player_control
        self.library_service = library_service
        self.cards = []
        
        # call functions
        self._connect_signals()
        
    def _connect_signals(self):
        self.local_panel.button_local.clicked.connect(self.change_local_path)
        self.local_panel.btn_reload.clicked.connect(self.reload_data)
        
        
    def set_label_path_text(self, path):
        self.local_panel.path_label.setText(str(path))
    

    def populate_musics_panel(self):
        self.clear_layout_and_cards()
        musics = self.library_service.get_musics()
        cards = []
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
            cards.append(card)
            card.clicked.connect(self.player.handle_music_selected)
            self.cards.append(card)
            self.local_panel.music_layout.addWidget(card)
            

    def change_local_path(self):
        path = QFileDialog.getExistingDirectory(self.local_panel, "Select paste")
        if path:
            StorageService.save_path_musics(path)
            self.set_label_path_text(path)
            self.library_service.set_local_path_musics(path)
            
    def reload_data(self):
        self.cache_data.init_data()

    def clear_layout_and_cards(self):
        self.cards.clear()
        while self.local_panel.music_layout.count():
            item = self.local_panel.music_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
    

    def select_card_by_position(self, music_data):
        position = music_data.position
        for i, card in enumerate(self.cards):
            if i == position:
                card.setFocus()
                # Garante que o scroll acompanhe a música se ela pular sozinha
                self.local_panel.scroll.ensureWidgetVisible(card)
            else:
                card.clearFocus()
                
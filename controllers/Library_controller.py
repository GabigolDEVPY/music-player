from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                            QLineEdit, QSlider, QFrame, QTabWidget, QFileDialog)
import sys
import os
from pathlib import Path
from components.music_card import MusicCard
from services.music_service import MusicService


class LibraryController:
    def __init__(self, local_panel, youtube_panel, player_control):
        self.local_panel = local_panel
        self.youtube_panel = youtube_panel
        self.player = player_control
        self.path_folder_musics = MusicService.load_path_musics()


    def load_musics(self):
        self.clear_layout(self.local_panel.music_layout)
        self.player.musics_list.clear()
        self.player.cards.clear()
        if not self.path_folder_musics:
            return
        self.local_panel.path_label.setText(str(self.path_folder_musics))
        musics = MusicService.get_local_musics(self.path_folder_musics)
        position = 0
        for music in musics:
            music["position"] = position
            self.player.musics_list.append(music)
            card = MusicCard(
                        music["title"],
                        music["artist"],
                        music["duration"],
                        music["path"],
                        music["icon"],
                        music["position"]
                    )
            card.clicked.connect(self.player.handle_music_selected)
            self.local_panel.music_layout.addWidget(card)
            self.player.cards.append(card)
            position += 1


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
    def change_local_path(self):
        path = QFileDialog.getExistingDirectory(self.local_panel, "Select paste")
        if path:
            self.path_folder_musics = Path(path)
            MusicService.save_path_musics(path)
            self.load_musics()
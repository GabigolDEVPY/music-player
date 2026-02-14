from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                               QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import sys
import os
from components.player_control import PlayerControl
from components.search_bar import SearchBar
from components.side_panel import SidePanel
from PySide6.QtWidgets import QStackedWidget
from components.youtube_panel import YouTubePanel
from components.music_card import MusicCard
from services.music_service import MusicService
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
MUSIC_ROOT = ROOT_DIR / "musicas"

class LibraryController:
    def __init__(self, local_panel, youtube_panel, player):
        self.local_panel = local_panel
        self.youtube_panel = youtube_panel
        self.player = player
        self.path_folder_musics = MUSIC_ROOT


    def load_musics(self):
        self.clear_layout(self.local_panel.music_layout)
        musics = MusicService.get_local_musics(self.path_folder_musics)
        for music in musics:
            card = MusicCard(
                        music["title"],
                        music["artist"],
                        music["duration"],
                        music["path"],
                        music["icon"]
                    )
            card.clicked.connect(self.player.handle_music_selected)
            self.local_panel.music_layout.addWidget(card)


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
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
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
MUSIC_ROOT = ROOT_DIR / "musicas"

class PanelController:
    def __init__(self, stacked_panel, youtube_panel, library_panel, player):
        self.stacked_panel = stacked_panel
        self.youtube_panel = youtube_panel
        self.library_panel = library_panel
        self.player = player


    def change_panel(self, index):
        self.stacked_panel.setCurrentIndex(index)
        if index == 0:
            self.clear_layout(self.library_panel.music_layout)
                # Adicionar músicas exemplo
            for file in os.listdir(MUSIC_ROOT):
                if file.lower().endswith(".mp3"):
                    audio = MP3(MUSIC_ROOT / file)
                    tags = EasyID3(MUSIC_ROOT / file)
                    id3 = ID3(MUSIC_ROOT / file)
                    cover_data = None
                    for tag in id3.values():
                        if tag.FrameID == "APIC":
                            cover_data = tag.data
                            break
                    pixmap = None
                    if cover_data:
                        pixmap = QPixmap()
                        pixmap.loadFromData(cover_data)    

                    card = MusicCard(
                        tags.get("title", ["Sem titulo"])[0],
                        tags.get("artist", ["Desconhecido"])[0],
                        str(audio.info.length),
                        MUSIC_ROOT / file,
                        pixmap
                    )
                    card.clicked.connect(self.player.handle_music_selected)
                    self.library_panel.music_layout.addWidget(card)


        elif index == 1:
            self.clear_layout(self.youtube_panel.music_layout)
            musicas = [
            ("Brinding", "The Weeknd", "3:20"),
            ("top de mais", "Dua Lipa", "3:23"),
            ]
            for titulo, artista, duracao in musicas:
                card = MusicCard(titulo, artista, duracao)
                self.youtube_panel.music_layout.addWidget(card)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

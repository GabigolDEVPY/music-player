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
    def __init__(self, stacked_panel, library_controller):
        self.stacked_panel = stacked_panel
        self.library_controller = library_controller


    def change_panel(self, index):
        self.stacked_panel.setCurrentIndex(index)
        if index == 0:
            self.library_controller.load_musics()


        elif index == 1:
            pass



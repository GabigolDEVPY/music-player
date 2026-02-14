from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                            QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QStackedLayout
import sys
from PySide6.QtCore import QUrl

class PlayerController:
    def __init__(self, player):
        self.player = player       
        self.player.stacked_layout.setCurrentIndex(0) 


    def change_status_play(self):
        if self.player.music_player.isPlaying():
            self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
            self.player.music_player.pause()
        else:
            self.player.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))


    def handle_music_selected(self, music_data):
        self.player.stacked_layout.setCurrentIndex(1)
        self.player.music_player.setSource(QUrl.fromLocalFile(music_data["path"]))
        self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        self.player.song_title.setText(music_data["title"])
        self.player.artist_name.setText(music_data["artist"])
        self.player.album_icon.setPixmap(music_data["icon"])
        self.player.time_total.setText(music_data["duration"])
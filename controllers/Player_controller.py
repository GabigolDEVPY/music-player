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
        self.musics_list = []
        self.current_music = None
        self.repeat = False
        self.random = False
        self.player.stacked_layout.setCurrentIndex(0) 


    def change_status_play(self):
        if self.player.music_player.isPlaying():
            self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
            self.player.music_player.pause()
        else:
            self.player.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))


    def handle_music_selected(self, music_data):
        self.current_music = music_data
        self.player.stacked_layout.setCurrentIndex(1)
        self.player.music_player.setSource(QUrl.fromLocalFile(music_data["path"]))
        self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        self.player.song_title.setText(music_data["title"])
        self.player.artist_name.setText(music_data["artist"])
        self.player.album_icon.setPixmap(music_data["icon"])
        
    def next_music(self, status):
        if status == QMediaPlayer.EndOfMedia:
            try:
                self.handle_music_selected(self.musics_list[self.current_music["position"] + 1])
            except IndexError:
                self.handle_music_selected(self.musics_list[0])
            self.player.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
    def next_music_btn(self, status):
        try:
            self.handle_music_selected(self.musics_list[self.current_music["position"] + 1])
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
        self.player.music_player.play() 
        self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
    def previous_music_btn(self, status):
        try:
            self.handle_music_selected(self.musics_list[self.current_music["position"] - 1])
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
        self.player.music_player.play()
        self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
        
    def update_style(self, button, active=None):
        self.button = button
        if active is True:
            colors = [ "#1bba53", "#4ee783"]
        else:
            colors = [ "#1a1a1a", "#282828"]
            
        btn_style = f"""
            QPushButton {{
                background-color: {colors[0]};
                color: white;
                border: none;
                border-radius: 20px;
            }}
            QPushButton:hover {{
                background-color: {colors[1]};
            }}
        """
        self.button.setStyleSheet(btn_style)

    def random_order(self):
        self.random = not self.random
        if self.random:
            self.repeat = False
            self.update_style(self.player.repeat_btn, active=False)
        self.update_style(self.player.shuffle_btn, active=self.random)
        
            
    def repeat_order(self):
        self.repeat = not self.repeat
        if self.repeat:
            self.random = False
            self.update_style(self.player.shuffle_btn, active=False)
        self.update_style(self.player.repeat_btn, active=self.repeat)
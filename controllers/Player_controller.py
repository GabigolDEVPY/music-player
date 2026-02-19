from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                            QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
import random
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QStackedLayout
from models.enums import RepeatMode, ShuffleMode
import sys
from PySide6.QtCore import QUrl

class PlayerController:
    def __init__(self, player, local_panel):
        self.player = player       
        self.local_panel = local_panel
        self.musics_list = []
        self.current_music = None
        self.cards = []
        self.repeat = RepeatMode.OFF
        self.random = ShuffleMode.OFF
        self.player.stacked_layout.setCurrentIndex(0) 

    def select_card_by_position(self, music_data):
        position = music_data.position
        for i, card in enumerate(self.cards):
            if i == position:
                card.setFocus()
                # Garante que o scroll acompanhe a música se ela pular sozinha
                self.local_panel.scroll.ensureWidgetVisible(card)
            else:
                card.clearFocus()

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
        self.player.music_player.setSource(QUrl.fromLocalFile(music_data.path))
        self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        self.player.song_title.setText(music_data.title)
        self.player.artist_name.setText(music_data.artist)
        self.player.album_icon.setPixmap(music_data.icon)
        
    def next_music(self, status):
        print(self.current_music.__dict__)
        if status == QMediaPlayer.EndOfMedia:
            # 1. Lógica para decidir qual é a próxima música
            if self.repeat == RepeatMode.ON:
                target_music = self.current_music
            elif self.random == ShuffleMode.ON:
                if len(self.musics_list) > 1:
                    new_index = self.current_music.position
                    while new_index == self.current_music.position:
                        new_index = random.randrange(len(self.musics_list))
                    target_music = self.musics_list[new_index]
                else:
                    target_music = self.musics_list[0]
            else:
                try:
                    target_music = self.musics_list[self.current_music.position + 1]
                except IndexError:
                    target_music = self.musics_list[0]

            # 2. Executa a troca e ATUALIZA O FOCO
            self.handle_music_selected(target_music)
            self.select_card_by_position(target_music) # <--- IMPORTANTE: Chama o foco aqui
            
            self.player.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
    def next_music_btn(self, status):
        try:
            self.handle_music_selected(self.musics_list[self.current_music.position + 1])
            self.select_card_by_position(self.current_music)
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
            self.select_card_by_position(self.current_music)    
        self.player.music_player.play() 
        self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
    def previous_music_btn(self, status):
        try:
            self.handle_music_selected(self.musics_list[self.current_music.position - 1])
            self.select_card_by_position(self.current_music)
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
            self.select_card_by_position(self.current_music)
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
        if self.random == ShuffleMode.OFF:
            self.random = ShuffleMode.ON
            
            self.repeat = RepeatMode.OFF
            self.update_style(self.player.repeat_btn, active=False)
        else:
            self.random = ShuffleMode.OFF
        self.update_style(self.player.shuffle_btn, active=self.random == ShuffleMode.ON)
        
            
    def repeat_order(self):
        if self.repeat == RepeatMode.OFF:
            self.repeat = RepeatMode.ON
            
            self.random = ShuffleMode.OFF
            self.update_style(self.player.shuffle_btn, active=False)
        else:
            self.repeat = RepeatMode.OFF
        self.update_style(self.player.repeat_btn,active=self.repeat == RepeatMode.ON)
        
        
    def change_volume(self, value):
        volume = value / 100
        self.player.audio_output.setVolume(volume)
    
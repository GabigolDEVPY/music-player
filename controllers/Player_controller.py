import qtawesome as qta
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider)
import random
from styles.button_shuffle_repeat import update_style
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QObject
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from models.enums import RepeatMode, ShuffleMode

class PlayerController(QObject):
    
    music_changed = Signal(object)
    
    def __init__(self, player, cache_data):
        super().__init__()
        self.player = player   
        self.musics_list = cache_data.get_music_list()
        self.current_music = None
        self.repeat = RepeatMode.OFF
        self.random = ShuffleMode.OFF
        self.music_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.music_player.setAudioOutput(self.audio_output)
        
        # call function connect the signals
        self._connect_signals()


    def _connect_signals(self):
        # signals view
        self.music_player.positionChanged.connect(self.update_position)
        self.music_player.durationChanged.connect(self.update_duration)
        self.music_player.mediaStatusChanged.connect(self.next_music)     
        
        #signals player interface
        self.player.progress_slider.sliderMoved.connect(self.set_position)
        self.player.play_btn.clicked.connect(self.change_status_play)
        self.player.next_btn.clicked.connect(self.next_music_btn)
        self.player.prev_btn.clicked.connect(self.previous_music_btn)
        self.player.shuffle_btn.clicked.connect(self.random_order)
        self.player.repeat_btn.clicked.connect(self.repeat_order)
        self.player.volume_slider.valueChanged.connect(self.change_volume)


    def change_status_play(self):
        if self.music_player.isPlaying():
            self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
            self.music_player.pause()
        else:
            self.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))


    def handle_music_selected(self, music_data):
        self.current_music = music_data
        self.music_changed.emit(self.current_music)
        self.player.stacked_layout.setCurrentIndex(1)
        self.music_player.setSource(QUrl.fromLocalFile(music_data.path))
        self.player.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        self.player.song_title.setText(music_data.title)
        self.player.artist_name.setText(music_data.artist)
        self.player.album_icon.setPixmap(music_data.icon)
        
    def next_music(self, status):
        print("musicas do playercontroller",self.musics_list)
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
            self.music_changed.emit(self.current_music)
            
            self.music_player.play()
            self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
    def next_music_btn(self):
        try:
            self.handle_music_selected(self.musics_list[self.current_music.position + 1])
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
        self.music_player.play() 
        self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
            
            
    def previous_music_btn(self):
        try:
            self.handle_music_selected(self.musics_list[self.current_music.position - 1])
        except IndexError:
            self.handle_music_selected(self.musics_list[0])
        self.music_player.play()
        self.player.play_btn.setIcon(qta.icon('fa5s.pause', color='white'))
        

    def random_order(self):
        if self.random == ShuffleMode.OFF:
            self.random = ShuffleMode.ON
            
            self.repeat = RepeatMode.OFF
            update_style(self, self.player.repeat_btn, active=False)
        else:
            self.random = ShuffleMode.OFF
        update_style(self, self.player.shuffle_btn, active=self.random == ShuffleMode.ON)
        
            
    def repeat_order(self):
        if self.repeat == RepeatMode.OFF:
            self.repeat = RepeatMode.ON
            self.random = ShuffleMode.OFF
            update_style(self, self.player.shuffle_btn, active=False)
        else:
            self.repeat = RepeatMode.OFF
        update_style(self, self.player.repeat_btn,active=self.repeat == RepeatMode.ON)
        
        
    def change_volume(self, value):
        volume = value / 100
        self.audio_output.setVolume(volume)
    
    def format_time(self, ms):
        seconds = ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"


    def update_position(self, position):
        self.player.progress_slider.setValue(position)
        self.player.time_current.setText(self.format_time(position))


    def update_duration(self, duration):
        self.player.progress_slider.setRange(0, duration)
        self.player.time_total.setText(self.format_time(duration))


    def set_position(self, position):
        self.music_player.setPosition(position)
    
                
    def set_playlist(self, musics):
        self.musics_list = musics
    
    def clear_music_lists(self):
        self.musics_list = None
        
        
    
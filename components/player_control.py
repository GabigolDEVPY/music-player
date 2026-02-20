from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
import qtawesome as qta
from PySide6.QtWidgets import QStackedLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class PlayerControl(QWidget):
    """Controles do player (direita)"""
    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)

        self.empty_state = self.create_empty_state()
        self.player_state = self.create_player_state()

        self.stacked_layout.addWidget(self.empty_state)
        self.stacked_layout.addWidget(self.player_state)

        self.stacked_layout.setCurrentIndex(0)



    def create_empty_state(self):
        empty_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        label = QLabel("Selecione uma música para começar")
        label.setFont(QFont("Segoe UI", 14))
        label.setStyleSheet("color: #777777;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        empty_widget.setLayout(layout)
        return empty_widget



    def create_player_state(self):
        player_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Capa do álbum com ícone de disco
        album_cover_container = QWidget()
        album_cover_container.setFixedSize(200, 200)
        album_cover_container.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #3B1E54, stop:0.5 #9B59B6, stop:1 #E74C3C);
            border-radius: 8px;
            border: 2px solid #1DB954;
        """)
        
        album_layout = QVBoxLayout(album_cover_container)
        album_layout.setAlignment(Qt.AlignCenter)
        
        self.album_icon = QLabel()
        self.album_icon.setPixmap(qta.icon('fa5s.compact-disc', color='white').pixmap(QSize(70, 70)))
        self.album_icon.setAlignment(Qt.AlignCenter)
        album_layout.addWidget(self.album_icon)
        
        # Info da música tocando
        now_playing = QLabel("Now Playing")
        now_playing.setFont(QFont("Segoe UI", 8))
        now_playing.setStyleSheet("color: #b3b3b3;")
        now_playing.setAlignment(Qt.AlignCenter)
        
        self.song_title = QLabel("Blinding Lights")
        self.song_title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.song_title.setStyleSheet("color: #ffffff;")
        self.song_title.setAlignment(Qt.AlignCenter)
        
        self.artist_name = QLabel("The Weeknd")
        self.artist_name.setFont(QFont("Segoe UI", 11))
        self.artist_name.setStyleSheet("color: #b3b3b3;")
        self.artist_name.setAlignment(Qt.AlignCenter)
        
        # Barra de progresso
        progress_layout = QHBoxLayout()
        
        self.time_current = QLabel("00:00")
        self.time_current.setStyleSheet("color: #b3b3b3; font-size: 9px;")
    
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #404040;
                height: 4px;
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: #1DB954;
                width: 12px;
                height: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::sub-page:horizontal {
                background: #1DB954;
                border-radius: 2px;
            }
        """)
        self.progress_slider.setValue(40)
        
        self.time_total = QLabel()
        self.time_total.setStyleSheet("color: #b3b3b3; font-size: 9px;")
        
        progress_layout.addWidget(self.time_current)
        progress_layout.addWidget(self.progress_slider, 1)
        progress_layout.addWidget(self.time_total)
        
        # Controles de playback com ícones profissionais
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(10)
        
        btn_style = """
            QPushButton {
                background-color: #1a1a1a;
                color: white;
                border: none;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #282828;
            }
        """
        
        play_btn_style = """
            QPushButton {
                background-color: #1DB954;
                color: white;
                border: none;
                border-radius: 24px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
        """
        
        self.shuffle_btn = QPushButton()
        self.shuffle_btn.setIcon(qta.icon('fa5s.random', color='#b3b3b3'))
        self.shuffle_btn.setIconSize(QSize(14, 14))
        self.shuffle_btn.setFixedSize(40, 40)
        self.shuffle_btn.setStyleSheet(btn_style)
        
        self.prev_btn = QPushButton()
        self.prev_btn.setIcon(qta.icon('fa5s.step-backward', color='white'))
        self.prev_btn.setIconSize(QSize(16, 16))
        self.prev_btn.setFixedSize(40, 40)
        self.prev_btn.setStyleSheet(btn_style)
        
        self.play_btn = QPushButton()
        self.play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        self.play_btn.setIconSize(QSize(18, 18))
        self.play_btn.setFixedSize(48, 48)
        self.play_btn.setStyleSheet(play_btn_style)
        
        self.next_btn = QPushButton()
        self.next_btn.setIcon(qta.icon('fa5s.step-forward', color='white'))
        self.next_btn.setIconSize(QSize(16, 16))
        self.next_btn.setFixedSize(40, 40)
        self.next_btn.setStyleSheet(btn_style)
        
        self.repeat_btn = QPushButton()
        self.repeat_btn.setIcon(qta.icon('fa5s.redo', color='#b3b3b3'))
        self.repeat_btn.setIconSize(QSize(14, 14))
        self.repeat_btn.setFixedSize(40, 40)
        self.repeat_btn.setStyleSheet(btn_style)
        
        controls_layout.addStretch()
        controls_layout.addWidget(self.shuffle_btn)
        controls_layout.addWidget(self.prev_btn)
        controls_layout.addWidget(self.play_btn)
        controls_layout.addWidget(self.next_btn)
        controls_layout.addWidget(self.repeat_btn)
        controls_layout.addStretch()
        
        # Volume com ícone
        self.volume_layout = QHBoxLayout()
        
        self.volume_icon_label = QLabel()
        self.volume_icon_label.setPixmap(qta.icon('fa5s.volume-up', color='#b3b3b3').pixmap(QSize(14, 14)))
        
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMaximumWidth(120)
        self.volume_slider.setValue(70)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #404040;
                height: 3px;
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: #ffffff;
                width: 10px;
                height: 10px;
                margin: -4px 0;
                border-radius: 5px;
            }
            QSlider::sub-page:horizontal {
                background: #ffffff;
                border-radius: 2px;
            }
        """)
        
        self.volume_layout.addStretch()
        self.volume_layout.addWidget(self.volume_icon_label)
        self.volume_layout.addWidget(self.volume_slider)
        self.volume_layout.addStretch()
        
        # Adicionar tudo ao layout principal
        layout.addWidget(album_cover_container)
        layout.addWidget(now_playing)
        layout.addWidget(self.song_title)
        layout.addWidget(self.artist_name)
        layout.addSpacing(8)
        layout.addLayout(progress_layout)
        layout.addSpacing(8)
        layout.addLayout(controls_layout)
        layout.addSpacing(12)
        layout.addLayout(self.volume_layout)
        layout.addStretch()
        
        self.shuffle_btn.setFocusPolicy(Qt.NoFocus)
        self.prev_btn.setFocusPolicy(Qt.NoFocus)
        self.play_btn.setFocusPolicy(Qt.NoFocus)
        self.next_btn.setFocusPolicy(Qt.NoFocus)
        self.repeat_btn.setFocusPolicy(Qt.NoFocus)
        self.progress_slider.setFocusPolicy(Qt.NoFocus)
        # A MÁGICA: Define o layout no player_widget e retorna ele
        player_widget.setLayout(layout) 
        return player_widget
        
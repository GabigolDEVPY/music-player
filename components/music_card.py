from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                               QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
from components.marquee_label import MarqueeLabel
import sys
from PySide6.QtCore import Signal

class MusicCard(QFrame):
    """Card individual de música no painel lateral"""
    clicked = Signal(dict)
    def __init__(self, title, artist, duration, path, icon):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFixedHeight(90)
        self.setFixedWidth(280)
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("""
            MusicCard {
                background-color: #1a1a1a;
                border-radius: 6px;
                padding: 8px;
                margin: 4px 0;
            }
            MusicCard:hover {
                background-color: #404040;
            }
            MusicCard:focus {
                background-color: #404040;
            }
        """)
        self.music_data = {
            "title": title,
            "artist": artist,
            "duration": duration,
            "path": path,
            "icon": icon
        }

        layout = QHBoxLayout()
        layout.setSpacing(8)
        
        # Imagem placeholder com ícone de música
        img_container = QWidget()
        img_container.setFixedSize(45, 45)
        img_container.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #1DB954, stop:1 #1ed760);
            border-radius: 4px;
        """)
        
        img_layout = QHBoxLayout(img_container)
        img_layout.setContentsMargins(0, 0, 0, 0)
        
        music_icon = QLabel()
        if icon is not None:
            scaled = icon.scaled(45, 45, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            music_icon.setPixmap(scaled)
        else:
            music_icon.setPixmap(qta.icon('fa5s.music', color='white').pixmap(QSize(18, 18)))
        music_icon.setAlignment(Qt.AlignCenter)
        img_layout.addWidget(music_icon)
        
        # Info da música
        info_layout = QVBoxLayout()
        info_layout.setSpacing(2)
        
        title_label = MarqueeLabel(title)
        title_label.setFont(QFont("Segoe UI", 9, QFont.Bold))
        title_label.setStyleSheet("color: #ffffff;")
        
        artist_label = QLabel(artist)
        artist_label.setFont(QFont("Segoe UI", 8))
        artist_label.setStyleSheet("color: #b3b3b3;")
        
        duration_label = QLabel(duration)
        duration_label.setFont(QFont("Segoe UI", 7))
        duration_label.setStyleSheet("color: #b3b3b3;")
        
        info_layout.addWidget(title_label)
        info_layout.addWidget(artist_label)
        info_layout.addWidget(duration_label)
        info_layout.addStretch()
        
        # Botão download com ícone
        download_btn = QPushButton()
        download_btn.setIcon(qta.icon('fa5s.download', color='white'))
        download_btn.setIconSize(QSize(12, 12))
        download_btn.setText(" DL")
        download_btn.setFixedSize(50, 28)
        download_btn.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border: none;
                border-radius: 14px;
                font-size: 9px;
                font-weight: bold;
                padding-left: 4px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
            QPushButton:pressed {
                background-color: #1aa34a;
            }
        """)
        
        layout.addWidget(img_container)
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addWidget(download_btn)
        self.setLayout(layout)
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFocus()
            self.clicked.emit(self.music_data)
        super().mousePressEvent(event)
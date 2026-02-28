from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QFont
import qtawesome as qta
from components.marquee_label import MarqueeLabel
from models.playlist import Playlist


class PlaylistCard(QFrame):
    """Card individual de playlist no painel lateral"""
    clicked = Signal(object)

    def __init__(self, title, description, music_count, playlist_id):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFixedHeight(90)
        self.setFixedWidth(280)
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("""
            PlaylistCard {
                background-color: #1a1a1a;
                border-radius: 6px;
                padding: 8px;
                margin: 4px 0;
            }
            PlaylistCard:hover {
                background-color: #404040;
            }
            PlaylistCard:focus {
                background-color: #404040;
            }
        """)

        self.playlist_data = Playlist(
            title=title,
            description=description,
            music_count=music_count,
            playlist_id=playlist_id
        )

        layout = QHBoxLayout()
        layout.setSpacing(8)

        # Capa da playlist com ícone
        img_container = QWidget()
        img_container.setFixedSize(45, 45)
        img_container.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #7B2FBE, stop:1 #a855f7);
            border-radius: 4px;
        """)

        img_layout = QHBoxLayout(img_container)
        img_layout.setContentsMargins(0, 0, 0, 0)

        # Info da playlist
        info_layout = QVBoxLayout()
        info_layout.setSpacing(2)

        title_label = MarqueeLabel(title)
        title_label.setFont(QFont("Segoe UI", 9, QFont.Bold))
        title_label.setStyleSheet("color: #ffffff;")

        desc_label = QLabel(description if description else "Sem descrição")
        desc_label.setFont(QFont("Segoe UI", 8))
        desc_label.setStyleSheet("color: #b3b3b3;")
        desc_label.setMaximumWidth(140)
        desc_label.setWordWrap(False)

        # Linha com ícone de música + contagem
        count_layout = QHBoxLayout()
        count_layout.setSpacing(3)
        count_layout.setContentsMargins(0, 0, 0, 0)

        note_icon = QLabel()
        note_icon.setPixmap(qta.icon('fa5s.music', color='#1DB954').pixmap(QSize(9, 9)))

        count_label = QLabel(f"{music_count} música{'s' if music_count != 1 else ''}")
        count_label.setFont(QFont("Segoe UI", 7))
        count_label.setStyleSheet("color: #1DB954;")

        count_layout.addWidget(note_icon)
        count_layout.addWidget(count_label)
        count_layout.addStretch()

        info_layout.addWidget(title_label)
        info_layout.addWidget(desc_label)
        info_layout.addLayout(count_layout)
        info_layout.addStretch()

        # Botão play
        play_btn = QPushButton()
        play_btn.setIcon(qta.icon('fa5s.play', color='white'))
        play_btn.setIconSize(QSize(12, 12))
        play_btn.setFixedSize(32, 32)
        play_btn.setStyleSheet("""
            QPushButton {
                background-color: #7B2FBE;
                border: none;
                border-radius: 16px;
            }
            QPushButton:hover {
                background-color: #a855f7;
            }
            QPushButton:pressed {
                background-color: #6d28d9;
            }
        """)

        layout.addWidget(img_container)
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addWidget(play_btn)
        self.setLayout(layout)

        # Fundos transparentes
        title_label.setAttribute(Qt.WA_TranslucentBackground)
        desc_label.setAttribute(Qt.WA_TranslucentBackground)
        count_label.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFocus()
            self.clicked.emit(self.playlist_data)
        super().mousePressEvent(event)
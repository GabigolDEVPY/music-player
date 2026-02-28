from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QCheckBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
import qtawesome as qta
from components.marquee_label import MarqueeLabel
from models.music import Music
from PySide6.QtCore import Signal

class MusicCard(QFrame):
    """Card individual de música no painel lateral"""
    clicked = Signal(object)

    def __init__(self, title, artist, duration, path, icon, position):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFixedHeight(90)
        self.setFixedWidth(430)
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

        self.music_data = Music(
            title=title,
            artist=artist,
            duration=duration,
            path=path,
            icon=icon,
            position=position
        )

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

        # Checkbox de seleção
        self.checkbox = QCheckBox()
        self.checkbox.setFixedSize(22, 22)
        self.checkbox.setStyleSheet("""
            QCheckBox {
                background: transparent;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 5px;
                border: 2px solid #404040;
                background: transparent;
            }
            QCheckBox::indicator:hover {
                border-color: #1DB954;
            }
            QCheckBox::indicator:checked {
                background-color: #1DB954;
                border-color: #1DB954;
            }
        """)

        layout.addWidget(img_container)
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addWidget(self.checkbox, alignment=Qt.AlignVCenter)
        self.setLayout(layout)

        # Deixar fundos transparentes
        title_label.setAttribute(Qt.WA_TranslucentBackground)
        artist_label.setAttribute(Qt.WA_TranslucentBackground)
        duration_label.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFocus()
            self.checkbox.toggle()
            self.clicked.emit(self.music_data)
        super().mousePressEvent(event)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                               QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
from . music_card import MusicCard
import sys


class SidePanel(QWidget):
    """Painel lateral com lista de músicas"""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #000000;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header do painel com ícone
        header_container = QWidget()
        header_container.setStyleSheet("background-color: #000000; padding: 12px;")
        header_layout = QHBoxLayout(header_container)
        header_layout.setContentsMargins(12, 12, 12, 12)
        
        library_icon = QLabel()
        library_icon.setPixmap(qta.icon('fa5s.book', color='#1DB954').pixmap(QSize(16, 16)))
        
        header_text = QLabel("Youtube")
        header_text.setFont(QFont("Segoe UI", 12, QFont.Bold))
        header_text.setStyleSheet("color: #ffffff;")
        
        header_layout.addWidget(library_icon)
        header_layout.addWidget(header_text)
        header_layout.addStretch()
        
        # Área scrollável
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #000000;
            }
            QScrollBar:vertical {
                background-color: #000000;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #404040;
                border-radius: 6px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #535353;
            }
        """)
        
        # Container das músicas
        self.music_container = QWidget()
        self.music_layout = QVBoxLayout()
        self.music_layout.setContentsMargins(8, 8, 8, 8)
        self.music_layout.setAlignment(Qt.AlignTop)
        self.music_container.setLayout(self.music_layout)
        scroll.setWidget(self.music_container)
        
        # Container para músicas locais (estilizado)
        local_music_container = QWidget()
        local_music_container.setStyleSheet("""
            QWidget {
                background-color: #181818;
                border-top: 1px solid #282828;
            }
        """)
        local_layout = QVBoxLayout(local_music_container)
        local_layout.setContentsMargins(12, 12, 12, 12)
        local_layout.setSpacing(8)
        
        # Label do caminho
        self.path_label = QLabel("Nenhuma pasta selecionada")
        self.path_label.setFont(QFont("Segoe UI", 9))
        self.path_label.setStyleSheet("""
            QLabel {
                color: #b3b3b3;
                background-color: transparent;
                padding: 4px;
            }
        """)
        self.path_label.setWordWrap(True)
        
        # Botão de seleção
        self.button_local = QPushButton()
        self.button_local.setText("  Selecionar Músicas Locais")
        self.button_local.setIcon(qta.icon('fa5s.folder-open', color="#FFFFFF"))
        self.button_local.setIconSize(QSize(16, 16))
        self.button_local.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.button_local.setCursor(Qt.PointingHandCursor)
        self.button_local.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px 20px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #1ed760;
                transform: scale(1.02);
            }
            QPushButton:pressed {
                background-color: #169c46;
            }
        """)
        
        local_layout.addWidget(self.button_local)
        local_layout.addWidget(self.path_label)
        
        layout.addWidget(header_container)
        layout.addWidget(scroll)
        layout.addWidget(local_music_container)
        
        self.setLayout(layout)
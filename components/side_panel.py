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
        
        # Adicionar músicas exemplo

        
        self.music_container.setLayout(self.music_layout)
        scroll.setWidget(self.music_container)
        
        layout.addWidget(header_container)
        layout.addWidget(scroll)
        
        self.setLayout(layout)
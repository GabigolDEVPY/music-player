from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTabWidget)
from PySide6.QtCore import QSize
import qtawesome as qta



class SearchBar(QWidget):
    """Barra de pesquisa com tabs Local/YouTube"""
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 12)
        layout.setSpacing(8)
        
        # Tabs Local/YouTube
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background-color: transparent;
            }
            QTabBar::tab {
                background-color: #1a1a1a;
                color: #b3b3b3;
                padding: 8px 20px;
                margin-right: 4px;
                border-radius: 6px 6px 0 0;
                font-size: 10px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #282828;
                color: #1DB954;
            }
            QTabBar::tab:hover {
                background-color: #282828;
                color: #ffffff;
            }
        """)
        
        local_tab = QWidget()
        youtube_tab = QWidget()
        
        self.tabs.addTab(local_tab, "LOCAL")
        self.tabs.addTab(youtube_tab, "YOUTUBE")
        
        # Barra de pesquisa
        search_layout = QHBoxLayout()
        search_layout.setSpacing(8)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Buscar músicas, artistas ou álbuns...")
        search_input.setStyleSheet("""
            QLineEdit {
                background-color: #242424;
                color: #ffffff;
                border: 2px solid transparent;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 11px;
            }
            QLineEdit:focus {
                border: 2px solid #1DB954;
                background-color: #2a2a2a;
            }
        """)
        
        search_btn = QPushButton()
        search_btn.setIcon(qta.icon('fa5s.search', color='white'))
        search_btn.setIconSize(QSize(14, 14))
        search_btn.setText(" Search")
        search_btn.setFixedSize(100, 36)
        search_btn.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border: none;
                border-radius: 18px;
                font-size: 11px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
            QPushButton:pressed {
                background-color: #1aa34a;
            }
        """)
        
        search_layout.addWidget(search_input, 1)
        search_layout.addWidget(search_btn)
        
        layout.addWidget(self.tabs)
        layout.addLayout(search_layout)
        
        self.setLayout(layout)
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout)
from components.player_control import PlayerControl
from components.search_bar import SearchBar
from components.side_panel import SidePanel
from PySide6.QtWidgets import QStackedWidget
from components.youtube_panel import YouTubePanel

class SpotifyInterface(QMainWindow):
    """Janela principal"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Player")
        self.setGeometry(100, 100, 1000, 600)
        
        # Estilo global
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
        """)
        
        # Widget central
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        


        # Painel lateral (30%)
        self.stacked_panel = QStackedWidget()
        self.library_panel = SidePanel()
        self.youtube_panel = YouTubePanel()
        #config painel
        self.stacked_panel.setFixedWidth(300)
        self.stacked_panel.addWidget(self.library_panel)
        self.stacked_panel.addWidget(self.youtube_panel)
        

        # Painel direito
        right_panel = QWidget()
        right_panel.setStyleSheet("background-color: #121212;")
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 20, 20, 20)
        right_layout.setSpacing(0)
        
        # Barra de pesquisa
        self.search_bar = SearchBar()

        # Player
        self.player = PlayerControl()
        
        right_layout.addWidget(self.search_bar)
        right_layout.addWidget(self.player, 1)
        right_panel.setLayout(right_layout)
        
        # Adicionar ao layout principal
        main_layout.addWidget(self.stacked_panel)
        main_layout.addWidget(right_panel, 1)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)




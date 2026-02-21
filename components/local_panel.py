from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                               QScrollArea, QStackedWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
import qtawesome as qta


class SidePanel(QWidget):
    """Painel lateral com lista de músicas"""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #000000;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ── Barra de abas ──────────────────────────────────────────────────────
        tabs_container = QWidget()
        tabs_container.setStyleSheet("background-color: #000000; border-bottom: 1px solid #282828;")
        tabs_layout = QHBoxLayout(tabs_container)
        tabs_layout.setContentsMargins(8, 8, 8, 0)
        tabs_layout.setSpacing(4)

        self.btn_tab_playlists = QPushButton("  Playlists")
        self.btn_tab_playlists.setIcon(qta.icon('fa5s.list', color="#ffffff"))
        self.btn_tab_playlists.setIconSize(QSize(13, 13))
        self.btn_tab_playlists.setFont(QFont("Segoe UI", 9, QFont.Bold))
        self.btn_tab_playlists.setCursor(Qt.PointingHandCursor)
        self.btn_tab_playlists.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #1a1a1a;
                border: none;
                border-bottom: 2px solid #1DB954;
                border-radius: 0px;
                padding: 8px 14px;
            }
            QPushButton:hover { background-color: #1a1a1a; }
        """)

        self.btn_tab_songs = QPushButton("  Músicas")
        self.btn_tab_songs.setIcon(qta.icon('fa5s.music', color="#b3b3b3"))
        self.btn_tab_songs.setIconSize(QSize(13, 13))
        self.btn_tab_songs.setFont(QFont("Segoe UI", 9, QFont.Bold))
        self.btn_tab_songs.setCursor(Qt.PointingHandCursor)
        self.btn_tab_songs.setStyleSheet("""
            QPushButton {
                color: #b3b3b3;
                background-color: transparent;
                border: none;
                border-bottom: 2px solid transparent;
                border-radius: 0px;
                padding: 8px 14px;
            }
            QPushButton:hover { color: #ffffff; background-color: #1a1a1a; }
        """)

        tabs_layout.addWidget(self.btn_tab_playlists)
        tabs_layout.addWidget(self.btn_tab_songs)
        tabs_layout.addStretch()

        # ── Stack de conteúdo ──────────────────────────────────────────────────
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #000000;")

        # Página 0 – Playlists
        playlists_page = QWidget()
        pl_layout = QVBoxLayout(playlists_page)
        pl_layout.setContentsMargins(0, 0, 0, 0)

        pl_scroll = QScrollArea()
        pl_scroll.setWidgetResizable(True)
        pl_scroll.setStyleSheet("""
            QScrollArea { border: none; background-color: #000000; }
            QScrollBar:vertical { background-color: #000000; width: 12px; border-radius: 6px; }
            QScrollBar::handle:vertical { background-color: #404040; border-radius: 6px; min-height: 30px; }
            QScrollBar::handle:vertical:hover { background-color: #535353; }
        """)

        self.playlist_container = QWidget()
        self.playlist_layout = QVBoxLayout(self.playlist_container)
        self.playlist_layout.setContentsMargins(8, 8, 8, 8)
        self.playlist_layout.setAlignment(Qt.AlignTop)
        pl_scroll.setWidget(self.playlist_container)
        pl_layout.addWidget(pl_scroll)

        # Página 1 – Músicas
        songs_page = QWidget()
        songs_layout = QVBoxLayout(songs_page)
        songs_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("""
            QScrollArea { border: none; background-color: #000000; }
            QScrollBar:vertical { background-color: #000000; width: 12px; border-radius: 6px; }
            QScrollBar::handle:vertical { background-color: #404040; border-radius: 6px; min-height: 30px; }
            QScrollBar::handle:vertical:hover { background-color: #535353; }
        """)

        self.music_container = QWidget()
        self.music_layout = QVBoxLayout(self.music_container)
        self.music_layout.setContentsMargins(8, 8, 8, 8)
        self.music_layout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.music_container)
        songs_layout.addWidget(self.scroll)

        self.stack.addWidget(playlists_page)  # índice 0
        self.stack.addWidget(songs_page)       # índice 1

        # ── Rodapé – músicas locais ────────────────────────────────────────────
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

        self.path_label = QLabel("Nenhuma pasta selecionada")
        self.path_label.setFont(QFont("Segoe UI", 9))
        self.path_label.setStyleSheet("QLabel { color: #b3b3b3; background-color: transparent; padding: 4px; }")
        self.path_label.setWordWrap(True)

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
            QPushButton:hover { background-color: #1ed760; }
            QPushButton:pressed { background-color: #169c46; }
        """)

        local_layout.addWidget(self.button_local)
        local_layout.addWidget(self.path_label)

        # ── Montagem final ─────────────────────────────────────────────────────
        layout.addWidget(tabs_container)
        layout.addWidget(self.stack)
        layout.addWidget(local_music_container)
        self.setLayout(layout)
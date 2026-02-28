from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QScrollArea, QWidget, QFrame,
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
import qtawesome as qta


class NewPlaylistDialog(QDialog):
    """Dialog de criação de playlist — apenas interface."""

    def __init__(self, available_songs: list[str] | None = None, parent=None):
        super().__init__(parent)
        self.available_songs = available_songs or []

        self.setWindowTitle("Nova Playlist")
        self.setModal(True)
        self.setFixedSize(500, 620)
        self.setStyleSheet("QDialog { background-color: #121212; }")

        self._build_ui()

    # ─────────────────────────────────────────────────────────────────────────
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._make_header())
        root.addWidget(self._make_body(), 1)
        root.addWidget(self._make_footer())

    # ── Header ────────────────────────────────────────────────────────────────
    def _make_header(self) -> QWidget:
        header = QWidget()
        header.setFixedHeight(54)
        header.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-bottom: 1px solid #282828;
            }
        """)
        layout = QHBoxLayout(header)
        layout.setContentsMargins(20, 0, 12, 0)

        title = QLabel("Nova Playlist")
        title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        title.setStyleSheet("color: #ffffff; background: transparent;")

        self.btn_close = QPushButton()
        self.btn_close.setIcon(qta.icon("fa5s.times", color="#b3b3b3"))
        self.btn_close.setIconSize(QSize(13, 13))
        self.btn_close.setFixedSize(30, 30)
        self.btn_close.setCursor(Qt.PointingHandCursor)
        self.btn_close.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                border-radius: 15px;
            }
            QPushButton:hover { background-color: #282828; }
        """)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(self.btn_close)
        return header

    # ── Body ──────────────────────────────────────────────────────────────────
    def _make_body(self) -> QWidget:
        body = QWidget()
        body.setStyleSheet("background-color: #121212;")
        layout = QVBoxLayout(body)
        layout.setContentsMargins(22, 18, 22, 0)
        layout.setSpacing(18)

        layout.addLayout(self._make_top_row())
        layout.addWidget(self._make_separator())
        layout.addLayout(self._make_songs_header())
        layout.addWidget(self._make_search())
        layout.addWidget(self._make_songs_list(), 1)

        return body

    def _make_top_row(self) -> QHBoxLayout:
        """Foto + campo de nome."""
        row = QHBoxLayout()
        row.setSpacing(18)

        # Botão de capa
        self.btn_cover = QPushButton()
        self.btn_cover.setFixedSize(100, 100)
        self.btn_cover.setCursor(Qt.PointingHandCursor)
        self.btn_cover.setIcon(qta.icon("fa5s.camera", color="#535353"))
        self.btn_cover.setIconSize(QSize(26, 26))
        self.btn_cover.setToolTip("Escolher foto de capa")
        self.btn_cover.setStyleSheet("""
            QPushButton {
                background-color: #282828;
                border: 2px dashed #404040;
                border-radius: 8px;
            }
            QPushButton:hover {
                border-color: #1DB954;
                background-color: #1a1a1a;
            }
        """)

        # Coluna nome
        col = QVBoxLayout()
        col.setSpacing(6)

        lbl = QLabel("Nome")
        lbl.setFont(QFont("Segoe UI", 8))
        lbl.setStyleSheet("color: #535353; background: transparent;")

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Ex: Chill vibes...")
        self.input_name.setFont(QFont("Segoe UI", 10))
        self.input_name.setFixedHeight(40)
        self.input_name.setStyleSheet("""
            QLineEdit {
                background-color: #282828;
                color: #ffffff;
                border: 1px solid #404040;
                border-radius: 8px;
                padding: 0 12px;
            }
            QLineEdit:focus {
                border-color: #1DB954;
                background-color: #1f1f1f;
            }
            QLineEdit::placeholder { color: #535353; }
        """)

        col.addWidget(lbl)
        col.addWidget(self.input_name)
        col.addStretch()

        row.addWidget(self.btn_cover)
        row.addLayout(col, 1)
        return row

    def _make_separator(self) -> QFrame:
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFixedHeight(1)
        sep.setStyleSheet("background-color: #282828; border: none;")
        return sep

    def _make_songs_header(self) -> QHBoxLayout:
        row = QHBoxLayout()

        lbl = QLabel("Músicas disponíveis")
        lbl.setFont(QFont("Segoe UI", 9, QFont.Bold))
        lbl.setStyleSheet("color: #ffffff; background: transparent;")

        self.lbl_count = QLabel("0 selecionadas")
        self.lbl_count.setFont(QFont("Segoe UI", 8))
        self.lbl_count.setStyleSheet("color: #1DB954; background: transparent;")

        row.addWidget(lbl)
        row.addStretch()
        row.addWidget(self.lbl_count)
        return row

    def _make_search(self) -> QLineEdit:
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText("Buscar...")
        self.input_search.setFont(QFont("Segoe UI", 9))
        self.input_search.setFixedHeight(34)
        self.input_search.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #282828;
                border-radius: 17px;
                padding: 0 14px;
            }
            QLineEdit:focus { border-color: #404040; }
            QLineEdit::placeholder { color: #404040; }
        """)
        return self.input_search

    def _make_songs_list(self) -> QScrollArea:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea { border: none; background-color: #121212; }
            QScrollBar:vertical {
                background: #121212; width: 8px; border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #333333; border-radius: 4px; min-height: 24px;
            }
            QScrollBar::handle:vertical:hover { background: #444444; }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical { height: 0; }
        """)

        self.songs_container = QWidget()
        self.songs_container.setStyleSheet("background: #121212;")
        self.songs_layout = QVBoxLayout(self.songs_container)
        self.songs_layout.setContentsMargins(0, 2, 0, 2)
        self.songs_layout.setSpacing(1)
        self.songs_layout.setAlignment(Qt.AlignTop)

        # Popula com as músicas recebidas
        if self.available_songs:
            for song in self.available_songs:
                self.songs_layout.addWidget(SongItem(song))
        else:
            empty = QLabel("Nenhuma música encontrada")
            empty.setAlignment(Qt.AlignCenter)
            empty.setFont(QFont("Segoe UI", 9))
            empty.setStyleSheet("color: #404040; padding: 28px;")
            self.songs_layout.addWidget(empty)

        scroll.setWidget(self.songs_container)
        return scroll

    # ── Footer ────────────────────────────────────────────────────────────────
    def _make_footer(self) -> QWidget:
        footer = QWidget()
        footer.setFixedHeight(68)
        footer.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-top: 1px solid #282828;
            }
        """)
        layout = QHBoxLayout(footer)
        layout.setContentsMargins(22, 0, 22, 0)
        layout.setSpacing(10)

        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setFont(QFont("Segoe UI", 9, QFont.Bold))
        self.btn_cancel.setFixedHeight(38)
        self.btn_cancel.setCursor(Qt.PointingHandCursor)
        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #b3b3b3;
                border: 1px solid #404040;
                border-radius: 19px;
                padding: 0 22px;
            }
            QPushButton:hover { color: #ffffff; border-color: #606060; }
        """)

        self.btn_create = QPushButton("  Criar Playlist")
        self.btn_create.setIcon(qta.icon("fa5s.check", color="#ffffff"))
        self.btn_create.setIconSize(QSize(12, 12))
        self.btn_create.setFont(QFont("Segoe UI", 9, QFont.Bold))
        self.btn_create.setFixedHeight(38)
        self.btn_create.setCursor(Qt.PointingHandCursor)
        self.btn_create.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: #ffffff;
                border: none;
                border-radius: 19px;
                padding: 0 24px;
            }
            QPushButton:hover   { background-color: #1ed760; }
            QPushButton:pressed { background-color: #169c46; }
        """)

        layout.addStretch()
        layout.addWidget(self.btn_cancel)
        layout.addWidget(self.btn_create)
        return footer
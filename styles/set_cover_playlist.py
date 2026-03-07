from PySide6.QtCore import Qt, QSize
import qtawesome as qta
from PySide6.QtGui import QPixmap, QIcon

def set_default_cover(btn_cover):
    btn_cover.setFixedSize(100, 100)
    btn_cover.setCursor(Qt.PointingHandCursor)
    btn_cover.setIcon(qta.icon("fa5s.camera", color="#535353"))
    btn_cover.setIconSize(QSize(26, 26))
    btn_cover.setToolTip("Escolher foto de capa")
    btn_cover.setStyleSheet("""
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

def set_cover_photo(btn_cover, path):
    if not path:
        return
    btn = btn_cover
    pixmap = QPixmap(path)
    btn_w = btn.width()
    btn_h = btn.height()
    scaled = pixmap.scaled(
        btn_w,btn_h,
        Qt.KeepAspectRatioByExpanding,
        Qt.SmoothTransformation
    )
    x = (scaled.width() - btn_w) // 2
    y = (scaled.height() - btn_h) // 2
    cropped = scaled.copy(x, y, btn_w, btn_h)
    btn.setIcon(QIcon(cropped))
    btn.setIconSize(btn.size())
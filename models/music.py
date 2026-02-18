from dataclasses import dataclass
from pathlib import Path
from PySide6.QtGui import QPixmap

@dataclass
class Music:
    position: int | None
    title: str
    artist: str
    duration: str
    path: Path
    icon: QPixmap = None


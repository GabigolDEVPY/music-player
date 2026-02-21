from dataclasses import dataclass
from models.music import Music
from PySide6.QtGui import QPixmap

@dataclass
class Playlist:
    title: str
    description: str
    music_count: str
    playlist_id: str
    # musics: list[Music]


    
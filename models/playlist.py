from dataclasses import dataclass
from models.music import Music

@dataclass
class Playlist:
    name: str
    musics: list[Music]
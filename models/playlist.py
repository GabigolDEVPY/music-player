from dataclasses import dataclass

@dataclass
class Playlist:
    title: str
    description: str
    music_count: str
    playlist_id: str
    # musics: list[Music]


    
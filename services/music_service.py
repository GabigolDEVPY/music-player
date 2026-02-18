from PySide6.QtCore import  QSize
from PySide6.QtGui import  QPixmap
import qtawesome as qta
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from pathlib import Path
from models.music import Music

class MusicService:
    @staticmethod
    def load_folder_musics(path):
        musics = []
        for file in Path(path).glob("*.mp3"):
            audio = MP3(path / file)
            tags = EasyID3(path / file)
            id3 = ID3(path / file)

            length = int(audio.info.length)
            duration = f"{length // 60:02}:{length % 60:02}"

            cover_data = None
            for tag in id3.values():
                if isinstance(tag, APIC):
                    cover_data = tag.data
                    break

            pixmap = qta.icon('fa5s.music', color='white').pixmap(QSize(18, 18))

            if cover_data:
                pixmap = QPixmap()
                pixmap.loadFromData(cover_data)    

            music = Music(
                position=None,
                title=tags.get("title", ["Sem titulo"])[0],
                artist=tags.get("artist", ["Desconhecido"])[0],
                duration=duration,
                path=path / file,
                icon=pixmap
                )
            musics.append(music)
        return musics


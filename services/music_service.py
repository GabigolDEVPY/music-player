from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QScrollArea, 
                               QLineEdit, QSlider, QFrame, QTabWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
import qtawesome as qta
from mutagen.mp3 import MP3
import json
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import sys
import os
from PySide6.QtWidgets import QStackedWidget
from pathlib import Path

class MusicService:
    @staticmethod
    def get_local_musics(path):
        path = Path(path)
        musics = []
        for file in os.listdir(path):
            if file.lower().endswith(".mp3"):
                audio = MP3(path / file)
                tags = EasyID3(path / file)
                id3 = ID3(path / file)
                cover_data = None
                length = int(audio.info.length)
                minutes = length // 60
                seconds = length % 60

                for tag in id3.values():
                    if tag.FrameID == "APIC":
                        cover_data = tag.data
                        break

                pixmap = qta.icon('fa5s.music', color='white').pixmap(QSize(18, 18))
                if cover_data:
                    pixmap = QPixmap()
                    pixmap.loadFromData(cover_data)    

                music_data = {
                    "title": tags.get("title", ["Sem titulo"])[0],
                    "artist": tags.get("artist", ["Desconhecido"])[0],
                    "duration": f"{minutes:02}:{seconds:02}",
                    "path": path / file,
                    "icon": pixmap
                }
                musics.append(music_data)
        return musics

    def load_path_musics():
        try:
            path = Path(__file__).parent / "save.json"
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            return None
        
    def save_path_musics(file):
        path = Path(__file__).parent / "save.json"
        with open(path, "w", encoding="utf-8") as f:
            return json.dump(file, f, indent=4)

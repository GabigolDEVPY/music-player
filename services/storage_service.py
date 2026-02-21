import json
from pathlib import Path

class StorageService:
    @staticmethod
    def get_config_path():
        folder = Path.home() / "Documentos"
        print(folder)

        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
            print(folder)
        return folder / "save.json"

    @staticmethod
    def load_path_musics():
        path = StorageService.get_config_path()
        if not path.exists():
            return None

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)


    @staticmethod
    def save_path_musics(data):
        path = StorageService.get_config_path()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

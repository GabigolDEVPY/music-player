import json
from pathlib import Path
import platform

platform_system = platform.system()

class StorageService:
    @staticmethod
    def get_config_path():
        if platform_system == "Windows":
            folder = Path.home() / "Documents"
            print("caminhooooo",folder)
        else:
            folder = Path.home() / "Documentos"
            print("caminhooooo",folder)

        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
        return folder / "save.json"

    @staticmethod
    def load_json():
        path = StorageService.get_config_path()
        if not path.exists():
            print("entrou no inexistente")
            return {"path": ""}

        with open(path, "r", encoding="utf-8") as f:
            print("retornando json")
            return json.load(f)
        



    @staticmethod
    def save_json(data):
        path = StorageService.get_config_path()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

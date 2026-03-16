from models.playlist import Playlist
from services.storage_service import StorageService
from random import randint

class PlaylistService:
    def __init__(self, cache_data):
        self.cache_data = cache_data
        self.new_playlist_info = {"cover_path": None}
        
    def get_playlists():
        playlists = []
        playlists_dicts = [{    
        "title": "Melhor playlist",
        "description": "aqui a musica nunca acaba",
        "music_count": "14",
        "playlist_id": "1",
        "cover_path": "nada aqui"
        }]

        for playlist in playlists_dicts:
            playlist = Playlist(
                title=playlist["title"],
                description=playlist["description"],
                music_count=playlist["music_count"],
                playlist_id=playlist["playlist_id"],
                cover_path=playlist["cover_path"],
            )
            playlists.append(playlist)
        return playlists
    
    def get_musics(self):
        musics = self.cache_data.get_music_list()
        return musics
    
    def select_cover_photo(self, path):
        self.new_playlist_info["cover_path"] = path
    
    def create_playlist(self, name, description, musics_selected):
        # classe
        playlist = {    
        "title": name,
        "description": description,
        "music_count": len(musics_selected),
        "playlist_id": randint(10000000, 99999999),
        "cover_path": self.new_playlist_info["cover_path"]
        }
        self.save_playlist_storage(playlist)

    def save_playlist_storage(self, playlist):
        json = StorageService.load_path_musics()
        json["playlists"] = []
        json["playlists"].append(playlist)
        StorageService.save_path_musics(json)
        pass
from models.playlist import Playlist
from models.music import Music

class PlaylistService:
    @staticmethod
    def get_playlists():
        playlists = []
        playlists_dicts = [{    
        "title": "Melhor playlist",
        "description": "aqui a musica nunca acaba",
        "music_count": "14",
        "playlist_id": "1",
        }]

        for playlist in playlists_dicts:
            playlist = Playlist(
                title=playlist["title"],
                description=playlist["description"],
                music_count=playlist["music_count"],
                playlist_id=playlist["playlist_id"],
            )
            playlists.append(playlist)
        return playlists
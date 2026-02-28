from models.playlist import Playlist

class PlaylistService:
    def __init__(self, cache_data):
        self.cache_data = cache_data
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
    
    def get_musics(self):
        musics = self.cache_data.get_music_list()
        return musics
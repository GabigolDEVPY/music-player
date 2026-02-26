from components.interface import SpotifyInterface
from controllers.Panel_controller import PanelController
from controllers.Player_controller import PlayerController
from controllers.Library_controller import LibraryController
from controllers.Playlist_controller import Playlist
from models.cache_data import CacheData


class MainController():
    def __init__(self):
        super().__init__()
        self.view = SpotifyInterface()
        
        #cache data
        self.cache_data = CacheData()

        # player controller with signals 
        self.player_controller = PlayerController(
            self.view.player,
            self.cache_data
        )

        # playlist controller 
        self.playlist_controller = Playlist(
            self.cache_data,
            self.view.library_panel,
            self.view.playlist_dialog_create
            )

        # library controller / passando player no final
        self.library_controller = LibraryController(
            self.view.library_panel, 
            self.view.youtube_panel, 
            self.player_controller,
            self.cache_data
            )


        # panel controller
        self.panel_controller = PanelController(
            self.view.search_bar,
            self.view.stacked_panel,
            self.library_controller
            )
        
        #select card by  
        self.player_controller.music_changed.connect(
        self.library_controller.select_card_by_position
        )
        
        
        self.cache_data.reload_data.connect(self.call_functions_reload_data)
    

        self.cache_data.reload_data.emit(self.cache_data.get_local_path())
        

    def call_functions_reload_data(self):
        self.library_controller.load_musics(self.cache_data.get_music_list())
        self.player_controller.set_playlist(self.cache_data.get_music_list())
        self.playlist_controller.populate_panel_playlists(self.cache_data.get_playlists())

    def run(self):
        self.view.show()

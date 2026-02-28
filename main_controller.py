from components.interface import SpotifyInterface
from controllers.Panel_controller import PanelController
from controllers.Player_controller import PlayerController
from controllers.Library_controller import LibraryController
from controllers.Playlist_controller import PlaylistController
from services.playlist_service import PlaylistService
from services.library_service import LibraryService
from models.cache_data import CacheData


class MainController():
    def __init__(self):
        super().__init__()
        self.view = SpotifyInterface()
        
        #cache data
        self.cache_data = CacheData()

        #services
        self.playlist_service = PlaylistService(self.cache_data)
        self.library_service = LibraryService(self.cache_data)
        
        # player controller with signals 
        self.player_controller = PlayerController(
            self.view.player,
            self.cache_data
        )

        # playlist controller 
        self.playlist_controller = PlaylistController(
            self.view.library_panel,
            self.view.playlist_dialog_create,
            self.playlist_service
            )

        # library controller / passando player no final
        self.library_controller = LibraryController(
            self.view.library_panel, 
            self.player_controller,
            self.library_service
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
        
        #reload data
        self.cache_data.reload_data.connect(self.call_functions_reload_data)
    
        #reload data emit
        self.cache_data.init_data()
        

    def call_functions_reload_data(self, path):
        self.library_controller.populate_musics_panel()
        self.library_controller.set_label_path_text()
        self.player_controller.set_playlist(self.cache_data.get_music_list())
        self.playlist_controller.populate_panel_playlists(self.cache_data.get_playlists())

    def run(self):
        self.view.show()

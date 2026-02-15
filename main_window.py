from components.interface import SpotifyInterface
from controllers.Panel_controller import PanelController
from controllers.Player_controller import PlayerController
from controllers.Library_controller import LibraryController

from pathlib import Path
from PySide6.QtCore import QUrl


ROOT_DIR = Path(__file__).parent

class MainController(SpotifyInterface):
    def __init__(self):
        super().__init__()

        # player control
        self.player_control = PlayerController(self.player)
        # change status player/pause button
        self.player.play_btn.clicked.connect(self.player_control.change_status_play)
        #change status player/music end time
        self.player.music_player.mediaStatusChanged.connect(self.player_control.next_music)
        #change next music
        self.player.next_btn.clicked.connect(self.player_control.next_music_btn)
        #change previous music
        self.player.prev_btn.clicked.connect(self.player_control.previous_music_btn)
        # change random mode
        self.player.shuffle_btn.clicked.connect(self.player_control.random_order)
        #change repeat mode
        self.player.repeat_btn.clicked.connect(self.player_control.repeat_order)
        

        # library controller
        self.library_controller = LibraryController(self.library_panel, self.youtube_panel, self.player_control)


        # panel controller
        self.panel_controller = PanelController(self.stacked_panel, self.library_controller)
        self.panel_controller.change_panel(0)
        
        #Change pannel music youtube/local 
        self.search_bar.tabs.currentChanged.connect(self.panel_controller.change_panel)

        # select folder path
        self.library_panel.button_local.clicked.connect(self.library_controller.change_local_path)



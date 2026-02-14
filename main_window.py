from components.interface import SpotifyInterface
from controllers.Panel_controller import PanelController
from controllers.PlayerController import PlayerController
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


        # panel controller
        self.panel_controller = PanelController(self.stacked_panel, self.youtube_panel, self.library_panel, self.player_control)
        self.panel_controller.change_panel(0)
        #Change pannel music youtube/local 
        self.search_bar.tabs.currentChanged.connect(self.panel_controller.change_panel)




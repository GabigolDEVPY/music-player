from components.interface import SpotifyInterface
from controllers.Panel_controller import PanelController
from controllers.Player_controller import PlayerController
from controllers.Library_controller import LibraryController
from PySide6.QtCore import QUrl


class MainController():
    def __init__(self):
        super().__init__()
        self.view = SpotifyInterface()
        
        # player controller with signals 
        self.player_control = PlayerController(
            self.view.player,
            self.view.library_panel
        )

        # library controller / passando player no final
        self.library_controller = LibraryController(
            self.view.library_panel, 
            self.view.youtube_panel, 
            self.player_control
            )


        # panel controller
        self.panel_controller = PanelController(
            self.view.search_bar,
            self.view.stacked_panel,
            self.library_controller
            )
        
        
    def run(self):
        self.view.show()



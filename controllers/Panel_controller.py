from styles.set_active_tab import set_active_tab


class PanelController:
    def __init__(self,search_bar, stacked_panel, library_controller):
        self.search_bar = search_bar
        self.stacked_panel = stacked_panel
        self.library_controller = library_controller
        self.change_panel(0)
        self._connect_signals()
    
    def _connect_signals(self):
        self.search_bar.tabs.currentChanged.connect(self.change_panel)
        self.stacked_panel.currentWidget().btn_tab_songs.clicked.connect(self.change_musics_panel)
        self.stacked_panel.currentWidget().btn_tab_playlists.clicked.connect(self.change_playlist_panel)

    def change_panel(self, index):
        self.stacked_panel.setCurrentIndex(index)

        
    def change_playlist_panel(self):
        self.stacked_panel.currentWidget().stack.setCurrentIndex(0)
        set_active_tab(self, "playlists")
        
        
    def change_musics_panel(self):
        self.stacked_panel.currentWidget().stack.setCurrentIndex(1)
        set_active_tab(self, "songs")


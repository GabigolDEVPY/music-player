class PanelController:
    def __init__(self,search_bar, stacked_panel, library_controller):
        self.search_bar = search_bar
        self.stacked_panel = stacked_panel
        self.library_controller = library_controller
        self.change_panel(0)
        self._connect_signals()
    
    def _connect_signals(self):
        self.search_bar.tabs.currentChanged.connect(self.change_panel)

    def change_panel(self, index):
        self.stacked_panel.setCurrentIndex(index)
        if index == 0:
            self.library_controller.load_musics()


        elif index == 1:
            pass



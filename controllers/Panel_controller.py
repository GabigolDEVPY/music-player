class PanelController:
    def __init__(self, stacked_panel, library_controller):
        self.stacked_panel = stacked_panel
        self.library_controller = library_controller


    def change_panel(self, index):
        self.stacked_panel.setCurrentIndex(index)
        if index == 0:
            self.library_controller.load_musics()


        elif index == 1:
            pass



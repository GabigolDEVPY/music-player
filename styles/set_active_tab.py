
def set_active_tab(self, active):
    panel = self.stacked_panel.currentWidget()

    active_style = """
        QPushButton {
            color: #ffffff;
            background-color: #1a1a1a;
            border: none;
            border-bottom: 2px solid #1DB954;
            border-radius: 0px;
            padding: 8px 14px;
        }
        QPushButton:hover { background-color: #1a1a1a; }
    """
    inactive_style = """
        QPushButton {
            color: #b3b3b3;
            background-color: transparent;
            border: none;
            border-bottom: 2px solid transparent;
            border-radius: 0px;
            padding: 8px 14px;
        }
        QPushButton:hover { color: #ffffff; background-color: #1a1a1a; }
    """

    if active == "playlists":
        panel.btn_tab_playlists.setStyleSheet(active_style)
        panel.btn_tab_songs.setStyleSheet(inactive_style)
    else:
        panel.btn_tab_songs.setStyleSheet(active_style)
        panel.btn_tab_playlists.setStyleSheet(inactive_style)
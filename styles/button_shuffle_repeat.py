def update_style(self, button, active=None):
    self.button = button
    if active is True:
        colors = [ "#1bba53", "#4ee783"]
    else:
        colors = [ "#1a1a1a", "#282828"]
        
    btn_style = f"""
        QPushButton {{
            background-color: {colors[0]};
            color: white;
            border: none;
            border-radius: 20px;
        }}
        QPushButton:hover {{
            background-color: {colors[1]};
        }}
    """
    self.button.setStyleSheet(btn_style)
from utils.constants import LIGHT_COLORS, DARK_COLORS

class ThemeManager:
    def __init__(self):
        self.is_dark_mode = False
        self.colors = LIGHT_COLORS
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.colors = DARK_COLORS if self.is_dark_mode else LIGHT_COLORS
        return self.colors
    
    def get_colors(self):
        return self.colors
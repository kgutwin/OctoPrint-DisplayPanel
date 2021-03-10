
from . import base


class SoftButtonsScreen(base.MicroPanelScreenScroll):
    def __init__(self, width, height, _printer, _settings):
        menu = [
            'Auto Home',
            'Bed Leveling',
            'Filament Load',
            'Filament Unload',
            'Cooldown'
        ]
        super().__init__(width, height, 'Soft Buttons', menu)
        

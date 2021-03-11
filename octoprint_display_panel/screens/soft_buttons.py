
from . import base


class SoftButtonsScreen(base.MicroPanelScreenScroll):
    def __init__(self, width, height, _printer, _settings):
        menu = [
            'Auto Home',
            'Bed Leveling',
            'Filament Unload',
            'Filament Load',
            'Cooldown'
        ]
        super().__init__(width, height, 'Soft Buttons', menu)
        self._printer = _printer
        self._settings = _settings
        
    def handle_menu_item(self, menu_item):
        if menu_item == 'Auto Home':
            self._printer.commands('G28')
        elif menu_item == 'Bed Leveling':
            self._printer.commands([
                'M140 S50', 'G28', 'M190',
                'G0 X30 Y30 Z1', 'G0 Z0', 'M0 Point 1',
                'G0 X30 Y200 Z1', 'G0 Z0', 'M0 Point 2',
                'G0 X200 Y200 Z1', 'G0 Z0', 'M0 Point 3',
                'G0 X200 Y30 Z1', 'G0 Z0', 'M0 Point 4',
                'G28'
            ])
        elif menu_item == 'Filament Load':
            self._printer.commands('M701 L10')
        elif menu_item == 'Filament Unload':
            self._printer.commands('M702 U10')
        elif menu_item == 'Cooldown':
            self._printer.commands(['M104 S0', 'M140 S0'])

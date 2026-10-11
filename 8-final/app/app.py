
from config.config import AppSettings
from screens.main import MainScreen
from textual.app import App


class MonitoringApp(App):
    """App"""

    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = settings

    def on_mount(self) -> None:
        """Main Screen"""
        main_screen = MainScreen()
        self.push_screen(main_screen)

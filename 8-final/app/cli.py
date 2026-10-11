"""CLI Module"""

import sys
from pathlib import Path

from config.config import AppSettings

from app.app import MonitoringApp


def create_app(data_path: Path | None = None):
    settings: AppSettings
    if data_path:
        settings = AppSettings.from_custom_path(data_path)
    else:
        settings = AppSettings.from_defaults()

    # Start App
    return MonitoringApp(settings)


def monitoring():
    data_path = None
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])

    app = create_app(data_path)
    app.run()


from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppSettings:
    data_directory: Path
    app_name: str = "Monitoring App"
    app_version: str = "0.1.0"

    @classmethod
    def from_defaults(cls) -> AppSettings:  # noqa: F821
        base_path = Path(__file__).parent.parent.parent
        data_path = base_path / "data"
        return cls(data_directory=data_path)

    @classmethod
    def from_custom_path(cls, data_path: str | Path) -> AppSettings:  # noqa: F821
        return cls(data_directory=Path(data_path))

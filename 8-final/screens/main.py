from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Button, DataTable, Footer, Header, Input

ROWS = [
    ("URL", "Interval(s)", "Status", "HTTP", "Last Checked"),
    ("https://purpleschool.ru", "10", "OK", "200", "10:43:09")
]


class MainScreen(Screen):
    CSS = """
    #input-container {
        width: 100%;
        height: auto;
        padding: 0 5;
        layout: horizontal;
    }

    #url-input {
        width: 1fr;
    }

    #interval-input {
        width: 20;
    }

    #add-button {
        width: 12;
    }
    
    #monitoring-table {
        margin-top: 20;
    }
    """

    BINDINGS = [("q", "quit", "Exit")]  # noqa: RUF012

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="input-container"):
            yield Input(
                placeholder="https://example.com",
                type="text",
                id="url-input",
            )

            yield Input(
                placeholder="Interval",
                type="integer",
                id="interval-input",
            )

            yield Button(
                label="Add",
                variant="success",
                id="add-button",
            )

        yield DataTable(id="monitoring-table")

        yield Footer()

    def on_mount(self):
        self.title = "MonitorApp"
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_row(*ROWS[1])

    def action_quit(self):
        self.app.exit()

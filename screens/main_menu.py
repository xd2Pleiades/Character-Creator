#main_menu
"""
Main Menu UIX

"""
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label
from textual.containers import Vertical

class MainMenu(Screen):
    CSS = """
    Screen {
        align: center middle;
        }
    #menu {
        width: 40;
        height: auto;
        border: wide white;
        padding: 1 2;
        }
    Button {
        width: 100%;
        margin-top: 1;
        }
    """

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="menu"):
            yield Label("Welcome to DropperDeader:7777", id="welcome")
            yield Button("Play", id="play")
            yield Button("Quit", id="quit")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.app.theme = (
            "textual-dark" if self.app.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # This fires whenever ANY button is pressed
        if event.button.id == "play":
            self.notify("Those who moved forward with the stars... Seek a new hell.")
        elif event.button.id == "quit":
            self.notify("He had sought the abyss.")
            self.app.exit()
        return

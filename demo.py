#!/usr/bin/env python3
"""

lorem ipsum

"""

from textual.app import App
from textual.widgets import Header, Placeholder, Footer
from textual.widget import Widget
from textual.widgets._button import ButtonRenderable

from rich.panel import Panel
from rich.style import Style


class Tile(ButtonRenderable):

    def __init__(self, letter=' '):
        super().__init__()
        self.letter = letter

    def render(self):
        return Panel(self.letter, expand=False)


class Pyrdle(App):
    """lorem ipsum"""

    async def on_load(self, event):
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("q", "quit", "Quit")

    async def on_mount(self):
        """Mount the widget."""
        header_style = Style(color="#F5C2E7", bgcolor="#1c1c1c")
        await self.view.dock(Header(style=header_style), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        board = await self.view.dock_grid(edge="left", name="board")

        board.add_column(name="a")
        board.add_row(name="b", max_size=3)

        board.add_areas(areas="a,b")

        board.place(areas=Tile('A'))


Pyrdle.run(title="Pyrdle", log="pyrdle.log")

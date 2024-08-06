from typing import override

import pyglet

from guui.widget import Widget


class Label(Widget):
    """A widget that displays text."""

    def __init__(self, text: str, x: int = 0, y: int = 0, font_size: int = 12) -> None:
        """Initialize this label.

        Args:
            text: The text to display.
            x: The horizontal position of this label in pixels. Defaults to ``0``.
            y: The vertical position of this label in pixels. Defaults to ``0``.
            font_size: The size of the font in pixels. Defaults to ``12``.
        """

        self._label = pyglet.text.Label(text, x, y, font_size=font_size)

        super().__init__(x, y, self._label.content_width, self._label.content_height)

    @override
    def draw(self) -> None:
        self._label.x = self.x
        self._label.y = self.y
        self._label.draw()

    @property
    def text(self) -> str:
        """The text of this label."""
        return self._label.text

    @text.setter
    def text(self, new_text: str) -> None:
        self._label.text = new_text

        self.width = self._label.content_width
        self.height = self._label.content_height

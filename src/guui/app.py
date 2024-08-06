from typing import override

import pyglet

from guui._bounds import is_in_rectangle
from guui.widget import Widget


class App(pyglet.window.Window):
    """A Guui app."""

    def __init__(self, caption: str) -> None:
        """Initialize the app.

        After doing this, you should set a root widget at :attr:`App.root_widget`.

        Args:
            caption: The window caption/"title".
        """

        super().__init__(visible=False)  # pyright: ignore[reportUnknownMemberType]
        self.set_caption(caption)

        self._root_widget: Widget | None = None

    @override
    def on_draw(self) -> None:
        if self._root_widget is not None:
            self._root_widget.draw()

    @override
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self._root_widget is None:
            return

        if clicked_widget := self._widget_at(x, y):
            clicked_widget.click()

    def _widget_at(self, x: int, y: int, root: Widget | None = None) -> Widget | None:
        """Find a widget at the given position.

        Args:
            x: The horizontal position in pixels.
            y: The vertical position in pixels.
            root: The widget to start at. Defaults to this app's root widget.

        Returns:
            A widget at the given position, or None if none were found.
        """

        if self._root_widget is None:
            return None

        if root is None:
            root = self._root_widget

        if not is_in_rectangle(x, y, root.x, root.y, root.width, root.height):
            return None

        for child in reversed(root.children):
            result = self._widget_at(x, y, child)
            if result:
                return result

        return root

    def start(self) -> None:
        """Start this app."""

        self.set_visible(True)
        pyglet.app.run()

    @property
    def root_widget(self) -> Widget | None:
        """The widget to draw."""
        return self._root_widget

    @root_widget.setter
    def root_widget(self, new_root_widget: Widget) -> None:
        self._root_widget = new_root_widget

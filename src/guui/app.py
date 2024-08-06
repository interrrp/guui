from typing import override

import pyglet

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

import pyglet


class App:
    """A Guui app.

    Attributes:
        window: The Pyglet window.
    """

    def __init__(self, caption: str) -> None:
        """Initialize the app.

        Args:
            caption: The window caption/"title".
        """

        self.window = pyglet.window.Window(visible=False)
        self.window.set_caption(caption)

    def start(self) -> None:
        """Start the app."""

        self.window.set_visible(True)

        pyglet.app.run()

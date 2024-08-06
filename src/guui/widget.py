class Widget:
    """An interactable widget.

    Attributes:
        x: The horizontal position of this widget in pixels.
        y: The vertical position of this widget in pixels.
        width: The horizontal size of this widget in pixels.
        height: The vertical size of this widget in pixels.
    """

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """Initialize this widget.

        Args:
            x: The horizontal position of this widget in pixels.
            y: The vertical position of this widget in pixels.
            width: The horizontal size of this widget in pixels.
            height: The vertical size of this widget in pixels.
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self) -> None:
        """Draw this widget."""

from __future__ import annotations


class Widget:
    """An interactable widget.

    Attributes:
        x: The horizontal position of this widget in pixels.
        y: The vertical position of this widget in pixels.
        width: The horizontal size of this widget in pixels.
        height: The vertical size of this widget in pixels.
        children: The children of this widget.
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

        self.children: list[Widget] = []

    def add_child(self, widget: Widget) -> None:
        """Add a child widget to this widget.

        Args:
            widget: The widget to add.
        """
        self.children.append(widget)

    def draw(self) -> None:
        """Draw this widget."""

    def click(self) -> None:
        """Click this widget."""

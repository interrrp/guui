from typing import Literal, override

from guui.widget import Widget

type Orientation = Literal["horizontal", "vertical"]


class StackLayout(Widget):
    """A layout that stacks widgets horizontally or vertically."""

    def __init__(self, orientation: Orientation, x: int, y: int, gap: int = 0) -> None:
        """Initialize this stack layout.

        Args:
            orientation: The orientation in which to stack widgets in.
            x: The starting horizontal position of this layout in pixels.
            y: The starting vertical position of this layout in pixels.
            gap: The space between each widget in pixels.
        """

        super().__init__(x, y, 0, 0)

        self._orientation: Orientation = orientation
        self._gap = gap

    @override
    def draw(self) -> None:
        for index, widget in enumerate(self.children):
            if self._orientation == "horizontal":
                widget.x = self.x + sum(widget.width for widget in self.children[:index]) + index * self._gap
                widget.y = self.y
            elif self._orientation == "vertical":
                widget.x = self.x
                widget.y = self.y + sum(widget.height for widget in self.children[:index]) + index * self._gap
            widget.draw()

    @override
    def add_child(self, widget: Widget) -> None:
        super().add_child(widget)
        self._update_size()

    def _update_size(self) -> None:
        """Update this widget's width and height properties."""

        if self._orientation == "horizontal":
            self.width = sum(widget.width for widget in self.children) + (len(self.children) - 1) * self._gap
            self.height = max(widget.height for widget in self.children)
        elif self._orientation == "vertical":
            self.width = max(widget.width for widget in self.children)
            self.height = sum(widget.height for widget in self.children) + (len(self.children) - 1) * self._gap

    @property
    def orientation(self) -> Orientation:
        """The orientation in which to stack widgets in."""
        return self._orientation

    @orientation.setter
    def orientation(self, new_orientation: Orientation) -> None:
        self._orientation = new_orientation
        self._update_size()

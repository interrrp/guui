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
        self._widgets: list[Widget] = []

    @override
    def draw(self) -> None:
        for index, widget in enumerate(self._widgets):
            if self._orientation == "horizontal":
                widget.x = self.x + sum(widget.width for widget in self._widgets[:index]) + index * self._gap
                widget.y = self.y
            elif self._orientation == "vertical":
                widget.x = self.x
                widget.y = self.y + sum(widget.height for widget in self._widgets[:index]) + index * self._gap
            widget.draw()

    def add(self, widget: Widget) -> None:
        """Add a widget to this stack layout.

        Args:
            widget: The widget to add.
        """

        self._widgets.append(widget)
        self._update_size()

    def _update_size(self) -> None:
        """Update this widget's width and height properties."""

        if self._orientation == "horizontal":
            self.width = sum(widget.width for widget in self._widgets) + (len(self._widgets) - 1) * self._gap
            self.height = max(widget.height for widget in self._widgets)
        elif self._orientation == "vertical":
            self.width = max(widget.width for widget in self._widgets)
            self.height = sum(widget.height for widget in self._widgets) + (len(self._widgets) - 1) * self._gap

    @property
    def orientation(self) -> Orientation:
        """The orientation in which to stack widgets in."""
        return self._orientation

    @orientation.setter
    def orientation(self, new_orientation: Orientation) -> None:
        self._orientation = new_orientation
        self._update_size()

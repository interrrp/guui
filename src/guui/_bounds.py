def is_in_rectangle(  # noqa: PLR0913
    x: int,
    y: int,
    rect_x: int,
    rect_y: int,
    rect_width: int,
    rect_height: int,
) -> bool:
    """Check if the given position is inside a rectangle.

    Args:
        x: The horizontal position in pixels.
        y: The vertical position in pixels.
        rect_x: The horizontal position of the rectangle in pixels.
        rect_y: The vertical position of the rectangle in pixels.
        rect_width: The horizontal size of the rectangle in pixels.
        rect_height: The vertical size of the rectangle in pixels.

    Returns:
        ``True`` if the given position fits inside the rectangle, ``False`` otherwise.
    """
    return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height

from guui.app import App


def test_constructor_sets_correct_window_caption() -> None:
    app = App("Test")
    assert app.window.caption == "Test"

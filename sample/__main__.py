from guui.app import App
from guui.label import Label

if __name__ == "__main__":
    app = App("Guui Sample")

    label = Label("Hello, world", 16, 16)
    app.root_widget = label

    app.start()

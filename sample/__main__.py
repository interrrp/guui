from guui import App, Label, StackLayout

if __name__ == "__main__":
    app = App("Guui Sample")

    layout = StackLayout("horizontal", x=0, y=0, gap=8)
    layout.add(Label("Label1"))
    layout.add(Label("Label2"))
    layout.add(Label("Label3"))

    app.root_widget = layout

    app.start()

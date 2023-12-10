from src.ui.window import Window


class Launcher:
    def __init__(self):
        self.window = Window()

    def launch(self):
        self.window.mainloop()

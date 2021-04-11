import kivy
from kivy.app import App
from kivy.uix.label import Label

class Naka(App):
    def build(self):
        return Label(text = "Class Rank: 67/116")


if __name__ == "__main__":
    Naka().run()
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.image import Image


class Form(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        self.source = 'assets/images/Lucina.jpg'

    def on_press(self):
        self.source = 'assets/images/Roxy.jpeg'

    def on_release(self):
        self.source = 'assets/images/Lucina.jpg'

class Naka(App):
    def build(self):

        return Form()



if __name__ == "__main__":
    Naka().run()
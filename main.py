from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty







# Set the application to automatically adapt to the phone screen size
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 732)
Config.set('graphics', 'resizable', False)

from kivy.uix.gridlayout import GridLayout

class DropdownMenu(GridLayout):
    def __init__(self, **kwargs):
        super(DropdownMenu, self).__init__(**kwargs)
        self.opacity = 0

    def toggle_visibility(self):
        if self.opacity == 0:
            self.opacity = 1
        else:
            self.opacity = 0



class FirstLayout(Screen):
    pass

class SecondLayout(Screen):
    selected_period = StringProperty("AM")
    selected_time = StringProperty("")

class ThirdLayout(Screen):
    """dropdown_open = BooleanProperty(False)

    def toggle_dropdown(self, button):
        if not self.dropdown_open:
            self.dropdown.open(button)
            self.dropdown_open = True
        else:
            self.dropdown.dismiss()
            self.dropdown_open = False"""
    
    def dropdown_dismissed(self, *args):
        self.dropdown_open = False


class MyApp(App):
    def build(self):
        Builder.load_file('layout1.kv')
        Builder.load_file('layout2.kv')
        Builder.load_file('layout3.kv')

        return Builder.load_file('main.kv')
        
if __name__ == '__main__':
    MyApp().run()

from tkinter import Tk
from tkinter.filedialog import askdirectory

from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from ConfigManager import ConfigManager


class MyToggleButton(ToggleButton):
    text_on = 'On'
    text_off = 'Off'

    def __init__(self, **kwargs):
        super(MyToggleButton, self).__init__(**kwargs)

        self.state = 'normal'
        self.text = self.text_off

    def on_release(self):
        state = self.state
        if state == 'normal':
            self.text = self.text_off
            self.enable()
        elif state == 'down':
            self.text = self.text_on
            self.disable()

    def enable(self):
        pass

    def disable(self):
        pass


class DotsButton(MyToggleButton):
    def enable(self):
        print('Enable')

    def disable(self):
        print('Dissable')


class BrowseButton(Button):
    mp3_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(BrowseButton, self).__init__(**kwargs)
        self.text = 'Browse'

    def on_release(self):
        Tk().withdraw()
        directory = askdirectory()
        self.mp3_label.text = directory
        # Save to config file
        ConfigManager.config().set('main', 'mp3_location', directory)
        save_button = self.parent.parent.save_button
        save_button.disabled = False

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from ConfigManager import ConfigManager


class SettingsEntries(BoxLayout):
    save_button = ObjectProperty(None)
    mp3_label = ObjectProperty(None)

    def update_label(self):
        self.mp3_label.text = ConfigManager.config().get('main', 'mp3_location')


from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

scroll_items = []
MAX_SIZE = 4


class ScrollItem(BoxLayout):
    # height = 50
    # label = Label()

    def __init__(self, text, **kwargs):
        super(ScrollItem, self).__init__(**kwargs)
        self.padding = 2
        self.height = 30
        self.size_hint_y = None
        # Add label
        self.label = Label()
        self.label.text = text
        self.label.size_hint = (0.8, 1)
        self.add_widget(self.label)
        # Add progress bar
        self.progressbar = ProgressBar()
        self.progressbar.value = 0
        self.progressbar.size_hint = (0.2, 1)
        self.add_widget(self.progressbar)

        Clock.schedule_interval(self.update, 1 / 20.)
        print(len(scroll_items))

    def update(self, *args):
        if self.progressbar.value == 100:
            pass
        if self in scroll_items:
            self.progressbar.value += 1
            if self.progressbar.value >= 100:
                scroll_items.remove(self)
        else:
            if len(scroll_items) < MAX_SIZE:
                scroll_items.append(self)

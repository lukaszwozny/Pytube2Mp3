from kivy.uix.togglebutton import ToggleButton


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

import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from conversion import Converter


def main():
    url = 'https://www.youtube.com/watch?v=DebhiaQH3ps'
    vid_path = Converter.download_yt_video(url=url)
    Converter.convert_video_to_mp3(vid_path)
    os.remove(vid_path)


class Application(App):
    def build(self):
        super(Application, self).build()
        root_widget = Builder.load_file('main_widget.kv')
        return root_widget
        # return root_widget
        # return MyButton()


if __name__ == '__main__':
    Application().run()


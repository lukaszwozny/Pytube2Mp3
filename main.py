import ntpath
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

from conversion import Converter

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

def main():
    url = 'https://www.youtube.com/watch?v=DebhiaQH3ps'
    vid_path = Converter.download_yt_video(url=url)
    Converter.convert_video_to_mp3(vid_path)
    os.remove(vid_path)


class Youtube2Mp3(App):
    def build(self):
        super(Youtube2Mp3, self).build()
        Builder.load_file('kv//conversion_screen.kv')
        Builder.load_file('kv//settings_screen.kv')
        Builder.load_file('kv//settings_entries.kv')
        root_widget = Builder.load_file('kv//main_widget.kv')
        return root_widget


if __name__ == '__main__':
    # remove all from tmp/ folder
    directory = 'tmp'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for file in os.listdir(directory):
        os.remove(ntpath.join(directory, file))
    Youtube2Mp3().run()
